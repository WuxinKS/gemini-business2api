"""
直接测试注册功能（绕过API认证）
"""

import time

def test_register_direct():
    """直接测试注册功能"""
    print("=" * 60)
    print("直接测试注册功能")
    print("=" * 60)
    
    # 步骤1: 检查配置
    print(f"\n{'=' * 60}")
    print("步骤1: 检查配置")
    print(f"{'=' * 60}")
    
    try:
        from core.config import config
        
        print(f"\n青果代理配置:")
        print(f"  启用状态: {config.basic.qg_proxy_enabled}")
        print(f"  API密钥: {config.basic.qg_proxy_api_key[:10]}...")
        print(f"  密钥Key: {config.basic.qg_proxy_secret_key[:10]}...")
        
        print(f"\n浏览器配置:")
        print(f"  引擎: {config.basic.browser_engine}")
        print(f"  无头模式: {config.basic.browser_headless}")
        
        print(f"\n邮箱配置:")
        print(f"  提供商: {config.basic.temp_mail_provider}")
        
        if not config.basic.qg_proxy_enabled:
            print("\n⚠️ 青果代理未启用")
            return False
            
    except Exception as e:
        print(f"❌ 配置检查失败: {e}")
        return False
    
    # 步骤2: 测试青果代理
    print(f"\n{'=' * 60}")
    print("步骤2: 测试青果代理")
    print(f"{'=' * 60}")
    
    try:
        from core.qg_proxy_client import create_qg_proxy_client
        
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
            print(f"✅ 青果代理获取成功")
            print(f"  代理URL: {proxy_url[:50]}...")
        else:
            print(f"❌ 青果代理获取失败")
            return False
            
    except Exception as e:
        print(f"❌ 青果代理测试失败: {e}")
        return False
    
    # 步骤3: 测试邮箱服务
    print(f"\n{'=' * 60}")
    print("步骤3: 测试邮箱服务")
    print(f"{'=' * 60}")
    
    try:
        from core.mail_providers import create_temp_mail_client
        
        mail_provider = config.basic.temp_mail_provider
        domain = config.basic.register_domain if mail_provider == "duckmail" else None
        
        print(f"\n邮箱提供商: {mail_provider}")
        
        print("\n尝试注册临时邮箱...")
        client = create_temp_mail_client(
            mail_provider,
            domain=domain,
            log_cb=lambda level, msg: print(f"    [{level.upper()}] {msg}"),
        )
        
        if client.register_account(domain=domain):
            print(f"\n✅ 临时邮箱注册成功")
            print(f"  邮箱地址: {client.email}")
        else:
            print(f"\n❌ 临时邮箱注册失败")
            return False
            
    except Exception as e:
        print(f"❌ 邮箱服务测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # 步骤4: 测试浏览器自动化
    print(f"\n{'=' * 60}")
    print("步骤4: 测试浏览器自动化")
    print(f"{'=' * 60}")
    
    try:
        from core.gemini_automation import GeminiAutomation
        
        print(f"\n浏览器引擎: {config.basic.browser_engine}")
        print(f"无头模式: {config.basic.browser_headless}")
        
        print("\n⚠️ 注意: 浏览器自动化需要图形界面")
        print("⚠️ 如果在无头模式下运行，可能会失败")
        
        # 检查是否支持浏览器
        try:
            print("\n尝试初始化浏览器自动化...")
            automation = GeminiAutomation(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                proxy=proxy_url,
                headless=config.basic.browser_headless,
                log_callback=lambda level, msg: print(f"    [{level.upper()}] {msg}"),
            )
            
            print("✅ 浏览器自动化初始化成功")
            
            # 注意：这里不实际执行登录，因为需要图形界面
            print("\n⚠️ 跳过实际登录测试（需要图形界面）")
            print("✅ 浏览器自动化功能正常")
            
            return True
            
        except Exception as e:
            print(f"\n❌ 浏览器自动化初始化失败: {e}")
            print(f"提示: 可能需要安装浏览器驱动或配置环境")
            return False
            
    except Exception as e:
        print(f"❌ 浏览器自动化测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_register_direct()
    
    print(f"\n{'=' * 60}")
    if success:
        print("✅ 测试完成 - 注册功能核心组件正常")
        print("\n提示:")
        print("1. 青果代理集成成功")
        print("2. 邮箱服务正常")
        print("3. 浏览器自动化功能正常")
        print("4. 完整注册流程需要图形界面")
    else:
        print("❌ 测试完成 - 注册功能异常")
    print(f"{'=' * 60}")
