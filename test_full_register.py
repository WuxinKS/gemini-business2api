"""
完整注册流程测试 - 实际执行注册
"""

import time

def test_full_register():
    """完整测试注册流程"""
    print("=" * 60)
    print("完整注册流程测试")
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
    
    # 步骤2: 获取青果代理
    print(f"\n{'=' * 60}")
    print("步骤2: 获取青果代理")
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
    
    # 步骤3: 注册临时邮箱
    print(f"\n{'=' * 60}")
    print("步骤3: 注册临时邮箱")
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
    
    # 步骤4: 执行Gemini注册
    print(f"\n{'=' * 60}")
    print("步骤4: 执行Gemini注册")
    print(f"{'=' * 60}")
    
    try:
        from core.gemini_automation import GeminiAutomation
        
        print(f"\n浏览器引擎: {config.basic.browser_engine}")
        print(f"无头模式: {config.basic.browser_headless}")
        print(f"代理: {proxy_url[:50]}...")
        print(f"邮箱: {client.email}")
        
        print("\n正在初始化浏览器自动化...")
        automation = GeminiAutomation(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            proxy=proxy_url,
            headless=config.basic.browser_headless,
            log_callback=lambda level, msg: print(f"    [{level.upper()}] {msg}"),
        )
        
        print("✅ 浏览器自动化初始化成功")
        
        print("\n正在执行Gemini注册流程...")
        print("⚠️ 注意: 这将打开浏览器并执行自动化操作")
        print("⚠️ 请不要干扰浏览器操作")
        
        result = automation.login_and_extract(client.email, client)
        
        if result.get("success"):
            print(f"\n✅ Gemini注册成功！")
            print(f"  账户ID: {result['config'].get('id')}")
            print(f"  邮箱: {client.email}")
            
            # 步骤5: 保存账户配置
            print(f"\n{'=' * 60}")
            print("步骤5: 保存账户配置")
            print(f"{'=' * 60}")
            
            try:
                from core.account import load_accounts_from_source, save_accounts_to_source
                
                config_data = result["config"]
                config_data["mail_provider"] = mail_provider
                config_data["mail_address"] = client.email
                config_data["mail_password"] = getattr(client, "password", "")
                config_data["mail_base_url"] = config.basic.duckmail_base_url
                config_data["mail_api_key"] = config.basic.duckmail_api_key
                
                accounts_data = load_accounts_from_source()
                updated = False
                for acc in accounts_data:
                    if acc.get("id") == config_data["id"]:
                        acc.update(config_data)
                        updated = True
                        break
                
                if not updated:
                    accounts_data.append(config_data)
                
                save_accounts_to_source(accounts_data)
                
                print(f"✅ 账户配置保存成功")
                
                print(f"\n{'=' * 60}")
                print("🎉 完整注册流程成功！")
                print(f"{'=' * 60}")
                print(f"\n注册信息:")
                print(f"  账户ID: {config_data.get('id')}")
                print(f"  邮箱: {client.email}")
                print(f"  代理: {proxy_url[:50]}...")
                print(f"  邮箱提供商: {mail_provider}")
                
                return True
                
            except Exception as e:
                print(f"❌ 保存账户配置失败: {e}")
                import traceback
                traceback.print_exc()
                return False
        else:
            error = result.get("error", "未知错误")
            print(f"\n❌ Gemini注册失败: {error}")
            return False
            
    except Exception as e:
        print(f"❌ Gemini注册流程失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_full_register()
    
    print(f"\n{'=' * 60}")
    if success:
        print("✅ 测试完成 - 注册成功")
    else:
        print("❌ 测试完成 - 注册失败")
    print(f"{'=' * 60}")
