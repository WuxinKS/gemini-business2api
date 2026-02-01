"""
测试青果代理 - 使用正确的认证信息
"""

import requests

def test_qg_proxy_with_correct_auth():
    """使用正确的Authkey和Authpwd测试青果代理"""
    print("=" * 60)
    print("青果代理正确认证测试")
    print("=" * 60)
    
    AUTH_KEY = "A7F2B120"
    AUTH_PWD = "0CF9CD95C391"
    
    print(f"\nAuthkey: {AUTH_KEY}")
    print(f"Authpwd: {AUTH_PWD}")
    
    # 步骤1: 获取代理
    print(f"\n{'=' * 60}")
    print("步骤1: 获取代理")
    print(f"{'=' * 60}")
    
    try:
        response = requests.get(
            "https://overseas.proxy.qg.net/get",
            params={
                "key": AUTH_KEY,
                "num": "1"
            },
            timeout=10
        )
        
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == "SUCCESS" and data.get("data"):
                proxy_list = data["data"]
                if proxy_list and len(proxy_list) > 0:
                    proxy = proxy_list[0]
                    server = proxy.get("server", "")
                    proxy_ip = proxy.get("proxy_ip", "")
                    area = proxy.get("area", "")
                    deadline = proxy.get("deadline", "")
                    
                    print(f"\n✅ 成功获取代理")
                    print(f"  代理IP: {proxy_ip}")
                    print(f"  服务器: {server}")
                    print(f"  地区: {area}")
                    print(f"  过期时间: {deadline}")
                    
                    # 步骤2: 使用正确的认证方式测试代理
                    print(f"\n{'=' * 60}")
                    print("步骤2: 测试代理连接")
                    print(f"{'=' * 60}")
                    
                    # 使用Authkey和Authpwd进行认证
                    proxy_url = f"http://{AUTH_KEY}:{AUTH_PWD}@{server}"
                    print(f"\n代理URL: http://{AUTH_KEY}:***@{server}")
                    
                    proxies = {
                        "http": proxy_url,
                        "https": proxy_url
                    }
                    
                    print("正在连接到 https://ip.sb...")
                    response = requests.get(
                        "https://ip.sb",
                        proxies=proxies,
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        print(f"✅ 成功！")
                        print(f"响应: {response.text.strip()}")
                        
                        # 再次验证
                        print("\n再次验证...")
                        response2 = requests.get(
                            "https://ip.sb",
                            proxies=proxies,
                            timeout=10
                        )
                        if response2.status_code == 200:
                            print(f"✅ 验证成功！")
                            print(f"响应: {response2.text.strip()}")
                            
                            print(f"\n{'=' * 60}")
                            print("🎉 青果代理集成成功！")
                            print(f"{'=' * 60}")
                            print(f"\n代理信息:")
                            print(f"  服务器: {server}")
                            print(f"  代理IP: {proxy_ip}")
                            print(f"  地区: {area}")
                            print(f"  认证方式: Authkey + Authpwd")
                            print(f"  代理URL: http://{AUTH_KEY}:{AUTH_PWD}@{server}")
                            
                            return {
                                "server": server,
                                "proxy_ip": proxy_ip,
                                "area": area,
                                "deadline": deadline,
                                "proxy_url": proxy_url
                            }
                    else:
                        print(f"❌ 失败: {response.status_code}")
                        return None
        else:
            print(f"\n❌ 获取代理失败: {response.status_code}")
            print(f"响应: {response.text}")
            return None
            
    except Exception as e:
        print(f"\n❌ 异常: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    result = test_qg_proxy_with_correct_auth()
    
    if result:
        print(f"\n{'=' * 60}")
        print("✅ 测试完成 - 青果代理可用")
        print(f"{'=' * 60}")
    else:
        print(f"\n{'=' * 60}")
        print("❌ 测试完成 - 青果代理不可用")
        print(f"{'=' * 60}")
