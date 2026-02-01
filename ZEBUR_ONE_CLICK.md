# Zeabur一键部署

## 🚀 最简单的部署方式

### 只需要3步：

1. **推送代码到GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/your-username/gemini-business2api.git
   git push -u origin main
   ```

2. **在Zeabur创建服务**
   - 访问 https://dash.zeabur.com
   - 新建项目 → 新建服务
   - 选择"预构建镜像"
   - 输入: `cooooookk/gemini-business2api:latest`
   - 点击"部署"

3. **配置环境变量**

   复制以下环境变量到Zeabur服务配置中：

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
   ```

4. **配置存储**

   - 创建存储卷: `data`
   - 挂载路径: `/app/data`

5. **完成！**

   访问: `https://your-service.zeabur.app/admin/health`

## ✅ 就这么简单！

不需要：
- ❌ 编写构建命令
- ❌ 编写启动命令
- ❌ 安装依赖
- ❌ 配置Dockerfile

只需要：
- ✅ 推送代码到GitHub
- ✅ 在Zeabur选择预构建镜像
- ✅ 配置环境变量
- ✅ 配置存储

## 📝 配置说明

### 必需配置

| 变量名 | 值 | 说明 |
|---------|-----|------|
| ADMIN_KEY | admin123456 | 管理员密码（建议修改） |
| QG_PROXY_ENABLED | true | 启用青果代理 |
| QG_PROXY_API_KEY | BYJ3MCP5 | 青果代理API Key |
| QG_PROXY_SECRET_KEY | 7B3C288DCF56 | 青果代理AuthPwd |
| DUCKMAIL_API_KEY | dk_9172ab8f7dc0bc4b845d2f2a38e1246afc6d4b28427fb711e191cd4c2ff309a1 | DuckMail API Key |
| TEMP_MAIL_PROVIDER | duckmail | 邮箱提供商 |

### 可选配置

| 变量名 | 默认值 | 说明 |
|---------|---------|------|
| BROWSER_ENGINE | dp | 浏览器引擎 |
| BROWSER_HEADLESS | false | 无头模式 |
| PORT | 7860 | 服务端口 |
| TZ | Asia/Shanghai | 时区 |

## 🔧 修改配置

在Zeabur控制台直接修改环境变量，然后重启服务即可。

## 💰 费用估算

- **Zeabur**: 约$5-10/月
- **青果代理**: 按次计费，约¥0.01/次
- **DuckMail**: 免费套餐或约$5/月

## 📖 详细文档

如果需要更详细的配置，请参考：
- [ZEBUR_DEPLOYMENT.md](ZEBUR_DEPLOYMENT.md) - 完整部署指南
- [ZEBUR_CHECKLIST.md](ZEBUR_CHECKLIST.md) - 部署检查清单

## ❓ 常见问题

**Q: 部署失败怎么办？**
A: 检查环境变量是否正确，查看服务日志。

**Q: 如何修改密码？**
A: 在Zeabur控制台修改ADMIN_KEY环境变量，然后重启服务。

**Q: 数据会丢失吗？**
A: 配置了存储卷后，数据会持久化保存。

**Q: 如何更新服务？**
A: 推送新代码到GitHub，在Zeabur点击"重新部署"。

---

*一键部署指南最后更新: 2026-02-02*
