"""
后端API测试脚本

测试功能：
1. 健康检查
2. 公共端点（日志、统计、运行时间）
3. 青果代理配置测试
4. 管理员登录
5. 系统设置获取
"""

import requests
import json
import time

BASE_URL = "http://localhost:7860"
ADMIN_KEY = "admin123456"

def print_section(title):
    """打印分节标题"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def print_result(name, success, data=None, error=None):
    """打印测试结果"""
    status = "✅ 成功" if success else "❌ 失败"
    print(f"\n{name}: {status}")
    if data:
        print(f"  数据: {json.dumps(data, ensure_ascii=False, indent=2)[:200]}...")
    if error:
        print(f"  错误: {error}")

def test_health_check():
    """测试健康检查"""
    print_section("测试 1: 健康检查")
    try:
        response = requests.get(f"{BASE_URL}/admin/health", timeout=5)
        if response.status_code == 200:
            print_result("健康检查", True, response.json())
            return True
        else:
            print_result("健康检查", False, error=f"状态码: {response.status_code}")
            return False
    except Exception as e:
        print_result("健康检查", False, error=str(e))
        return False

def test_public_endpoints():
    """测试公共端点"""
    print_section("测试 2: 公共端点")
    
    endpoints = [
        ("日志", "/public/log"),
        ("统计", "/public/stats"),
        ("运行时间", "/public/uptime"),
    ]
    
    results = []
    for name, endpoint in endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                print_result(name, True, data)
                results.append(True)
            else:
                print_result(name, False, error=f"状态码: {response.status_code}")
                results.append(False)
        except Exception as e:
            print_result(name, False, error=str(e))
            results.append(False)
    
    return all(results)

def test_admin_login():
    """测试管理员登录"""
    print_section("测试 3: 管理员登录")
    try:
        response = requests.post(
            f"{BASE_URL}/admin/login",
            json={"admin_key": ADMIN_KEY},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            print_result("管理员登录", True, data)
            return data.get("success", False)
        else:
            print_result("管理员登录", False, error=f"状态码: {response.status_code}")
            return False
    except Exception as e:
        print_result("管理员登录", False, error=str(e))
        return False

def test_settings():
    """测试系统设置获取"""
    print_section("测试 4: 系统设置")
    try:
        response = requests.get(
            f"{BASE_URL}/admin/settings",
            headers={"X-Admin-Key": ADMIN_KEY},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            print_result("系统设置获取", True, data)
            
            print("\n  青果代理配置:")
            if "basic" in data:
                basic = data["basic"]
                print(f"    - 启用状态: {basic.get('qg_proxy_enabled', False)}")
                print(f"    - API密钥: {'已配置' if basic.get('qg_proxy_api_key') else '未配置'}")
                print(f"    - 代理类型: {basic.get('qg_proxy_type', 'N/A')}")
                print(f"    - 代理地区: {basic.get('qg_proxy_region', 'N/A')}")
                print(f"    - 代理协议: {basic.get('qg_proxy_protocol', 'N/A')}")
            
            return True
        else:
            print_result("系统设置获取", False, error=f"状态码: {response.status_code}")
            return False
    except Exception as e:
        print_result("系统设置获取", False, error=str(e))
        return False

def test_qg_proxy_direct():
    """直接测试青果代理客户端"""
    print_section("测试 5: 青果代理客户端")
    
    try:
        from core.qg_proxy_client import create_qg_proxy_client
        from core.config import config
        
        print(f"\n  配置信息:")
        print(f"    - 启用状态: {config.basic.qg_proxy_enabled}")
        print(f"    - API密钥: {config.basic.qg_proxy_api_key[:10]}..." if config.basic.qg_proxy_api_key else "    - API密钥: 未配置")
        print(f"    - 代理类型: {config.basic.qg_proxy_type}")
        print(f"    - 代理地区: {config.basic.qg_proxy_region}")
        print(f"    - 代理协议: {config.basic.qg_proxy_protocol}")
        
        if not config.basic.qg_proxy_enabled:
            print("\n  ⚠️ 青果代理未启用，跳过测试")
            return True
        
        print("\n  创建代理客户端...")
        client = create_qg_proxy_client(
            api_key=config.basic.qg_proxy_api_key,
            secret_id=config.basic.qg_proxy_secret_id,
            secret_key=config.basic.qg_proxy_secret_key,
            proxy_type=config.basic.qg_proxy_type,
            region=config.basic.qg_proxy_region,
            log_callback=lambda level, msg: print(f"    [{level.upper()}] {msg}"),
        )
        
        print("\n  尝试获取代理...")
        proxy_url = client.get_proxy_url()
        
        if proxy_url:
            print_result("代理获取", True, {"proxy_url": proxy_url[:50] + "..."})
            
            print("\n  测试代理健康状态...")
            is_healthy = client.check_proxy_health(proxy_url, timeout=10)
            if is_healthy:
                print_result("代理健康检查", True)
            else:
                print_result("代理健康检查", False, error="代理连接失败")
            
            return True
        else:
            print_result("代理获取", False, error="未能获取代理URL")
            return False
            
    except Exception as e:
        print_result("青果代理测试", False, error=str(e))
        import traceback
        traceback.print_exc()
        return False

def main():
    """主测试函数"""
    print("\n" + "=" * 60)
    print("  🚀 后端API测试")
    print("=" * 60)
    
    results = []
    
    results.append(("健康检查", test_health_check()))
    results.append(("公共端点", test_public_endpoints()))
    results.append(("管理员登录", test_admin_login()))
    results.append(("系统设置", test_settings()))
    results.append(("青果代理", test_qg_proxy_direct()))
    
    print_section("测试总结")
    
    for name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {name}")
    
    success_count = sum(1 for _, r in results if r)
    total_count = len(results)
    
    print(f"\n总计: {success_count}/{total_count} 通过")
    
    if success_count == total_count:
        print("\n🎉 所有测试通过！")
    else:
        print(f"\n⚠️ {total_count - success_count} 个测试失败")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
