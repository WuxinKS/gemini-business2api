"""
测试青果代理 - 使用账密模式
"""

import requests
import json

def test_qg_proxy_with_auth():
    """测试青果代理使用账密模式"""
    print("=" * 60)
    print("青果代理账密模式测试")
    print("=" * 60)
    
    API_KEY = "A7F2B120"
    PASSWORD = ""  # 如果有密码，请填写
    
    print(f"\nAPI密钥: {API_KEY}")
    print(f"密码: {'已设置' if PASSWORD else '未设置'}")
    
    # 先获取代理
    print(f"\n{'=' * 60}")
    print("步骤1: 获取代理")
    print(f"{'=' * 60}")
    
    try:
        response = requests.get(
            "https://overseas.proxy.qg.net/get",
            params={
                "key": API_KEY,
                "num": "1"
            },
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == "SUCCESS" and data.get("data"):
                proxy_list = data["data"]
                if proxy_list and len(proxy_list) > 0:
                    proxy = proxy_list[0]
                    server = proxy.get("server", "")
                    proxy_ip = proxy.get("proxy_ip", "")
                    area = proxy.get("area", "")
                    
                    print(f"\n✅ 成功获取代理")
                    print(f"  代理IP: {proxy_ip}")
                    print(f"  服务器: {server}")
                    print(f"  地区: {area}")
                    
                    # 步骤2: 测试代理连接
                    print(f"\n{'=' * 60}")
                    print("步骤2: 测试代理连接")
                    print(f"{'=' * 60}")
                    
                    # 尝试不同的认证方式
                    
                    # 方式1: 不使用认证
                    print(f"\n方式1: 不使用认证")
                    print(f"  代理URL: http://{server}")
                    test_proxy(server, None, None)
                    
                    # 方式2: 使用API Key作为用户名
                    print(f"\n方式2: 使用API Key作为用户名")
                    print(f"  代理URL: http://{API_KEY}@{server}")
                    test_proxy(server, API_KEY, None)
                    
                    # 方式3: 使用API Key作为用户名，密码为空
                    print(f"\n方式3: 使用API Key作为用户名，密码为空")
                    print(f"  代理URL: http://{API_KEY}:@{server}")
                    test_proxy(server, API_KEY, "")
                    
                    # 方式4: 如果有密码，使用密码
                    if PASSWORD:
                        print(f"\n方式4: 使用API Key和密码")
                        print(f"  代理URL: http://{API_KEY}:{PASSWORD}@{server}")
                        test_proxy(server, API_KEY, PASSWORD)
                    
                    return True
        else:
            print(f"\n❌ 获取代理失败: {response.status_code}")
            print(f"响应: {response.text}")
            return False
            
    except Exception as e:
        print(f"\n❌ 异常: {e}")
        return False

def test_proxy(server, username, password):
    """测试代理连接"""
    try:
        if username and password:
            proxy_url = f"http://{username}:{password}@{server}"
        elif username:
            proxy_url = f"http://{username}@{server}"
        else:
            proxy_url = f"http://{server}"
        
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        
        print(f"  正在连接...")
        response = requests.get(
            "https://ip.sb",
            proxies=proxies,
            timeout=10
        )
        
        if response.status_code == 200:
            print(f"  ✅ 成功！")
            print(f"  响应: {response.text.strip()}")
            return True
        else:
            print(f"  ❌ 失败: {response.status_code}")
            return False
            
    except requests.exceptions.ProxyError as e:
        print(f"  ❌ 代理错误: {e}")
        return False
    except Exception as e:
        print(f"  ❌ 异常: {e}")
        return False

if __name__ == "__main__":
    test_qg_proxy_with_auth()
    
    print(f"\n{'=' * 60}")
    print("测试完成")
    print(f"{'=' * 60}")
    print("\n提示:")
    print("1. 如果所有方式都失败，可能需要从青果网络后台获取AuthPwd")
    print("2. 访问 https://www.qg.net/ 查看账户信息")
    print("3. 如果有密码，请在脚本中设置PASSWORD变量")
