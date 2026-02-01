# 推送修改到GitHub指南

## 📋 需要推送的修改

### 新增文件

**Zeabur部署文档**:
- ✅ ZEBUR.md - 部署文档总览
- ✅ ZEBUR_ONE_CLICK.md - 一键部署指南
- ✅ ZEBUR_QUICK.md - 快速部署指南
- ✅ ZEBUR_DEPLOYMENT.md - 完整部署指南
- ✅ ZEBUR_CHECKLIST.md - 部署检查清单
- ✅ ZEBUR_MANUAL.md - 手动部署详细指南
- ✅ ZEBUR_COMPLETE.md - 完整部署流程

**配置文件**:
- ✅ zeabur-simple.yml - 简化版Zeabur配置
- ✅ zeabur.yml - 完整版Zeabur配置

**部署脚本**:
- ✅ deploy-zeabur.bat - Windows快速部署脚本
- ✅ deploy-zeabur.sh - Linux/Mac快速部署脚本

**其他文档**:
- ✅ ZEBUR_INDEX.md - 部署文档索引
- ✅ ZEBUR_README.md - Zeabur部署文档总览
- ✅ ZEBUR_SUMMARY.md - Zeabur部署总结

### 修改的文件

- ✅ core/qg_proxy_client.py - 修复代理URL格式
- ✅ core/config.py - 添加青果代理配置
- ✅ core/register_service.py - 集成青果代理
- ✅ .env - 添加青果代理和DuckMail配置
- ✅ .env.example - 更新配置示例

### 新增测试文件

- ✅ test_qg_proxy.py - 青果代理测试
- ✅ test_api.py - 后端API测试
- ✅ test_register.py - 注册功能测试
- ✅ test_full_register.py - 完整注册流程测试
- ✅ sync_env_to_db.py - 环境变量同步脚本

## 🚀 推送步骤

### 步骤1: 安装Git（如果还没有）

**Windows用户**:
1. 访问 https://git-scm.com/downloads
2. 下载Windows版本的Git
3. 运行安装程序，使用默认设置
4. 安装完成后，重新打开命令行窗口

**验证安装**:
```cmd
git --version
```

### 步骤2: 配置Git用户信息

```cmd
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 步骤3: 进入项目目录

```cmd
cd C:\Users\Admin\Downloads\gemini-business2api-main\gemini-business2api-main
```

### 步骤4: 检查Git状态

```cmd
git status
```

### 步骤5: 添加所有修改

```cmd
git add .
```

### 步骤6: 提交修改

```cmd
git commit -m "feat: 添加Zeabur部署文档和青果代理集成

- 添加完整的Zeabur部署文档
- 集成青果代理到注册流程
- 添加DuckMail邮箱服务
- 修复代理URL格式问题
- 添加部署脚本和配置文件
- 添加测试文件"
```

### 步骤7: 连接到GitHub仓库

**如果是第一次推送**:
```cmd
git remote add origin https://github.com/your-username/gemini-business2api.git
```

**如果已经连接过**:
```cmd
git remote -v
```

### 步骤8: 推送到GitHub

```cmd
git branch -M main
git push -u origin main
```

**注意**: 将 `your-username` 替换为你的GitHub用户名

## 🔐 使用SSH推送（推荐）

如果遇到HTTPS认证问题，可以使用SSH：

### 步骤1: 生成SSH密钥

```cmd
ssh-keygen -t ed25519 -C "your.email@example.com"
```

### 步骤2: 添加SSH密钥到GitHub

1. 复制SSH公钥:
   ```cmd
   type %USERPROFILE%\.ssh\id_ed25519.pub
   ```

2. 访问 https://github.com/settings/keys
3. 点击"New SSH key"
4. 粘贴公钥
5. 点击"Add SSH key"

### 步骤3: 使用SSH URL推送

```cmd
git remote set-url origin git@github.com:your-username/gemini-business2api.git
git push -u origin main
```

## 📝 完整命令脚本

复制以下脚本到命令行，一次性执行：

```cmd
REM 进入项目目录
cd C:\Users\Admin\Downloads\gemini-business2api-main\gemini-business2api-main

REM 添加所有修改
git add .

REM 提交修改
git commit -m "feat: 添加Zeabur部署文档和青果代理集成

- 添加完整的Zeabur部署文档
- 集成青果代理到注册流程
- 添加DuckMail邮箱服务
- 修复代理URL格式问题
- 添加部署脚本和配置文件
- 添加测试文件"

REM 推送到GitHub（替换your-username）
git remote add origin https://github.com/your-username/gemini-business2api.git
git branch -M main
git push -u origin main
```

## ❓ 常见问题

### Q: Git命令找不到怎么办？

A:
1. 访问 https://git-scm.com/downloads
2. 下载并安装Git
3. 重新打开命令行窗口

### Q: 推送失败，提示认证错误怎么办？

A:
1. 使用SSH方式推送（推荐）
2. 或者使用GitHub Personal Access Token

### Q: 提示"remote origin already exists"怎么办？

A:
```cmd
git remote remove origin
git remote add origin https://github.com/your-username/gemini-business2api.git
```

### Q: 推送失败，提示"Updates were rejected"怎么办？

A:
```cmd
git pull --rebase origin main
git push -u origin main
```

### Q: 如何查看已修改的文件？

A:
```cmd
git status
git diff
```

### Q: 如何撤销提交？

A:
```cmd
git reset --soft HEAD~1
```

## ✅ 验证推送成功

推送完成后，访问你的GitHub仓库查看：
```
https://github.com/your-username/gemini-business2api
```

应该能看到所有新增和修改的文件。

## 🎯 下一步

推送成功后，可以继续Zeabur部署：

1. 访问 https://dash.zeabur.com
2. 新建项目 → 新建服务
3. 选择"预构建镜像"
4. 输入: `cooooookk/gemini-business2api:latest`
5. 配置环境变量
6. 部署！

---

*推送指南最后更新: 2026-02-02*
