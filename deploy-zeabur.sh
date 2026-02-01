#!/bin/bash

# Zeabur快速部署脚本

set -e

echo "============================================================"
echo "Zeabur快速部署脚本"
echo "============================================================"

# 检查必要的工具
echo ""
echo "检查必要的工具..."

if ! command -v git &> /dev/null; then
    echo "❌ Git未安装，请先安装Git"
    exit 1
fi

if ! command -v curl &> /dev/null; then
    echo "❌ curl未安装，请先安装curl"
    exit 1
fi

echo "✅ 所有必要的工具已安装"

# 检查是否已初始化Git仓库
echo ""
echo "检查Git仓库..."

if [ ! -d ".git" ]; then
    echo "Git仓库未初始化，正在初始化..."
    git init
    echo "✅ Git仓库初始化完成"
else
    echo "✅ Git仓库已存在"
fi

# 检查是否有远程仓库
echo ""
echo "检查远程仓库..."

if ! git remote get-url origin &> /dev/null 2>&1; then
    echo "⚠️ 未配置远程仓库"
    echo ""
    echo "请执行以下步骤："
    echo "1. 在GitHub创建新仓库"
    echo "2. 运行: git remote add origin https://github.com/your-username/gemini-business2api.git"
    echo "3. 运行: git push -u origin main"
    echo ""
    read -p "是否继续？(y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✅ 远程仓库已配置"
    REMOTE_URL=$(git remote get-url origin)
    echo "  远程地址: $REMOTE_URL"
fi

# 添加所有文件
echo ""
echo "添加文件到Git..."

git add .

# 检查是否有更改
if git diff --cached --quiet; then
    echo "⚠️ 没有需要提交的更改"
else
    echo "正在提交更改..."
    git commit -m "Update for Zeabur deployment"
    echo "✅ 更改已提交"
fi

# 推送到远程仓库
echo ""
echo "推送到远程仓库..."

if git remote get-url origin &> /dev/null 2>&1; then
    echo "正在推送..."
    git push -u origin main || git push -u origin master
    echo "✅ 代码已推送到GitHub"
fi

# 显示部署说明
echo ""
echo "============================================================"
echo "部署说明"
echo "============================================================"
echo ""
echo "1. 登录Zeabur控制台: https://dash.zeabur.com"
echo "2. 点击'新建项目'"
echo "3. 选择'从Git仓库导入'"
echo "4. 授权GitHub并选择你的仓库"
echo "5. 等待Zeabur克隆代码"
echo ""
echo "服务配置："
echo "  - 构建命令: 见 ZEBUR_DEPLOYMENT.md"
echo "  - 启动命令: 见 ZEBUR_DEPLOYMENT.md"
echo "  - 端口: 7860"
echo "  - 环境变量: 见 ZEBUR_DEPLOYMENT.md"
echo ""
echo "详细部署指南: ZEBUR_DEPLOYMENT.md"
echo "部署检查清单: ZEBUR_CHECKLIST.md"
echo ""
echo "============================================================"
echo "✅ 准备完成！"
echo "============================================================"
