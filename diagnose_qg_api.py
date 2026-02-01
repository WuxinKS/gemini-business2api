"""
青果代理API诊断脚本

用于诊断青果代理API调用问题
"""

import requests
import json

API_KEY = "A7F2B120"

def test_api_direct():
    """直接测试青果代理API"""
    print("=" * 60)
    print("青果代理API诊断")
    print("=" * 60)
    
    print(f"\nAPI密钥: {API_KEY}")
    print(f"API端点: https://overseas.proxy.qg.net/get")
    
    test_cases = [
        {
            "name": "基础测试（仅key）",
            "params": {"key": API_KEY}
        },
        {
            "name": "指定地区（global）",
            "params": {"key": API_KEY, "area": "global"}
        },
        {
            "name": "指定地区（us）",
            "params": {"key": API_KEY, "area": "us"}
        },
        {
            "name": "指定数量",
            "params": {"key": API_KEY, "num": "1"}
        },
        {
            "name": "完整参数",
            "params": {
                "key": API_KEY,
                "num": "1",
                "area": "global",
                "format": "txt",
                "seq": "\r\n",
                "distinct": "false"
            }
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'=' * 60}")
        print(f"测试 {i}: {test_case['name']}")
        print(f"{'=' * 60}")
        print(f"参数: {json.dumps(test_case['params'], ensure_ascii=False)}")
        
        try:
            response = requests.get(
                "https://overseas.proxy.qg.net/get",
                params=test_case['params'],
                timeout=10
            )
            
            print(f"\n状态码: {response.status_code}")
            print(f"响应头: {dict(response.headers)}")
            
            try:
                data = response.json()
                print(f"\n响应数据:")
                print(json.dumps(data, ensure_ascii=False, indent=2))
                
                if data.get("code") == "SUCCESS":
                    print("\n✅ 成功！")
                    if data.get("data"):
                        print(f"获取到 {len(data['data'])} 个代理")
                        if len(data['data']) > 0:
                            proxy = data['data'][0]
                            print(f"代理信息: {json.dumps(proxy, ensure_ascii=False, indent=2)}")
                else:
                    print(f"\n❌ 失败: {data.get('message', '未知错误')}")
                    print(f"错误代码: {data.get('code')}")
                    print(f"请求ID: {data.get('request_id')}")
                    
                    if data.get("code") == "FAILED_OPERATION":
                        print("\n可能的原因:")
                        print("  1. API密钥无效或已过期")
                        print("  2. 账户余额不足")
                        print("  3. 产品类型不匹配")
                        print("  4. IP未添加到白名单")
                        print("  5. 超出请求频率限制")
                        
            except json.JSONDecodeError:
                print(f"\n响应文本:")
                print(response.text[:500])
                
        except requests.exceptions.Timeout:
            print("\n❌ 请求超时")
        except requests.exceptions.RequestException as e:
            print(f"\n❌ 请求异常: {e}")
        except Exception as e:
            print(f"\n❌ 未知错误: {e}")
    
    print(f"\n{'=' * 60}")
    print("诊断完成")
    print(f"{'=' * 60}")
    print("\n建议:")
    print("1. 登录青果网络后台验证API密钥: https://www.qg.net/")
    print("2. 检查账户余额是否充足")
    print("3. 确认产品类型是否支持短效代理")
    print("4. 将服务器IP添加到白名单（如需要）")
    print("5. 查看API文档: https://www.qg.net/tools/IPget.html")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    test_api_direct()
