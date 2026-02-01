"""
测试注册账号功能
"""

import asyncio
import requests
import time

def test_register_api():
    """测试注册API"""
    print("=" * 60)
    print("测试注册账号功能")
    print("=" * 60)
    
    # 步骤1: 检查后端服务
    print(f"\n{'=' * 60}")
    print("步骤1: 检查后端服务")
    print(f"{'=' * 60}")
    
    try:
        response = requests.get("http://localhost:7860/admin/health", timeout=5)
        if response.status_code == 200:
            print("✅ 后端服务正常运行")
        else:
            print(f"❌ 后端服务异常: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 后端服务连接失败: {e}")
        return False
    
    # 步骤2: 检查配置
    print(f"\n{'=' * 60}")
    print("步骤2: 检查配置")
    print(f"{'=' * 60}")
    
    try:
        from core.config import config
        
        print(f"\n青果代理配置:")
        print(f"  启用状态: {config.basic.qg_proxy_enabled}")
        print(f"  API密钥: {config.basic.qg_proxy_api_key[:10]}...")
        print(f"  密钥Key: {config.basic.qg_proxy_secret_key[:10]}...")
        print(f"  代理类型: {config.basic.qg_proxy_type}")
        print(f"  代理地区: {config.basic.qg_proxy_region}")
        
        print(f"\n浏览器配置:")
        print(f"  引擎: {config.basic.browser_engine}")
        print(f"  无头模式: {config.basic.browser_headless}")
        
        print(f"\n邮箱配置:")
        print(f"  提供商: {config.basic.temp_mail_provider}")
        print(f"  默认数量: {config.basic.register_default_count}")
        
        if config.basic.temp_mail_provider == "duckmail":
            print(f"  域名: {config.basic.register_domain}")
        
        if not config.basic.qg_proxy_enabled:
            print("\n⚠️ 青果代理未启用，注册可能失败")
        
    except Exception as e:
        print(f"❌ 配置检查失败: {e}")
        return False
    
    # 步骤3: 测试青果代理
    print(f"\n{'=' * 60}")
    print("步骤3: 测试青果代理")
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
    
    # 步骤4: 测试邮箱服务
    print(f"\n{'=' * 60}")
    print("步骤4: 测试邮箱服务")
    print(f"{'=' * 60}")
    
    try:
        from core.mail_providers import create_temp_mail_client
        
        mail_provider = config.basic.temp_mail_provider
        domain = config.basic.register_domain if mail_provider == "duckmail" else None
        
        print(f"\n邮箱提供商: {mail_provider}")
        if domain:
            print(f"域名: {domain}")
        
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
    
    # 步骤5: 测试注册API
    print(f"\n{'=' * 60}")
    print("步骤5: 测试注册API")
    print(f"{'=' * 60}")
    
    try:
        print("\n尝试启动注册任务...")
        
        # 准备请求数据
        data = {
            "count": 1,  # 只注册1个账号进行测试
            "mail_provider": config.basic.temp_mail_provider,
        }
        
        if config.basic.temp_mail_provider == "duckmail" and config.basic.register_domain:
            data["domain"] = config.basic.register_domain
        
        print(f"\n请求数据:")
        print(f"  数量: {data['count']}")
        print(f"  提供商: {data['mail_provider']}")
        if "domain" in data:
            print(f"  域名: {data['domain']}")
        
        # 注意：这里需要实际的API端点，可能需要认证
        print("\n⚠️ 注意: 注册API可能需要管理员认证")
        print("⚠️ 如果API认证失败，请检查管理员登录功能")
        
        # 尝试调用注册API
        try:
            response = requests.post(
                "http://localhost:7860/admin/register/start",
                json=data,
                timeout=10
            )
            
            print(f"\n状态码: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"响应: {result}")
                
                if result.get("success"):
                    print(f"\n✅ 注册任务启动成功")
                    task_id = result.get("task_id")
                    print(f"  任务ID: {task_id}")
                    
                    # 等待一段时间查看任务状态
                    print(f"\n等待5秒后检查任务状态...")
                    time.sleep(5)
                    
                    status_response = requests.get(
                        f"http://localhost:7860/admin/register/status?task_id={task_id}",
                        timeout=10
                    )
                    
                    if status_response.status_code == 200:
                        status = status_response.json()
                        print(f"\n任务状态:")
                        print(f"  状态: {status.get('status')}")
                        print(f"  进度: {status.get('progress')}")
                        print(f"  成功: {status.get('success_count')}")
                        print(f"  失败: {status.get('fail_count')}")
                        
                        logs = status.get('logs', [])
                        if logs:
                            print(f"\n最近日志:")
                            for log in logs[-5:]:
                                print(f"  [{log.get('level')}] {log.get('message')}")
                    
                    return True
                else:
                    print(f"\n❌ 注册任务启动失败")
                    print(f"错误: {result.get('error')}")
                    return False
            else:
                print(f"\n❌ API请求失败: {response.status_code}")
                print(f"响应: {response.text}")
                return False
                
        except Exception as e:
            print(f"\n❌ API调用异常: {e}")
            print(f"提示: 注册API可能需要管理员认证")
            return False
            
    except Exception as e:
        print(f"❌ 注册API测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_register_api()
    
    print(f"\n{'=' * 60}")
    if success:
        print("✅ 测试完成 - 注册功能正常")
    else:
        print("❌ 测试完成 - 注册功能异常")
    print(f"{'=' * 60}")
