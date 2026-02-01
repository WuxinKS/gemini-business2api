"""
测试青果代理 - 使用之前获取的代理和正确的认证
"""

import requests

def test_with_previous_proxy():
    """使用之前获取的代理和正确的认证信息测试"""
    print("=" * 60)
    print("青果代理认证测试（使用之前获取的代理）")
    print("=" * 60)
    
    AUTH_KEY = "A7F2B120"
    AUTH_PWD = "0CF9CD95C391"
    PROXY_SERVER = "45.131.177.12:20315"  # 之前成功获取的代理
    
    print(f"\nAuthkey: {AUTH_KEY}")
    print(f"Authpwd: {AUTH_PWD}")
    print(f"代理服务器: {PROXY_SERVER}")
    
    # 使用正确的认证方式
    proxy_url = f"http://{AUTH_KEY}:{AUTH_PWD}@{PROXY_SERVER}"
    print(f"\n代理URL: http://{AUTH_KEY}:***@{PROXY_SERVER}")
    
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    
    print(f"\n{'=' * 60}")
    print("测试代理连接")
    print(f"{'=' * 60}")
    
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
                
                # 测试其他网站
                print("\n测试其他网站 (https://api.ipify.org)...")
                response3 = requests.get(
                    "https://api.ipify.org?format=json",
                    proxies=proxies,
                    timeout=10
                )
                if response3.status_code == 200:
                    print(f"✅ 成功！")
                    print(f"响应: {response3.text.strip()}")
                
                print(f"\n{'=' * 60}")
                print("🎉 青果代理认证成功！")
                print(f"{'=' * 60}")
                print(f"\n代理信息:")
                print(f"  服务器: {PROXY_SERVER}")
                print(f"  认证方式: Authkey + Authpwd")
                print(f"  代理URL: http://{AUTH_KEY}:{AUTH_PWD}@{PROXY_SERVER}")
                
                return True
        else:
            print(f"❌ 失败: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ 异常: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_with_previous_proxy()
    
    print(f"\n{'=' * 60}")
    if success:
        print("✅ 测试完成 - 青果代理可用")
    else:
        print("❌ 测试完成 - 青果代理不可用")
    print(f"{'=' * 60}")
