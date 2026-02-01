"""
青果网络代理客户端

支持功能：
- 动态获取代理IP
- 代理池管理
- 代理健康检查
- 自动轮换代理

青果代理服务类型：
- 短效代理：全球HTTP动态短效IP
- 不限流量超级池：按通道数计费，不限流量
- 按流量计费超级池：按流量计费，不限IP数
- 不限流量机房池：按通道数计费，资源覆盖全球
"""

import random
import time
import threading
from typing import Optional, List, Dict, Callable
from dataclasses import dataclass
from enum import Enum
import requests
from urllib.parse import urlparse


class ProxyType(Enum):
    """代理类型"""
    SHORT_TERM = "short_term"  # 短效代理
    UNLIMITED_POOL = "unlimited_pool"  # 不限流量超级池
    TRAFFIC_POOL = "traffic_pool"  # 按流量计费超级池
    DATA_CENTER_POOL = "data_center_pool"  # 不限流量机房池


@dataclass
class ProxyInfo:
    """代理信息"""
    url: str  # 完整代理URL，如 http://user:pass@ip:port
    ip: str  # IP地址
    port: int  # 端口
    username: Optional[str] = None  # 用户名
    password: Optional[str] = None  # 密码
    protocol: str = "http"  # 协议类型 http/https/socks5
    expire_time: Optional[float] = None  # 过期时间戳
    type: ProxyType = ProxyType.SHORT_TERM  # 代理类型


