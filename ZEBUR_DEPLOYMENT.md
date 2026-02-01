# Zeabur部署指南

## 项目概述

本项目是一个Gemini Business 2API服务，支持自动注册Gemini账号，集成了青果代理和DuckMail临时邮箱服务。

## 部署架构

- **后端服务**: Python FastAPI
- **前端服务**: Vue.js (需要构建)
- **浏览器自动化**: DrissionPage + Chromium
- **代理服务**: 青果网络代理
- **邮箱服务**: DuckMail临时邮箱

## 前置要求

1. **Zeabur账号**: 注册 [Zeabur](https://zeabur.com)
2. **GitHub账号**: 用于代码托管
3. **青果代理账号**: 注册 [青果网络](https://www.qg.net/)
4. **DuckMail账号**: 注册 [DuckMail](https://duckmail.sbs/)

## 部署步骤

### 1. 准备代码仓库

#### 1.1 创建GitHub仓库

1. 在GitHub创建新仓库
2. 将项目代码推送到GitHub

```bash
# 初始化Git仓库（如果还没有）
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

#### 1.2 创建Zeabur项目

1. 登录 [Zeabur控制台](https://dash.zeabur.com)
2. 点击"新建项目"
3. 选择"从Git仓库导入"
4. 授权GitHub并选择你的仓库
5. 等待Zeabur克隆代码

### 2. 配置后端服务

#### 2.1 创建后端服务

1. 在Zeabur项目中点击"新建服务"
2. 选择"Git仓库"
3. 选择你的仓库
4. Zeabur会自动检测到Python项目

#### 2.2 配置构建命令

在服务配置中设置：

**构建命令**:
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

**启动命令**:
```bash
# 启动虚拟显示
Xvfb :99 -screen 0 1280x800x24 -ac &
sleep 1
export DISPLAY=:99

# 启动应用
python main.py
```

#### 2.3 配置环境变量

在服务配置中添加以下环境变量：

**基础配置**:
```env
PORT=7860
TZ=Asia/Shanghai
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
```

**管理员配置**:
```env
ADMIN_KEY=your_admin_password_here
```

**青果代理配置**:
```env
QG_PROXY_ENABLED=true
QG_PROXY_API_KEY=BYJ3MCP5
QG_PROXY_SECRET_ID=
QG_PROXY_SECRET_KEY=7B3C288DCF56
QG_PROXY_TYPE=short_term
QG_PROXY_REGION=global
QG_PROXY_PROTOCOL=http
```

**DuckMail配置**:
```env
DUCKMAIL_API_KEY=dk_9172ab8f7dc0bc4b845d2f2a38e1246afc6d4b28427fb711e191cd4c2ff309a1
DUCKMAIL_BASE_URL=https://api.duckmail.sbs
TEMP_MAIL_PROVIDER=duckmail
```

**浏览器配置**:
```env
BROWSER_ENGINE=dp
BROWSER_HEADLESS=false
```

**注册配置**:
```env
REGISTER_DEFAULT_COUNT=1
REGISTER_DOMAIN=
```

#### 2.4 配置端口

- **内部端口**: 7860
- **公开端口**: 80 (自动分配HTTPS端口)

#### 2.5 配置持久化存储

1. 在服务配置中点击"存储"
2. 创建新存储卷，命名为`data`
3. 挂载路径: `/app/data`

#### 2.6 配置健康检查

```yaml
类型: HTTP
路径: /admin/health
端口: 7860
间隔: 30s
超时: 10s
重试次数: 3
```

### 3. 配置前端服务（可选）

如果需要使用管理面板，需要单独部署前端服务。

#### 3.1 创建前端服务

1. 在Zeabur项目中点击"新建服务"
2. 选择"Git仓库"
3. 选择你的仓库（同一个仓库）
4. 设置工作目录为`frontend`

#### 3.2 配置构建命令

```bash
npm install
npm run build
```

#### 3.3 配置启动命令

```bash
# 使用nginx提供静态文件
npm run preview
```

或者使用nginx配置：

**Dockerfile**:
```dockerfile
FROM nginx:alpine
COPY dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

**nginx.conf**:
```nginx
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api/ {
        proxy_pass http://gemini-api:7860/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 3.4 配置环境变量

```env
VITE_API_BASE_URL=https://your-backend-url.zeabur.app
```

### 4. 配置域名（可选）

#### 4.1 绑定自定义域名

1. 在服务配置中点击"域名"
2. 添加自定义域名
3. 按照提示配置DNS记录

#### 4.2 配置SSL证书

Zeabur会自动为你的域名配置SSL证书（Let's Encrypt）。

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

## 监控和日志

### 查看日志

1. 在Zeabur控制台选择服务
2. 点击"日志"标签
3. 实时查看应用日志

### 监控指标

1. 在服务配置中查看资源使用情况
2. 监控CPU、内存、磁盘使用
3. 查看网络流量

## 常见问题

### 1. 构建失败

**问题**: 构建过程中出现依赖安装错误

**解决方案**:
- 检查requirements.txt是否完整
- 确保Python版本兼容（Python 3.11+）
- 增加构建超时时间

### 2. 浏览器启动失败

**问题**: Chromium无法启动

**解决方案**:
- 确保安装了所有浏览器依赖
- 检查DISPLAY环境变量
- 使用有头模式进行调试

### 3. 代理连接失败

**问题**: 青果代理连接失败

**解决方案**:
- 检查API Key和AuthPwd是否正确
- 确认账户余额充足
- 检查代理地区是否支持

### 4. 邮箱服务失败

**问题**: DuckMail邮箱注册失败

**解决方案**:
- 检查API Key是否正确
- 确认API地址正确
- 查看DuckMail服务状态

### 5. 端口冲突

**问题**: 服务无法启动，提示端口被占用

**解决方案**:
- 修改PORT环境变量
- 确保只有一个服务使用7860端口

### 6. 数据持久化问题

**问题**: 重启后数据丢失

**解决方案**:
- 确保配置了持久化存储
- 检查挂载路径是否正确（/app/data）

## 性能优化

### 1. 资源配置

根据使用情况调整服务配置：

**最低配置**:
- CPU: 0.5核
- 内存: 512MB
- 存储: 1GB

**推荐配置**:
- CPU: 1核
- 内存: 1GB
- 存储: 5GB

**高性能配置**:
- CPU: 2核+
- 内存: 2GB+
- 存储: 10GB+

### 2. 自动扩缩容

1. 在服务配置中启用自动扩缩容
2. 设置最小和最大实例数
3. 配置CPU和内存阈值

### 3. 缓存优化

- 启用Redis缓存（可选）
- 配置CDN加速静态资源
- 优化数据库查询

## 安全建议

1. **修改默认密码**: 修改ADMIN_KEY为强密码
2. **启用HTTPS**: 使用Zeabur自动SSL证书
3. **限制访问**: 配置IP白名单（可选）
4. **定期备份**: 定期备份数据目录
5. **监控日志**: 定期检查异常日志

## 更新部署

### 自动更新

1. 推送代码到GitHub
2. Zeabur自动检测更新
3. 自动重新部署

### 手动更新

1. 在Zeabur控制台选择服务
2. 点击"重新部署"
3. 等待部署完成

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

## 技术支持

- **Zeabur文档**: https://zeabur.com/docs
- **青果网络文档**: https://www.qg.net/help
- **DuckMail文档**: https://duckmail.sbs/docs
- **项目Issues**: https://github.com/your-username/gemini-business2api/issues

## 附录

### A. 环境变量完整列表

详见 [.env.example](.env.example) 文件。

### B. Docker部署

如果需要使用Docker部署，请参考 [docker-compose.yml](docker-compose.yml)。

### C. 本地开发

详见项目README文件。

---

*部署指南最后更新: 2026-02-02*
