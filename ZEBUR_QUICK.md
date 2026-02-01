# Zeabur一键部署指南

## 最简单的一键部署方式

### 步骤1: 推送代码到GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/gemini-business2api.git
git push -u origin main
```

### 步骤2: 在Zeabur创建服务

1. 访问 https://dash.zeabur.com
2. 点击"新建项目"
3. 点击"新建服务"
4. 选择"预构建镜像"
5. 输入镜像名称: `cooooookk/gemini-business2api:latest`
6. 点击"部署"

### 步骤3: 配置环境变量

在服务配置中添加以下环境变量：

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

### 步骤4: 配置存储

1. 在服务配置中点击"存储"
2. 创建新存储卷，命名为`data`
3. 挂载路径: `/app/data`

### 步骤5: 配置端口

- **内部端口**: 7860
- **公开端口**: 自动分配

### 步骤6: 配置健康检查

- **路径**: `/admin/health`
- **端口**: 7860

### 步骤7: 部署

点击"部署"按钮，等待部署完成。

## 访问服务

部署完成后，Zeabur会提供一个访问URL，例如：
```
https://your-service.zeabur.app
```

访问健康检查端点验证服务是否正常：
```
https://your-service.zeabur.app/admin/health
```

## 完成！

就这么简单！服务已经部署完成，可以开始使用了。

## 修改配置

如果需要修改配置，直接在Zeabur控制台修改环境变量，然后重启服务即可。

## 注意事项

1. **修改密码**: 将`ADMIN_KEY`修改为强密码
2. **代理配置**: 确保青果代理账户余额充足
3. **邮箱配置**: 确保DuckMail API Key有效
4. **数据持久化**: 确保配置了存储卷

---

*一键部署指南最后更新: 2026-02-02*
