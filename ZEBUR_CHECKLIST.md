# Zeabur部署快速检查清单

## 准备阶段

- [ ] 注册Zeabur账号
- [ ] 注册GitHub账号
- [ ] 注册青果网络账号
- [ ] 注册DuckMail账号
- [ ] 获取青果代理API Key和AuthPwd
- [ ] 获取DuckMail API Key

## 代码准备

- [ ] 初始化Git仓库
- [ ] 创建GitHub仓库
- [ ] 推送代码到GitHub
- [ ] 确认.env.example文件存在
- [ ] 确认Dockerfile文件存在
- [ ] 确认requirements.txt文件存在

## Zeabur配置

- [ ] 在Zeabur创建新项目
- [ ] 从GitHub导入仓库
- [ ] 创建后端服务
- [ ] 配置构建命令
- [ ] 配置启动命令
- [ ] 配置环境变量
- [ ] 配置端口（7860）
- [ ] 配置持久化存储（/app/data）
- [ ] 配置健康检查（/admin/health）

## 环境变量配置

### 基础配置
- [ ] PORT=7860
- [ ] TZ=Asia/Shanghai
- [ ] PYTHONDONTWRITEBYTECODE=1
- [ ] PYTHONUNBUFFERED=1

### 管理员配置
- [ ] ADMIN_KEY=your_admin_password

### 青果代理配置
- [ ] QG_PROXY_ENABLED=true
- [ ] QG_PROXY_API_KEY=your_qg_api_key
- [ ] QG_PROXY_SECRET_KEY=your_qg_auth_pwd
- [ ] QG_PROXY_TYPE=short_term
- [ ] QG_PROXY_REGION=global
- [ ] QG_PROXY_PROTOCOL=http

### DuckMail配置
- [ ] DUCKMAIL_API_KEY=your_duckmail_api_key
- [ ] DUCKMAIL_BASE_URL=https://api.duckmail.sbs
- [ ] TEMP_MAIL_PROVIDER=duckmail

### 浏览器配置
- [ ] BROWSER_ENGINE=dp
- [ ] BROWSER_HEADLESS=false

### 注册配置
- [ ] REGISTER_DEFAULT_COUNT=1
- [ ] REGISTER_DOMAIN= (可选）

## 部署验证

- [ ] 服务成功启动
- [ ] 健康检查通过
- [ ] 可以访问API端点
- [ ] 青果代理工作正常
- [ ] DuckMail邮箱服务正常
- [ ] 数据持久化正常

## 测试验证

- [ ] 测试健康检查接口
- [ ] 测试青果代理获取
- [ ] 测试DuckMail邮箱注册
- [ ] 测试注册流程（需要图形界面）

## 生产环境配置

- [ ] 修改默认管理员密码
- [ ] 配置自定义域名
- [ ] 启用HTTPS（Zeabur自动配置）
- [ ] 配置日志监控
- [ ] 配置告警通知
- [ ] 设置自动备份

## 安全检查

- [ ] 修改ADMIN_KEY为强密码
- [ ] 检查API密钥是否泄露
- [ ] 配置访问限制（可选）
- [ ] 启用防火墙规则（可选）

## 性能优化

- [ ] 调整资源配置（CPU/内存）
- [ ] 配置自动扩缩容
- [ ] 启用CDN加速（可选）
- [ ] 优化数据库查询（可选）

## 文档和监控

- [ ] 保存部署文档
- [ ] 配置日志收集
- [ ] 设置监控指标
- [ ] 配置告警规则

## 常见问题排查

### 构建失败
- [ ] 检查requirements.txt是否完整
- [ ] 检查Python版本兼容性
- [ ] 查看构建日志

### 服务启动失败
- [ ] 检查端口配置
- [ ] 检查环境变量
- [ ] 查看服务日志

### 代理连接失败
- [ ] 检查青果代理API Key
- [ ] 检查青果代理AuthPwd
- [ ] 检查账户余额

### 邮箱服务失败
- [ ] 检查DuckMail API Key
- [ ] 检查API地址
- [ ] 查看DuckMail服务状态

## 部署后维护

- [ ] 定期检查服务状态
- [ ] 监控资源使用情况
- [ ] 定期备份数据
- [ ] 更新依赖包
- [ ] 更新应用版本

## 联系方式

- **Zeabur支持**: https://zeabur.com/support
- **青果网络支持**: https://www.qg.net/support
- **DuckMail支持**: https://duckmail.sbs/support
- **项目Issues**: https://github.com/your-username/gemini-business2api/issues

---

*检查清单最后更新: 2026-02-02*
