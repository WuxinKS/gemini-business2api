"""
直接测试青果代理API - 使用诊断脚本的成功模式
"""

import requests
import json

def test_qg_proxy_direct():
    """直接测试青果代理API"""
    print("=" * 60)
    print("青果代理直接测试")
    print("=" * 60)
    
    API_KEY = "A7F2B120"
    
    print(f"\nAPI密钥: {API_KEY}")
    print(f"API端点: https://overseas.proxy.qg.net/get")
    print(f"参数: key={API_KEY}, num=1")
    
    try:
        response = requests.get(
            "https://overseas.proxy.qg.net/get",
            params={
                "key": API_KEY,
                "num": "1"
            },
            timeout=10
        )
        
        print(f"\n状态码: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"\n响应数据:")
                print(json.dumps(data, ensure_ascii=False, indent=2))
                
                if data.get("code") == "SUCCESS":
                    print("\n✅ 成功！")
                    if data.get("data"):
                        proxy_list = data["data"]
                        print(f"获取到 {len(proxy_list)} 个代理")
                        
                        if len(proxy_list) > 0:
                            proxy = proxy_list[0]
                            server = proxy.get("server", "")
                            proxy_ip = proxy.get("proxy_ip", "")
                            area = proxy.get("area", "")
                            deadline = proxy.get("deadline", "")
                            
                            print(f"\n代理详情:")
                            print(f"  代理IP: {proxy_ip}")
                            print(f"  服务器: {server}")
                            print(f"  地区: {area}")
                            print(f"  过期时间: {deadline}")
                            
                            if server:
                                proxy_url = f"http://{server}"
                                print(f"\n代理URL: {proxy_url}")
                                return proxy_url
                else:
                    error_msg = data.get("message", "未知错误")
                    error_code = data.get("code", "")
                    request_id = data.get("request_id", "")
                    print(f"\n❌ 失败: {error_msg}")
                    print(f"错误代码: {error_code}")
                    print(f"请求ID: {request_id}")
                    
            except json.JSONDecodeError:
                print(f"\n响应文本:")
                print(response.text)
        else:
            print(f"\n❌ 请求失败: {response.status_code}")
            print(f"响应: {response.text}")
            
    except requests.exceptions.Timeout:
        print("\n❌ 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ 请求异常: {e}")
    except Exception as e:
        print(f"\n❌ 未知错误: {e}")
    
    return None

def test_proxy_connection(proxy_url):
    """测试代理连接"""
    print(f"\n{'=' * 60}")
    print("测试代理连接")
    print(f"{'=' * 60}")
    
    print(f"\n代理URL: {proxy_url}")
    
    try:
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        
        print("\n正在测试代理连接到 https://ip.sb...")
        response = requests.get(
            "https://ip.sb",
            proxies=proxies,
            timeout=10
        )
        
        print(f"状态码: {response.status_code}")
        print(f"响应: {response.text.strip()}")
        
        if response.status_code == 200:
            print("\n✅ 代理连接成功！")
            return True
        else:
            print("\n❌ 代理连接失败")
            return False
            
    except Exception as e:
        print(f"\n❌ 代理连接异常: {e}")
        return False

if __name__ == "__main__":
    proxy_url = test_qg_proxy_direct()
    
    if proxy_url:
        test_proxy_connection(proxy_url)
    
    print(f"\n{'=' * 60}")
    print("测试完成")
    print(f"{'=' * 60}")