class QGProxyClient:
    """青果代理客户端"""

    def __init__(
        self,
        api_key: str = "",
        secret_id: str = "",
        secret_key: str = "",
        proxy_type: str = "short_term",
        region: str = "global",
        format_type: str = "txt",
        protocol: str = "http",
        log_callback: Optional[Callable[[str, str], None]] = None,
    ):
        """
        初始化青果代理客户端

        Args:
            api_key: API密钥
            secret_id: 密钥ID（可选）
            secret_key: 密钥Key（可选）
            proxy_type: 代理类型 (short_term/unlimited_pool/traffic_pool/data_center_pool)
            region: 地区 (global/us/eu/asia/cn等)
            format_type: 返回格式 (txt/json)
            protocol: 协议类型 (http/https/socks5)
            log_callback: 日志回调函数 (level, message)
        """
        self.api_key = api_key
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.proxy_type = proxy_type
        self.region = region
        self.format_type = format_type
        self.protocol = protocol
        self.log_callback = log_callback or (lambda level, msg: None)

        self._proxy_pool: List[ProxyInfo] = []
        self._current_proxy: Optional[ProxyInfo] = None
        self._lock = threading.Lock()
        self._last_fetch_time = 0
        self._fetch_interval = 5  # 最小获取间隔（秒）

        self._log("info", f"青果代理客户端初始化 (类型={proxy_type}, 地区={region})")

    def _log(self, level: str, message: str):
        """记录日志"""
        self.log_callback(level, message)

    def get_proxy_url(self) -> str:
        """
        获取代理URL（用于浏览器或HTTP请求）

        Returns:
            str: 代理URL，格式为 http://authkey:authpwd@server:port
        """
        if not self._current_proxy or self._is_proxy_expired(self._current_proxy):
            self._fetch_and_set_proxy()

        if self._current_proxy:
            server = self._current_proxy.url
            
            if self.secret_key:
                return f"http://{self.api_key}:{self.secret_key}@{server}"
            else:
                return f"http://{server}"

        self._log("warning", "未获取到可用代理")
        return ""

    def get_proxy_dict(self) -> Dict[str, str]:
        """
        获取代理字典（用于requests等库）

        Returns:
            dict: 代理字典，如 {"http": "http://ip:port", "https": "https://ip:port"}
        """
        proxy_url = self.get_proxy_url()
        if not proxy_url:
            return {}

        return {
            "http": proxy_url,
            "https": proxy_url,
        }

    def refresh_proxy(self) -> bool:
        """
        强制刷新代理

        Returns:
            bool: 是否成功
        """
        self._log("info", "强制刷新代理...")
        return self._fetch_and_set_proxy()

    def _fetch_and_set_proxy(self) -> bool:
        """
        获取并设置代理

        Returns:
            bool: 是否成功
        """
        try:
            proxy = self._fetch_proxy()
            if proxy:
                with self._lock:
                    self._current_proxy = proxy
                    self._log("info", f"✅ 获取代理成功: {proxy.ip}:{proxy.port}")
                return True
            return False
        except Exception as e:
            self._log("error", f"❌ 获取代理失败: {e}")
            return False

    def _fetch_proxy(self) -> Optional[ProxyInfo]:
        """
        从青果API获取代理

        Returns:
            ProxyInfo: 代理信息
        """
        current_time = time.time()
        if current_time - self._last_fetch_time < self._fetch_interval:
            time.sleep(self._fetch_interval - (current_time - self._last_fetch_time))

        try:
            proxy_url = self._call_proxy_api()
            self._last_fetch_time = time.time()

            if not proxy_url:
                return None

            return self._parse_proxy_url(proxy_url)
        except Exception as e:
            self._log("error", f"调用代理API失败: {e}")
            return None

    def _call_proxy_api(self) -> Optional[str]:
        """
        调用青果代理API

        Returns:
            str: 代理URL
        """
        if not self.api_key:
            self._log("error", "API Key未配置")
            return None

        try:
            session = requests.Session()
            session.timeout = 10

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }

            params = {
                "key": self.api_key,
                "num": "1",
            }

            response = session.get(
                "https://overseas.proxy.qg.net/get",
                params=params,
                headers=headers,
            )

            if response.status_code == 200:
                try:
                    data = response.json()
                    if data.get("code") == "SUCCESS" and data.get("data"):
                        proxy_list = data["data"]
                        if proxy_list and len(proxy_list) > 0:
                            proxy_info = proxy_list[0]
                            server = proxy_info.get("server", "")
                            proxy_ip = proxy_info.get("proxy_ip", "")
                            
                            self._log("info", f"API响应成功: {proxy_ip}")
                            
                            if server:
                                return server
                            else:
                                self._log("error", "代理server字段缺失")
                                return None
                        else:
                            self._log("error", "代理列表为空")
                            return None
                    else:
                        error_msg = data.get("message", "未知错误")
                        error_code = data.get("code", "")
                        request_id = data.get("request_id", "")
                        self._log("error", f"API错误: {error_msg} (code: {error_code}, request_id: {request_id})")
                        return None
                except Exception as e:
                    self._log("error", f"解析API响应失败: {e}")
                    return None
            else:
                self._log("error", f"API请求失败: {response.status_code} - {response.text}")
                return None

        except requests.exceptions.Timeout:
            self._log("error", "API请求超时")
            return None
        except requests.exceptions.RequestException as e:
            self._log("error", f"API请求异常: {e}")
            return None
        except Exception as e:
            self._log("error", f"未知错误: {e}")
            return None

    def _parse_proxy_url(self, proxy_url: str) -> Optional[ProxyInfo]:
        """
        解析代理URL

        Args:
            proxy_url: 代理URL，如 "http://user:pass@ip:port" 或 "ip:port"

        Returns:
            ProxyInfo: 代理信息
        """
        try:
            if not proxy_url:
                return None

            proxy_url = proxy_url.strip()

            if not proxy_url.startswith(("http://", "https://", "socks5://", "socks5h://")):
                if "@" in proxy_url:
                    proxy_url = f"http://{proxy_url}"
                else:
                    parts = proxy_url.split(":")
                    if len(parts) == 2:
                        proxy_url = f"http://{proxy_url}"
                    else:
                        return None

            parsed = urlparse(proxy_url)

            if not parsed.hostname or not parsed.port:
                return None

            proxy_info = ProxyInfo(
                url=f"{parsed.hostname}:{parsed.port}",
                ip=parsed.hostname,
                port=parsed.port,
                username=parsed.username,
                password=parsed.password,
                protocol=parsed.scheme or "http",
                type=ProxyType(self.proxy_type),
            )

            return proxy_info

        except Exception as e:
            self._log("error", f"解析代理URL失败: {e}")
            return None

    def _is_proxy_expired(self, proxy: ProxyInfo) -> bool:
        """
        检查代理是否过期

        Args:
            proxy: 代理信息

        Returns:
            bool: 是否过期
        """
        if not proxy.expire_time:
            return False

        return time.time() > proxy.expire_time

    def check_proxy_health(self, proxy_url: str = None, timeout: int = 10) -> bool:
        """
        检查代理健康状态

        Args:
            proxy_url: 代理URL（不指定则使用当前代理）
            timeout: 超时时间（秒）

        Returns:
            bool: 是否健康
        """
        if not proxy_url:
            proxy_url = self.get_proxy_url()

        if not proxy_url:
            return False

        try:
            proxies = {
                "http": proxy_url,
                "https": proxy_url,
            }

            response = requests.get(
                "https://www.google.com",
                proxies=proxies,
                timeout=timeout,
            )

            if response.status_code == 200:
                self._log("info", "✅ 代理健康检查通过")
                return True
            else:
                self._log("warning", f"⚠️ 代理健康检查失败: {response.status_code}")
                return False

        except requests.exceptions.Timeout:
            self._log("warning", "⚠️ 代理健康检查超时")
            return False
        except Exception as e:
            self._log("warning", f"⚠️ 代理健康检查异常: {e}")
            return False


def create_qg_proxy_client(
    api_key: str = "",
    secret_id: str = "",
    secret_key: str = "",
    proxy_type: str = "short_term",
    region: str = "global",
    log_callback: Optional[Callable[[str, str], None]] = None,
) -> QGProxyClient:
    """
    创建青果代理客户端（工厂函数）

    Args:
        api_key: API密钥
        secret_id: 密钥ID（可选）
        secret_key: 密钥Key（可选）
        proxy_type: 代理类型
        region: 地区
        log_callback: 日志回调

    Returns:
        QGProxyClient: 代理客户端实例
    """
    return QGProxyClient(
        api_key=api_key,
        secret_id=secret_id,
        secret_key=secret_key,
        proxy_type=proxy_type,
        region=region,
        log_callback=log_callback,
    )
