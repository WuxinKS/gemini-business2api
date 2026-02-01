"""
测试青果代理 - 使用HTTP协议测试
"""

import requests

def test_with_http():
    """使用HTTP协议测试代理"""
    print("=" * 60)
    print("青果代理HTTP协议测试")
    print("=" * 60)
    
    AUTH_KEY = "A7F2B120"
    AUTH_PWD = "0CF9CD95C391"
    PROXY_SERVER = "45.131.177.12:20315"
    
    print(f"\nAuthkey: {AUTH_KEY}")
    print(f"Authpwd: {AUTH_PWD}")
    print(f"代理服务器: {PROXY_SERVER}")
    
    proxy_url = f"http://{AUTH_KEY}:{AUTH_PWD}@{PROXY_SERVER}"
    print(f"\n代理URL: http://{AUTH_KEY}:***@{PROXY_SERVER}")
    
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    
    print(f"\n{'=' * 60}")
    print("测试HTTP连接")
    print(f"{'=' * 60}")
    
    # 测试HTTP网站
    try:
        print("正在连接到 http://httpbin.org/ip...")
        response = requests.get(
            "http://httpbin.org/ip",
            proxies=proxies,
            timeout=10
        )
        
        if response.status_code == 200:
            print(f"✅ 成功！")
            print(f"响应: {response.text.strip()}")
            
            # 再次验证
            print("\n再次验证...")
            response2 = requests.get(
                "http://httpbin.org/ip",
                proxies=proxies,
                timeout=10
            )
            if response2.status_code == 200:
                print(f"✅ 验证成功！")
                print(f"响应: {response2.text.strip()}")
                
                print(f"\n{'=' * 60}")
                print("🎉 青果代理HTTP连接成功！")
                print(f"{'=' * 60}")
                
                return True
        else:
            print(f"❌ 失败: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ 异常: {e}")
        return False

if __name__ == "__main__":
    success = test_with_http()
    
    print(f"\n{'=' * 60}")
    if success:
        print("✅ 测试完成 - 青果代理HTTP可用")
    else:
        print("❌ 测试完成 - 青果代理HTTP不可用")
    print(f"{'=' * 60}")
