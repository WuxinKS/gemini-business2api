# Zeabur部署总结

## 已创建的文件

### 1. 部署文档
- **[ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md)** - 完整的Zeabur部署指南
- **[ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md)** - 部署检查清单
- **[ZEBUR_README.md](ZEBUR_README.md)** - Zeabur部署文档总览

### 2. 配置文件
- **[zeabur.yml](zeabur.yml)** - Zeabur配置文件示例

### 3. 部署脚本
- **[deploy-zeabur.sh](deploy-zeabur.sh)** - Linux/Mac快速部署脚本
- **[deploy-zeabur.bat](deploy-zeabur.bat)** - Windows快速部署脚本

## 快速部署步骤

### 步骤1: 准备代码仓库

**使用快速部署脚本**:

Windows:
```cmd
deploy-zeabur.bat
```

Linux/Mac:
```bash
chmod +x deploy-zeabur.sh
./deploy-zeabur.sh
```

**手动操作**:
```bash
# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit"

# 添加远程仓库
git remote add origin https://github.com/your-username/gemini-business2api.git

# 推送到GitHub
git push -u origin main
```

### 步骤2: 在Zeabur创建项目

1. 访问 [Zeabur控制台](https://dash.zeabur.com)
2. 点击"新建项目"
3. 选择"从Git仓库导入"
4. 授权GitHub并选择你的仓库
5. 等待Zeabur克隆代码

### 步骤3: 配置后端服务

#### 3.1 创建服务
- 在Zeabur项目中点击"新建服务"
- 选择"Git仓库"
- 选择你的仓库

#### 3.2 配置构建命令
```bash
pip install --no-cache-dir -r requirements.txt

apt-get update && \
apt-get install -y --no-install-recommends \
  curl \
  chromium chromium-driver \
  dbus dbus-x11 \
  xvfb xauth \
  libglib2.0-0 libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
  libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 \
  libxfixes3 libxrandr2 libgbm1 libasound2 libpango-1.0-0 \
  libcairo2 fonts-liberation fonts-noto-cjk && \
rm -rf /var/lib/apt/lists/*
```

#### 3.3 配置启动命令
```bash
Xvfb :99 -screen 0 1280x800x24 -ac &
sleep 1
export DISPLAY=:99
python main.py
```

#### 3.4 配置环境变量

**必需配置**:
```env
ADMIN_KEY=your_admin_password
QG_PROXY_ENABLED=true
QG_PROXY_API_KEY=BYJ3MCP5
QG_PROXY_SECRET_KEY=7B3C288DCF56
DUCKMAIL_API_KEY=dk_9172ab8f7dc0bc4b845d2f2a38e1246afc6d4b28427fb711e191cd4c2ff309a1
TEMP_MAIL_PROVIDER=duckmail
```

**可选配置**:
```env
BROWSER_ENGINE=dp
BROWSER_HEADLESS=false
REGISTER_DEFAULT_COUNT=1
```

#### 3.5 配置端口
- **内部端口**: 7860
- **公开端口**: 80 (自动分配HTTPS端口)

#### 3.6 配置持久化存储
- **存储名称**: data
- **挂载路径**: /app/data

#### 3.7 配置健康检查
- **类型**: HTTP
- **路径**: /admin/health
- **端口**: 7860
- **间隔**: 30秒
- **超时**: 10秒
- **重试**: 3次

### 步骤4: 验证部署

1. 检查服务状态是否为"运行中"
2. 访问健康检查端点: `https://your-service.zeabur.app/admin/health`
3. 查看服务日志确认无错误
4. 测试API端点是否正常

## 配置说明

### 青果代理配置

**获取认证信息**:
1. 登录 [青果网络](https://www.qg.net/)
2. 进入"API管理"
3. 获取API Key和AuthPwd

**配置参数**:
- `QG_PROXY_ENABLED`: 是否启用青果代理（true/false）
- `QG_PROXY_API_KEY`: 青果代理API Key
- `QG_PROXY_SECRET_KEY`: 青果代理AuthPwd
- `QG_PROXY_TYPE`: 代理类型（short_term/unlimited_pool/traffic_pool/data_center_pool）
- `QG_PROXY_REGION`: 代理地区（global/us/eu/asia/cn等）

### DuckMail配置

**获取API Key**:
1. 登录 [DuckMail](https://duckmail.sbs/)
2. 进入"API管理"
3. 获取API Key

**配置参数**:
- `DUCKMAIL_API_KEY`: DuckMail API Key
- `DUCKMAIL_BASE_URL`: DuckMail API地址（默认: https://api.duckmail.sbs）
- `TEMP_MAIL_PROVIDER`: 邮箱提供商（duckmail/moemail/freemail/gptmail）

### 浏览器配置

**配置参数**:
- `BROWSER_ENGINE`: 浏览器引擎（dp=DrissionPage, uc=undetected-chromedriver）
- `BROWSER_HEADLESS`: 无头模式（true/false）

**建议**:
- 注册流程建议使用有头模式（BROWSER_HEADLESS=false）
- 生产环境可以使用无头模式（BROWSER_HEADLESS=true）

## 监控和维护

### 查看日志
1. 在Zeabur控制台选择服务
2. 点击"日志"标签
3. 实时查看应用日志

### 监控指标
1. 在服务配置中查看资源使用情况
2. 监控CPU、内存、磁盘使用
3. 查看网络流量

### 定期维护
- 定期检查服务状态
- 监控资源使用情况
- 定期备份数据
- 更新依赖包
- 更新应用版本

## 常见问题

### Q1: 构建失败
**A**: 检查requirements.txt是否完整，确保Python版本兼容（3.11+），查看构建日志。

### Q2: 浏览器启动失败
**A**: 确保安装了所有浏览器依赖，检查DISPLAY环境变量，使用有头模式进行调试。

### Q3: 代理连接失败
**A**: 检查API Key和AuthPwd是否正确，确认账户余额充足，检查代理地区是否支持。

### Q4: 邮箱服务失败
**A**: 检查API Key是否正确，确认API地址正确，查看DuckMail服务状态。

### Q5: 端口冲突
**A**: 修改PORT环境变量，确保只有一个服务使用7860端口。

### Q6: 数据持久化问题
**A**: 确保配置了持久化存储，检查挂载路径是否正确（/app/data）。

## 成本估算

### Zeabur费用
- **最低配置**: 约$5/月
- **推荐配置**: 约$10/月
- **高性能配置**: 约$20+/月

### 青果代理费用
- **短效代理**: 按次计费，约¥0.01/次
- **不限流量池**: 按通道数计费，约¥100/通道/月

### DuckMail费用
- **免费套餐**: 每日限额
- **付费套餐**: 约$5/月起

## 安全建议

1. **修改默认密码**: 修改ADMIN_KEY为强密码
2. **启用HTTPS**: 使用Zeabur自动SSL证书
3. **限制访问**: 配置IP白名单（可选）
4. **定期备份**: 定期备份数据目录
5. **监控日志**: 定期检查异常日志

## 技术支持

- **Zeabur文档**: https://zeabur.com/docs
- **Zeabur支持**: https://zeabur.com/support
- **青果网络文档**: https://www.qg.net/help
- **DuckMail文档**: https://duckmail.sbs/docs

## 相关文档

- [完整部署指南](ZEBUR_DEPLOYMENT.md)
- [部署检查清单](ZEBUR_CHECKLIST.md)
- [Zeabur配置文件](zeabur.yml)
- [项目README](../README.md)
- [Docker部署](../docker-compose.yml)

## 下一步

1. ✅ 阅读完整部署指南: [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md)
2. ✅ 使用部署检查清单: [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md)
3. ✅ 运行快速部署脚本: `deploy-zeabur.bat` (Windows) 或 `./deploy-zeabur.sh` (Linux/Mac)
4. ✅ 在Zeabur创建项目并配置服务
5. ✅ 验证部署成功并测试功能

---

*部署总结最后更新: 2026-02-02*
