# 推送修改到GitHub脚本（WuxinKS专用）
# 使用方法: 在PowerShell中执行 .\push-to-github-WuxinKS.ps1

Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "推送修改到GitHub（WuxinKS专用）" -ForegroundColor Cyan
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""

# GitHub配置
$GitHubUsername = "WuxinKS"
$RepoName = "gemini-business2api"
$RemoteUrl = "https://github.com/$GitHubUsername/$RepoName.git"

Write-Host "GitHub用户名: $GitHubUsername" -ForegroundColor Yellow
Write-Host "仓库名称: $RepoName" -ForegroundColor Yellow
Write-Host "远程仓库: $RemoteUrl" -ForegroundColor Yellow
Write-Host ""

# 进入项目目录
Write-Host "[1/5] 进入项目目录..." -ForegroundColor Yellow
try {
    Set-Location $PSScriptRoot
    $CurrentDir = Get-Location
    Write-Host "✅ 已进入项目目录: $CurrentDir" -ForegroundColor Green
} catch {
    Write-Host "❌ 无法进入项目目录" -ForegroundColor Red
    Read-Host "按回车键退出"
    exit 1
}
Write-Host ""

# 检查Git状态
Write-Host "[2/5] 检查Git状态..." -ForegroundColor Yellow
git status
Write-Host ""

# 添加所有修改
Write-Host "[3/5] 添加所有修改..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 添加文件失败" -ForegroundColor Red
    Read-Host "按回车键退出"
    exit 1
}
Write-Host "✅ 文件添加成功" -ForegroundColor Green
Write-Host ""

# 提交修改
Write-Host "[4/5] 提交修改..." -ForegroundColor Yellow
git commit -m "feat: 添加Zeabur部署文档和青果代理集成

- 添加完整的Zeabur部署文档
- 集成青果代理到注册流程
- 添加DuckMail邮箱服务
- 修复代理URL格式问题
- 添加部署脚本和配置文件
- 添加测试文件"

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  提交失败或没有需要提交的修改" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "可能是:" -ForegroundColor Yellow
    Write-Host "1. 没有需要提交的修改" -ForegroundColor White
    Write-Host "2. 提交信息格式问题" -ForegroundColor White
    Write-Host ""
    Write-Host "继续执行推送..." -ForegroundColor Yellow
} else {
    Write-Host "✅ 提交成功" -ForegroundColor Green
}
Write-Host ""

# 检查远程仓库
Write-Host "[5/6] 检查远程仓库..." -ForegroundColor Yellow
$RemoteOutput = git remote -v 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  未配置远程仓库，正在配置..." -ForegroundColor Yellow
    git remote add origin $RemoteUrl
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ 配置远程仓库失败" -ForegroundColor Red
        Read-Host "按回车键退出"
        exit 1
    }
    Write-Host "✅ 远程仓库配置成功: $RemoteUrl" -ForegroundColor Green
} else {
    Write-Host "✅ 远程仓库已配置" -ForegroundColor Green
    Write-Host $RemoteOutput
}
Write-Host ""

# 推送到GitHub
Write-Host "[6/6] 推送到GitHub..." -ForegroundColor Yellow
Write-Host "目标仓库: $RemoteUrl" -ForegroundColor Cyan
Write-Host ""

git branch -M main
git push -u origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 推送失败" -ForegroundColor Red
    Write-Host ""
    Write-Host "可能的原因:" -ForegroundColor Yellow
    Write-Host "1. 需要GitHub认证（用户名/密码/Token）" -ForegroundColor White
    Write-Host "2. 网络连接问题" -ForegroundColor White
    Write-Host "3. 仓库不存在" -ForegroundColor White
    Write-Host ""
    Write-Host "解决方案:" -ForegroundColor Yellow
    Write-Host "1. 使用GitHub Personal Access Token进行认证" -ForegroundColor White
    Write-Host "2. 访问: https://github.com/settings/tokens" -ForegroundColor White
    Write-Host "3. 创建Token时选择 'repo' 权限" -ForegroundColor White
    Write-Host "4. 推送时使用Token作为密码" -ForegroundColor White
    Write-Host ""
    Write-Host "认证格式:" -ForegroundColor Yellow
    Write-Host "用户名: $GitHubUsername" -ForegroundColor White
    Write-Host "密码: <你的Personal Access Token>" -ForegroundColor White
    Write-Host ""
    Read-Host "按回车键退出"
    exit 1
}

Write-Host "✅ 推送成功" -ForegroundColor Green
Write-Host ""

Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "推送完成！" -ForegroundColor Green
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "访问你的GitHub仓库查看:" -ForegroundColor White
Write-Host "$RemoteUrl" -ForegroundColor Cyan
Write-Host ""

Read-Host "按回车键退出"
