# Zeabur部署文档

## 🚀 一键部署（推荐）

**最简单的部署方式，只需3步！**

查看: [ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md)

**特点**:
- ✅ 使用预构建镜像，无需编译
- ✅ 只需配置环境变量
- ✅ 3步完成部署

---

## 📋 部署文档索引

| 文档 | 说明 | 复杂度 |
|------|------|---------|
| [ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md) | 一键部署 | ⭐ |
| [ZEBUR_QUICK.md](ZEBUR_QUICK.md) | 快速部署 | ⭐⭐ |
| [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md) | 完整部署指南 | ⭐⭐⭐ |
| [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md) | 部署检查清单 | ⭐⭐ |

---

## 📁 配置文件

| 文件 | 说明 |
|------|------|
| [zeabur-simple.yml](zeabur-simple.yml) | 简化版Zeabur配置 |
| [zeabur.yml](zeabur.yml) | 完整版Zeabur配置 |

---

## 🛠 部署脚本

| 脚本 | 说明 |
|------|------|
| [deploy-zeabur.bat](deploy-zeabur.bat) | Windows快速部署脚本 |
| [deploy-zeabur.sh](deploy-zeabur.sh) | Linux/Mac快速部署脚本 |

---

## 🎯 推荐流程

### 第一次部署

1. 📖 阅读 [ZEBUR_ONE_CLICK.md](ZEBUR_ONE_CLICK.md)
2. 📤 推送代码到GitHub
3. 🌐 在Zeabur创建服务
4. ⚙️ 配置环境变量
5. ✅ 完成！

---

## 💡 快速开始

### 方式1: 一键部署（推荐）

```bash
# 1. 推送代码
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/gemini-business2api.git
git push -u origin main

# 2. 在Zeabur创建服务
# 访问: https://dash.zeabur.com
# 新建项目 → 新建服务
# 选择"预构建镜像"
# 输入: cooooookk/gemini-business2api:latest
# 点击"部署"

# 3. 配置环境变量
# 复制 ZEBUR_ONE_CLICK.md 中的环境变量

# 4. 完成！
```

---

## 🔗 相关链接

- **Zeabur**: https://zeabur.com
- **Zeabur控制台**: https://dash.zeabur.com
- **Zeabur文档**: https://zeabur.com/docs
- **青果网络**: https://www.qg.net
- **DuckMail**: https://duckmail.sbs

---

## ❓ 需要帮助？

- 查看 [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md) 中的常见问题
- 查看 [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md) 中的问题排查
- 联系Zeabur支持: https://zeabur.com/support

---

*文档最后更新: 2026-02-02*
