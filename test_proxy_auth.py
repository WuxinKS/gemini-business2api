"""
测试青果代理 - 使用之前获取的代理
"""

import requests

def test_proxy_authentication():
    """测试代理的不同认证方式"""
    print("=" * 60)
    print("青果代理认证测试")
    print("=" * 60)
    
    API_KEY = "A7F2B120"
    PROXY_SERVER = "45.131.177.12:20315"  # 之前成功获取的代理
    
    print(f"\nAPI密钥: {API_KEY}")
    print(f"代理服务器: {PROXY_SERVER}")
    
    # 测试不同的认证方式
    test_cases = [
        {
            "name": "方式1: 不使用认证",
            "username": None,
            "password": None
        },
        {
            "name": "方式2: 使用API Key作为用户名",
            "username": API_KEY,
            "password": None
        },
        {
            "name": "方式3: 使用API Key作为用户名，密码为空",
            "username": API_KEY,
            "password": ""
        },
        {
            "name": "方式4: 使用API Key作为用户名和密码",
            "username": API_KEY,
            "password": API_KEY
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'=' * 60}")
        print(f"{test_case['name']}")
        print(f"{'=' * 60}")
        
        username = test_case["username"]
        password = test_case["password"]
        
        if username and password:
            proxy_url = f"http://{username}:{password}@{PROXY_SERVER}"
        elif username:
            proxy_url = f"http://{username}@{PROXY_SERVER}"
        else:
            proxy_url = f"http://{PROXY_SERVER}"
        
        print(f"代理URL: {proxy_url}")
        
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        
        try:
            print("正在连接到 https://ip.sb...")
            response = requests.get(
                "https://ip.sb",
                proxies=proxies,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✅ 成功！")
                print(f"响应: {response.text.strip()}")
                
                # 测试第二个请求验证
                print("\n再次验证...")
                response2 = requests.get(
                    "https://ip.sb",
                    proxies=proxies,
                    timeout=10
                )
                if response2.status_code == 200:
                    print(f"✅ 验证成功！")
                    print(f"响应: {response2.text.strip()}")
                    
                    print(f"\n🎉 找到正确的认证方式: {test_case['name']}")
                    return proxy_url
            else:
                print(f"❌ 失败: {response.status_code}")
                
        except requests.exceptions.ProxyError as e:
            error_msg = str(e)
            if "407" in error_msg:
                print(f"❌ 代理认证失败 (407)")
            else:
                print(f"❌ 代理错误: {e}")
        except Exception as e:
            print(f"❌ 异常: {e}")
    
    print(f"\n{'=' * 60}")
    print("测试完成")
    print(f"{'=' * 60}")
    print("\n所有认证方式都失败了。")
    print("可能的原因:")
    print("1. 代理已过期")
    print("2. 需要从青果网络后台获取AuthPwd")
    print("3. API Key不是正确的认证方式")
    print("\n建议:")
    print("1. 访问 https://www.qg.net/ 查看账户信息")
    print("2. 查看青果网络官方文档了解正确的认证方式")
    print("3. 联系青果网络客服获取帮助")
    
    return None

if __name__ == "__main__":
    test_proxy_authentication()
