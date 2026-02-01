# Zeabur部署 - 选择你的部署方式

## 🚀 一键部署（推荐）

**文件**: [ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md)

**特点**:
- ✅ 最简单，只需3步
- ✅ 使用预构建镜像，无需编译
- ✅ 只需配置环境变量
- ✅ 适合快速部署

**适合人群**: 想要快速部署的用户

**开始部署**: 查看 [ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md)

---

## 📋 快速部署

**文件**: [ZEBUR_QUICK.md](ZEBUR_QUICK.md)

**特点**:
- ✅ 简单易用
- ✅ 步骤清晰
- ✅ 配置简单
- ✅ 适合大多数场景

**适合人群**: 需要一些自定义配置的用户

**开始部署**: 查看 [ZEBUR_QUICK.md](ZEBUR_QUICK.md)

---

## 📚 完整部署指南

**文件**: [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md)

**特点**:
- ✅ 详细的部署步骤
- ✅ 完整的配置说明
- ✅ 常见问题解答
- ✅ 性能优化建议
- ✅ 安全建议

**适合人群**: 需要完全控制部署过程的用户

**开始部署**: 查看 [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md)

---

## ✅ 部署检查清单

**文件**: [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md)

**特点**:
- ✅ 详细的检查项
- ✅ 确保不遗漏步骤
- ✅ 问题排查指南

**适合人群**: 需要确保部署正确性的用户

**开始部署**: 查看 [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md)

---

## 📁 配置文件

### zeabur-simple.yml
简化版Zeabur配置文件，包含所有必需的环境变量。

### zeabur.yml
完整版Zeabur配置文件，包含构建和启动命令。

---

## 🛠 部署脚本

### deploy-zeabur.bat
Windows快速部署脚本，自动准备代码并推送到GitHub。

### deploy-zeabur.sh
Linux/Mac快速部署脚本，自动准备代码并推送到GitHub。

---

## 🎯 推荐部署流程

### 第一次部署

1. 阅读 [ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md)
2. 推送代码到GitHub
3. 在Zeabur创建服务
4. 配置环境变量
5. 完成！

### 需要自定义

1. 阅读 [ZEBUR_QUICK.md](ZEBUR_QUICK.md)
2. 根据需要修改配置
3. 推送代码到GitHub
4. 在Zeabur创建服务
5. 配置环境变量
6. 完成！

### 需要完全控制

1. 阅读 [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md)
2. 使用 [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md) 检查
3. 推送代码到GitHub
4. 在Zeabur创建服务
5. 按照详细步骤配置
6. 完成！

---

## 📖 文档索引

| 文档 | 用途 | 复杂度 |
|------|------|---------|
| [ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md) | 一键部署 | ⭐ |
| [ZEBUR_QUICK.md](ZEBUR_QUICK.md) | 快速部署 | ⭐⭐ |
| [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md) | 完整指南 | ⭐⭐⭐ |
| [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md) | 检查清单 | ⭐⭐ |

---

## 💡 快速开始

### 最快的方式（推荐）

```bash
# 1. 推送代码
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/gemini-business2api.git
git push -u origin main

# 2. 在Zeabur创建服务
# - 访问 https://dash.zeabur.com
# - 新建项目 → 新建服务
# - 选择"预构建镜像"
# - 输入: cooooookk/gemini-business2api:latest
# - 点击"部署"

# 3. 配置环境变量
# 复制 ZEBUR_ONE_CLICK.md 中的环境变量到Zeabur

# 4. 完成！
```

---

## 🔗 相关链接

- **Zeabur官网**: https://zeabur.com
- **Zeabur文档**: https://zeabur.com/docs
- **Zeabur控制台**: https://dash.zeabur.com
- **青果网络**: https://www.qg.net
- **DuckMail**: https://duckmail.sbs

---

## ❓ 需要帮助？

- 查看 [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md) 中的常见问题部分
- 查看 [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md) 中的问题排查部分
- 联系Zeabur支持: https://zeabur.com/support

---

*部署文档索引最后更新: 2026-02-02*
