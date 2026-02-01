"""
青果代理集成测试脚本

测试功能：
1. 配置加载测试
2. 代理客户端创建测试
3. 代理获取测试
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.config import config
from core.qg_proxy_client import create_qg_proxy_client


def test_config_loading():
    """测试配置加载"""
    print("=" * 60)
    print("测试 1: 配置加载")
    print("=" * 60)

    print(f"✅ 青果代理启用状态: {config.basic.qg_proxy_enabled}")
    print(f"✅ API密钥: {'已配置' if config.basic.qg_proxy_api_key else '未配置'}")
    print(f"✅ 代理类型: {config.basic.qg_proxy_type}")
    print(f"✅ 代理地区: {config.basic.qg_proxy_region}")
    print(f"✅ 代理协议: {config.basic.qg_proxy_protocol}")
    print()

    return True


def test_proxy_client_creation():
    """测试代理客户端创建"""
    print("=" * 60)
    print("测试 2: 代理客户端创建")
    print("=" * 60)

    try:
        client = create_qg_proxy_client(
            api_key=config.basic.qg_proxy_api_key,
            secret_id=config.basic.qg_proxy_secret_id,
            secret_key=config.basic.qg_proxy_secret_key,
            proxy_type=config.basic.qg_proxy_type,
            region=config.basic.qg_proxy_region,
            log_callback=lambda level, msg: print(f"[{level.upper()}] {msg}"),
        )

        print("✅ 代理客户端创建成功")
        print()

        return client
    except Exception as e:
        print(f"❌ 代理客户端创建失败: {e}")
        print()
        return None


def test_proxy_fetch(client):
    """测试代理获取"""
    print("=" * 60)
    print("测试 3: 代理获取")
    print("=" * 60)

    if not client:
        print("⚠️ 跳过测试：代理客户端未创建")
        print()
        return False

    try:
        proxy_url = client.get_proxy_url()

        if proxy_url:
            print(f"✅ 代理获取成功: {proxy_url[:50]}...")
            print()

            proxy_dict = client.get_proxy_dict()
            print(f"✅ 代理字典格式: {proxy_dict}")
            print()

            return True
        else:
            print("⚠️ 代理获取失败（可能API Key未配置）")
            print()
            return False
    except Exception as e:
        print(f"❌ 代理获取失败: {e}")
        print()
        return False


def main():
    """主测试函数"""
    print()
    print("🚀 青果代理集成测试")
    print()

    try:
        test_config_loading()
        client = test_proxy_client_creation()
        test_proxy_fetch(client)

        print("=" * 60)
        print("✅ 所有测试完成")
        print("=" * 60)
        print()

    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
