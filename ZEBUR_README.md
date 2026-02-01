# Zeabur部署文档

本目录包含部署到Zeabur所需的所有文档和脚本。

## 文件说明

### 1. [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md)
完整的Zeabur部署指南，包含：
- 项目概述
- 部署架构
- 前置要求
- 详细部署步骤
- 配置说明
- 监控和日志
- 常见问题
- 性能优化
- 安全建议

### 2. [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md)
部署检查清单，包含：
- 准备阶段检查
- 代码准备检查
- Zeabur配置检查
- 环境变量配置检查
- 部署验证检查
- 生产环境配置检查
- 安全检查
- 性能优化检查
- 常见问题排查

### 3. [zeabur.yml](zeabur.yml)
Zeabur配置文件示例，包含：
- 后端服务配置
- 构建命令
- 启动命令
- 环境变量
- 端口配置
- 健康检查

### 4. [deploy-zeabur.sh](deploy-zeabur.sh)
Linux/Mac快速部署脚本，功能：
- 检查必要工具
- 初始化Git仓库
- 添加和提交文件
- 推送到GitHub
- 显示部署说明

### 5. [deploy-zeabur.bat](deploy-zeabur.bat)
Windows快速部署脚本，功能：
- 检查必要工具
- 初始化Git仓库
- 添加和提交文件
- 推送到GitHub
- 显示部署说明

## 快速开始

### 方式1: 使用快速部署脚本

**Windows用户**:
```cmd
deploy-zeabur.bat
```

**Linux/Mac用户**:
```bash
chmod +x deploy-zeabur.sh
./deploy-zeabur.sh
```

### 方式2: 手动部署

1. **准备代码仓库**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/your-username/gemini-business2api.git
   git push -u origin main
   ```

2. **在Zeabur创建项目**
   - 访问 https://dash.zeabur.com
   - 新建项目
   - 从Git仓库导入

3. **配置服务**
   - 参考 [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md) 进行详细配置

## 部署步骤概览

### 1. 准备阶段
- 注册Zeabur账号
- 注册GitHub账号
- 注册青果网络账号
- 注册DuckMail账号
- 获取API密钥

### 2. 代码准备
- 创建GitHub仓库
- 推送代码到GitHub
- 确认配置文件完整

### 3. Zeabur配置
- 创建Zeabur项目
- 导入Git仓库
- 配置构建和启动命令
- 配置环境变量
- 配置端口和存储

### 4. 部署验证
- 检查服务状态
- 测试API端点
- 验证功能正常

## 环境变量配置

### 必需配置

```env
# 管理员密码
ADMIN_KEY=your_admin_password

# 青果代理
QG_PROXY_ENABLED=true
QG_PROXY_API_KEY=BYJ3MCP5
QG_PROXY_SECRET_KEY=7B3C288DCF56

# DuckMail
DUCKMAIL_API_KEY=dk_9172ab8f7dc0bc4b845d2f2a38e1246afc6d4b28427fb711e191cd4c2ff309a1
TEMP_MAIL_PROVIDER=duckmail
```

### 可选配置

```env
# 浏览器
BROWSER_ENGINE=dp
BROWSER_HEADLESS=false

# 注册
REGISTER_DEFAULT_COUNT=1
REGISTER_DOMAIN=
```

## 构建命令

```bash
# 安装Python依赖
pip install --no-cache-dir -r requirements.txt

# 安装浏览器依赖
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

## 启动命令

```bash
# 启动虚拟显示
Xvfb :99 -screen 0 1280x800x24 -ac &
sleep 1
export DISPLAY=:99

# 启动应用
python main.py
```

## 健康检查

- **路径**: `/admin/health`
- **端口**: 7860
- **间隔**: 30秒
- **超时**: 10秒
- **重试**: 3次

## 持久化存储

- **挂载路径**: `/app/data`
- **存储名称**: `data`
- **用途**: 保存账户配置和数据库

## 常见问题

### Q: 构建失败怎么办？
A: 检查requirements.txt是否完整，确保Python版本兼容（3.11+），查看构建日志。

### Q: 浏览器启动失败怎么办？
A: 确保安装了所有浏览器依赖，检查DISPLAY环境变量，使用有头模式进行调试。

### Q: 代理连接失败怎么办？
A: 检查API Key和AuthPwd是否正确，确认账户余额充足，检查代理地区是否支持。

### Q: 邮箱服务失败怎么办？
A: 检查API Key是否正确，确认API地址正确，查看DuckMail服务状态。

## 技术支持

- **Zeabur文档**: https://zeabur.com/docs
- **Zeabur支持**: https://zeabur.com/support
- **青果网络文档**: https://www.qg.net/help
- **DuckMail文档**: https://duckmail.sbs/docs

## 相关文档

- [项目README](../README.md)
- [Docker部署](../docker-compose.yml)
- [环境变量示例](../.env.example)

## 更新日志

- 2026-02-02: 初始版本，添加完整的Zeabur部署文档

---

*文档最后更新: 2026-02-02*
