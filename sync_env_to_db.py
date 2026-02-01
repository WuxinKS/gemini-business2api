"""
将 .env 文件中的青果代理配置同步到数据库

使用方法：
python sync_env_to_db.py
"""

import os
from dotenv import load_dotenv
from core import storage
from core.config import config_manager

load_dotenv()

def sync_qg_proxy_config():
    """同步青果代理配置到数据库"""
    print("=" * 60)
    print("同步配置到数据库")
    print("=" * 60)
    
    # 从环境变量读取青果代理配置
    qg_proxy_enabled = os.getenv("QG_PROXY_ENABLED", "false").lower() in ("true", "1", "yes")
    qg_proxy_api_key = os.getenv("QG_PROXY_API_KEY", "")
    qg_proxy_secret_id = os.getenv("QG_PROXY_SECRET_ID", "")
    qg_proxy_secret_key = os.getenv("QG_PROXY_SECRET_KEY", "")
    qg_proxy_type = os.getenv("QG_PROXY_TYPE", "short_term")
    qg_proxy_region = os.getenv("QG_PROXY_REGION", "global")
    qg_proxy_protocol = os.getenv("QG_PROXY_PROTOCOL", "http")
    
    # 从环境变量读取DuckMail配置
    duckmail_api_key = os.getenv("DUCKMAIL_API_KEY", "")
    
    print(f"\n从 .env 读取的配置:")
    print(f"  - 启用状态: {qg_proxy_enabled}")
    print(f"  - API密钥: {qg_proxy_api_key[:10]}..." if qg_proxy_api_key else "  - API密钥: 未配置")
    print(f"  - 密钥ID: {qg_proxy_secret_id[:10]}..." if qg_proxy_secret_id else "  - 密钥ID: 未配置")
    print(f"  - 密钥Key: {qg_proxy_secret_key[:10]}..." if qg_proxy_secret_key else "  - 密钥Key: 未配置")
    print(f"  - 代理类型: {qg_proxy_type}")
    print(f"  - 代理地区: {qg_proxy_region}")
    print(f"  - 代理协议: {qg_proxy_protocol}")
    print(f"  - DuckMail API Key: {duckmail_api_key[:10]}..." if duckmail_api_key else "  - DuckMail API Key: 未配置")
    
    # 从数据库加载当前配置
    current_settings = storage.load_settings_sync()
    
    if not current_settings:
        current_settings = {}
    
    if "basic" not in current_settings:
        current_settings["basic"] = {}
    
    # 更新青果代理配置
    current_settings["basic"]["qg_proxy_enabled"] = qg_proxy_enabled
    current_settings["basic"]["qg_proxy_api_key"] = qg_proxy_api_key
    current_settings["basic"]["qg_proxy_secret_id"] = qg_proxy_secret_id
    current_settings["basic"]["qg_proxy_secret_key"] = qg_proxy_secret_key
    current_settings["basic"]["qg_proxy_type"] = qg_proxy_type
    current_settings["basic"]["qg_proxy_region"] = qg_proxy_region
    current_settings["basic"]["qg_proxy_protocol"] = qg_proxy_protocol
    
    # 更新DuckMail配置
    current_settings["basic"]["duckmail_api_key"] = duckmail_api_key
    
    # 保存到数据库
    print(f"\n保存配置到数据库...")
    saved = storage.save_settings_sync(current_settings)
    
    if saved:
        print("✅ 配置保存成功")
        
        # 重新加载配置
        print("\n重新加载配置...")
        config_manager.reload()
        
        print(f"\n验证配置:")
        print(f"  - 启用状态: {config_manager.config.basic.qg_proxy_enabled}")
        print(f"  - API密钥: {'已配置' if config_manager.config.basic.qg_proxy_api_key else '未配置'}")
        print(f"  - 代理类型: {config_manager.config.basic.qg_proxy_type}")
        print(f"  - 代理地区: {config_manager.config.basic.qg_proxy_region}")
        print(f"  - 代理协议: {config_manager.config.basic.qg_proxy_protocol}")
        print(f"  - DuckMail API Key: {'已配置' if config_manager.config.basic.duckmail_api_key else '未配置'}")
        
        print("\n" + "=" * 60)
        print("✅ 配置同步完成！请重启服务使配置生效")
        print("=" * 60)
    else:
        print("❌ 配置保存失败")

if __name__ == "__main__":
    sync_qg_proxy_config()
