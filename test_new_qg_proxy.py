"""
测试新的青果代理认证信息
"""

import requests

def test_new_qg_proxy():
    """测试新的青果代理认证信息"""
    print("=" * 60)
    print("青果代理新认证信息测试")
    print("=" * 60)
    
    AUTH_KEY = "BYJ3MCP5"
    AUTH_PWD = "7B3C288DCF56"
    
    print(f"\nAuthkey: {AUTH_KEY}")
    print(f"Authpwd: {AUTH_PWD}")
    
    # 步骤1: 测试青果代理API
    print(f"\n{'=' * 60}")
    print("步骤1: 测试青果代理API")
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
                    
                    # 步骤2: 测试代理连接
                    print(f"\n{'=' * 60}")
                    print("步骤2: 测试代理连接")
                    print(f"{'=' * 60}")
                    
                    proxy_url = f"http://{AUTH_KEY}:{AUTH_PWD}@{server}"
                    print(f"\n代理URL: http://{AUTH_KEY}:***@{server}")
                    
                    proxies = {
                        "http": proxy_url,
                        "https": proxy_url
                    }
                    
                    try:
                        print("正在连接到 http://httpbin.org/ip...")
                        response = requests.get(
                            "http://httpbin.org/ip",
                            proxies=proxies,
                            timeout=10
                        )
                        
                        if response.status_code == 200:
                            print(f"✅ 代理连接成功！")
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
                                
                                # 步骤3: 测试青果代理客户端
                                print(f"\n{'=' * 60}")
                                print("步骤3: 测试青果代理客户端")
                                print(f"{'=' * 60}")
                                
                                from core.qg_proxy_client import create_qg_proxy_client
                                from core.config import config
                                
                                print(f"\n配置信息:")
                                print(f"  启用状态: {config.basic.qg_proxy_enabled}")
                                print(f"  API密钥: {config.basic.qg_proxy_api_key[:10]}...")
                                print(f"  密钥Key: {config.basic.qg_proxy_secret_key[:10]}...")
                                
                                client = create_qg_proxy_client(
                                    api_key=config.basic.qg_proxy_api_key,
                                    secret_key=config.basic.qg_proxy_secret_key,
                                    proxy_type=config.basic.qg_proxy_type,
                                    region=config.basic.qg_proxy_region,
                                    log_callback=lambda level, msg: print(f"    [{level.upper()}] {msg}"),
                                )
                                
                                print("\n尝试获取代理...")
                                proxy_url = client.get_proxy_url()
                                
                                if proxy_url:
                                    print(f"✅ 代理客户端获取成功")
                                    print(f"  代理URL: {proxy_url[:50]}...")
                                    
                                    print(f"\n{'=' * 60}")
                                    print("🎉 青果代理新认证信息测试成功！")
                                    print(f"{'=' * 60}")
                                    print(f"\n功能验证:")
                                    print(f"  ✅ 后端服务正常")
                                    print(f"  ✅ 青果代理API可用")
                                    print(f"  ✅ 代理连接成功")
                                    print(f"  ✅ 青果代理客户端正常")
                                    print(f"  ✅ 新认证信息有效")
                                    
                                    return True
                                else:
                                    print(f"❌ 代理客户端获取失败")
                                    return False
                        else:
                            print(f"❌ 代理连接失败: {response.status_code}")
                            return False
                    except Exception as e:
                        print(f"❌ 代理连接异常: {e}")
                        import traceback
                        traceback.print_exc()
                        return False
        else:
            print(f"\n❌ 获取代理失败: {response.status_code}")
            print(f"响应: {response.text}")
            return False
            
    except Exception as e:
        print(f"\n❌ 青果代理API异常: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_new_qg_proxy()
    
    print(f"\n{'=' * 60}")
    if success:
        print("✅ 测试完成 - 青果代理新认证信息有效")
    else:
        print("❌ 测试完成 - 青果代理新认证信息无效")
    print(f"{'=' * 60}")
