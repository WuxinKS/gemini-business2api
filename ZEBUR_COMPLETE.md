# Zeabur部署完整流程

## 🎯 部署概览

由于系统环境限制，需要手动完成部署。以下是完整的部署流程。

## 📋 部署清单

### 阶段1: 准备工作

- [ ] 安装Git
- [ ] 创建GitHub账号
- [ ] 创建Zeabur账号
- [ ] 获取青果代理API Key和AuthPwd
- [ ] 获取DuckMail API Key

### 阶段2: 代码准备

- [ ] 在GitHub创建新仓库
- [ ] 初始化本地Git仓库
- [ ] 添加所有文件到Git
- [ ] 提交代码
- [ ] 推送到GitHub

### 阶段3: Zeabur配置

- [ ] 在Zeabur创建新项目
- [ ] 创建新服务（预构建镜像）
- [ ] 配置环境变量
- [ ] 配置存储卷
- [ ] 配置端口
- [ ] 配置健康检查
- [ ] 部署服务

### 阶段4: 验证部署

- [ ] 检查服务状态
- [ ] 访问健康检查端点
- [ ] 查看服务日志
- [ ] 测试API功能

## 📖 详细步骤

### 步骤1: 安装Git

**Windows用户**:
1. 访问 https://git-scm.com/downloads
2. 下载Windows版本的Git
3. 运行安装程序，使用默认设置
4. 安装完成后，重新打开命令行窗口

**验证安装**:
```cmd
git --version
```

### 步骤2: 创建GitHub仓库

1. 访问 https://github.com/new
2. 输入仓库名称: `gemini-business2api`
3. 选择"Public"或"Private"
4. 点击"Create repository"

### 步骤3: 初始化Git仓库

在项目目录中打开命令行，执行：

```cmd
cd C:\Users\Admin\Downloads\gemini-business2api-main\gemini-business2api-main
git init
git add .
git commit -m "Initial commit"
```

### 步骤4: 连接GitHub仓库

```cmd
git remote add origin https://github.com/your-username/gemini-business2api.git
git branch -M main
git push -u origin main
```

**注意**: 将 `your-username` 替换为你的GitHub用户名

### 步骤5: 在Zeabur创建项目

1. 访问 https://dash.zeabur.com
2. 登录或注册账号
3. 点击"新建项目"
4. 输入项目名称: `gemini-business2api`
5. 点击"创建"

### 步骤6: 创建服务

1. 在项目中点击"新建服务"
2. 选择"预构建镜像"
3. 输入镜像名称: `cooooookk/gemini-business2api:latest`
4. 点击"部署"

### 步骤7: 配置环境变量

在服务配置中，点击"环境变量"，添加以下变量：

```env
ADMIN_KEY=admin123456
QG_PROXY_ENABLED=true
QG_PROXY_API_KEY=BYJ3MCP5
QG_PROXY_SECRET_KEY=7B3C288DCF56
QG_PROXY_TYPE=short_term
QG_PROXY_REGION=global
QG_PROXY_PROTOCOL=http
DUCKMAIL_API_KEY=dk_9172ab8f7dc0bc4b845d2f2a38e1246afc6d4b28427fb711e191cd4c2ff309a1
DUCKMAIL_BASE_URL=https://api.duckmail.sbs
TEMP_MAIL_PROVIDER=duckmail
BROWSER_ENGINE=dp
BROWSER_HEADLESS=false
PORT=7860
TZ=Asia/Shanghai
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
```

### 步骤8: 配置存储

1. 在服务配置中点击"存储"
2. 点击"创建存储卷"
3. 输入名称: `data`
4. 点击"创建"
5. 点击"挂载"
6. 挂载路径: `/app/data`
7. 选择存储卷: `data`
8. 点击"确认"

### 步骤9: 配置端口

1. 在服务配置中点击"端口"
2. 添加端口映射:
   - 内部端口: `7860`
   - 公开端口: 自动分配
3. 点击"保存"

### 步骤10: 配置健康检查

1. 在服务配置中点击"健康检查"
2. 配置:
   - 类型: HTTP
   - 路径: `/admin/health`
   - 端口: `7860`
   - 间隔: `30s`
   - 超时: `10s`
   - 重试: `3`
3. 点击"保存"

### 步骤11: 部署服务

1. 点击"部署"按钮
2. 等待部署完成（通常需要1-3分钟）
3. 查看部署日志确认无错误

## ✅ 验证部署

### 检查服务状态

1. 在Zeabur控制台查看服务状态
2. 状态应该显示为"运行中"

### 访问健康检查端点

Zeabur会提供一个访问URL，例如：
```
https://your-service.zeabur.app
```

访问健康检查端点验证服务是否正常：
```
https://your-service.zeabur.app/admin/health
```

应该返回：
```json
{"status": "ok"}
```

### 查看日志

1. 在服务配置中点击"日志"
2. 查看应用日志
3. 确认没有错误信息

## 🔧 修改配置

如果需要修改配置：

1. 在Zeabur控制台选择服务
2. 点击"环境变量"
3. 修改需要更改的变量
4. 点击"保存"
5. 点击"重启"按钮

## 📊 监控服务

### 查看资源使用

1. 在服务配置中点击"监控"
2. 查看CPU、内存、磁盘使用情况
3. 查看网络流量

### 查看日志

1. 在服务配置中点击"日志"
2. 实时查看应用日志
3. 搜索特定关键词

## 📝 部署文档

以下是已创建的部署文档：

1. **[ZEBUR.md](ZEBUR.md)** - 部署文档总览
2. **[ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md)** - 一键部署指南
3. **[ZEBUR_QUICK.md](ZEBUR_QUICK.md)** - 快速部署指南
4. **[ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md)** - 完整部署指南
5. **[ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md)** - 部署检查清单
6. **[ZEBUR_MANUAL.md](ZEBUR_MANUAL.md)** - 手动部署详细指南

## 🎯 推荐阅读顺序

1. **[ZEBUR.md](ZEBUR.md)** - 了解所有部署方式
2. **[ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md)** - 按照一键部署步骤操作
3. **[ZEBUR_MANUAL.md](ZEBUR_MANUAL.md)** - 参考详细步骤

## 💡 提示

1. **首次部署**: 建议先使用一键部署方式
2. **配置管理**: 在Zeabur控制台修改环境变量即可
3. **数据备份**: 定期备份存储卷中的数据
4. **监控日志**: 定期查看服务日志，及时发现异常
5. **成本控制**: 根据使用情况调整资源配置

## ❓ 需要帮助？

- 查看 [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md) 中的常见问题部分
- 查看 [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md) 中的问题排查部分
- 联系Zeabur支持: https://zeabur.com/support

## 🔗 有用链接

- **Zeabur**: https://zeabur.com
- **Zeabur控制台**: https://dash.zeabur.com
- **Zeabur文档**: https://zeabur.com/docs
- **GitHub**: https://github.com
- **Git下载**: https://git-scm.com/downloads
- **青果网络**: https://www.qg.net
- **DuckMail**: https://duckmail.sbs

---

*完整流程最后更新: 2026-02-02*
