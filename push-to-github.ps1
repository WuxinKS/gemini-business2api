# 推送修改到GitHub脚本（PowerShell版本）
# 使用方法: 在PowerShell中执行 .\push-to-github.ps1

Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "推送修改到GitHub（PowerShell版本）" -ForegroundColor Cyan
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""

# 创建日志文件
$LogFile = Join-Path $PSScriptRoot "push-github-log.txt"
"推送日志 - $(Get-Date)" | Out-File -FilePath $LogFile -Encoding UTF8
"========================================" | Out-File -FilePath $LogFile -Append -Encoding UTF8

# 检查Git是否安装
Write-Host "[1/8] 检查Git安装..." -ForegroundColor Yellow
"[$(Get-Date)] 检查Git安装..." | Out-File -FilePath $LogFile -Append -Encoding UTF8

try {
    $GitVersion = git --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Git未安装"
    }
    Write-Host "✅ Git已安装: $GitVersion" -ForegroundColor Green
    "[$(Get-Date)] Git版本: $GitVersion" | Out-File -FilePath $LogFile -Append -Encoding UTF8
} catch {
    Write-Host "❌ Git未安装或未添加到PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "请检查:" -ForegroundColor Yellow
    Write-Host "1. Git是否已安装" -ForegroundColor White
    Write-Host "2. Git是否添加到系统PATH" -ForegroundColor White
    Write-Host "3. 访问: https://git-scm.com/downloads" -ForegroundColor White
    Write-Host ""
    Read-Host "按回车键退出"
    exit 1
}

Write-Host ""

# 进入项目目录
Write-Host "[2/8] 进入项目目录..." -ForegroundColor Yellow
"[$(Get-Date)] 进入项目目录: $PSScriptRoot" | Out-File -FilePath $LogFile -Append -Encoding UTF8

try {
    Set-Location $PSScriptRoot
    $CurrentDir = Get-Location
    Write-Host "✅ 已进入项目目录: $CurrentDir" -ForegroundColor Green
    "[$(Get-Date)] 当前目录: $CurrentDir" | Out-File -FilePath $LogFile -Append -Encoding UTF8
} catch {
    Write-Host "❌ 无法进入项目目录" -ForegroundColor Red
    Read-Host "按回车键退出"
    exit 1
}

Write-Host ""

# 检查是否是Git仓库
Write-Host "[3/8] 检查Git仓库..." -ForegroundColor Yellow
"[$(Get-Date)] 检查Git仓库" | Out-File -FilePath $LogFile -Append -Encoding UTF8

if (-not (Test-Path ".git")) {
    Write-Host "⚠️  当前目录不是Git仓库，正在初始化..." -ForegroundColor Yellow
    "[$(Get-Date)] 初始化Git仓库" | Out-File -FilePath $LogFile -Append -Encoding UTF8
    
    git init
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Git初始化失败" -ForegroundColor Red
        Read-Host "按回车键退出"
        exit 1
    }
    
    Write-Host "✅ Git仓库初始化成功" -ForegroundColor Green
    "[$(Get-Date)] Git仓库初始化成功" | Out-File -FilePath $LogFile -Append -Encoding UTF8
} else {
    Write-Host "✅ 已是Git仓库" -ForegroundColor Green
    "[$(Get-Date)] 已是Git仓库" | Out-File -FilePath $LogFile -Append -Encoding UTF8
}

Write-Host ""

# 检查Git状态
Write-Host "[4/8] 检查Git状态..." -ForegroundColor Yellow
"[$(Get-Date)] 检查Git状态" | Out-File -FilePath $LogFile -Append -Encoding UTF8
Write-Host ""

git status
"[$(Get-Date)] Git状态检查完成" | Out-File -FilePath $LogFile -Append -Encoding UTF8

Write-Host ""

# 添加所有修改
Write-Host "[5/8] 添加所有修改..." -ForegroundColor Yellow
"[$(Get-Date)] 添加所有修改" | Out-File -FilePath $LogFile -Append -Encoding UTF8

git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 添加文件失败" -ForegroundColor Red
    Read-Host "按回车键退出"
    exit 1
}

Write-Host "✅ 文件添加成功" -ForegroundColor Green
"[$(Get-Date)] 文件添加成功" | Out-File -FilePath $LogFile -Append -Encoding UTF8
Write-Host ""

# 提交修改
Write-Host "[6/8] 提交修改..." -ForegroundColor Yellow
"[$(Get-Date)] 提交修改" | Out-File -FilePath $LogFile -Append -Encoding UTF8

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
    "[$(Get-Date)] 提交成功" | Out-File -FilePath $LogFile -Append -Encoding UTF8
}

Write-Host ""

# 检查远程仓库
Write-Host "[7/8] 检查远程仓库..." -ForegroundColor Yellow
"[$(Get-Date)] 检查远程仓库" | Out-File -FilePath $LogFile -Append -Encoding UTF8

$RemoteOutput = git remote -v 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  未配置远程仓库" -ForegroundColor Yellow
    "[$(Get-Date)] 未配置远程仓库" | Out-File -FilePath $LogFile -Append -Encoding UTF8
    Write-Host ""
    
    $Username = Read-Host "请输入你的GitHub用户名"
    $RepoName = Read-Host "请输入仓库名称（默认: gemini-business2api）"
    
    if ([string]::IsNullOrWhiteSpace($RepoName)) {
        $RepoName = "gemini-business2api"
    }
    
    $RemoteUrl = "https://github.com/$Username/$RepoName.git"
    Write-Host ""
    Write-Host "配置远程仓库: $RemoteUrl" -ForegroundColor Cyan
    "[$(Get-Date)] 配置远程仓库: $RemoteUrl" | Out-File -FilePath $LogFile -Append -Encoding UTF8
    
    git remote add origin $RemoteUrl
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ 配置远程仓库失败" -ForegroundColor Red
        Read-Host "按回车键退出"
        exit 1
    }
    
    Write-Host "✅ 远程仓库配置成功" -ForegroundColor Green
    "[$(Get-Date)] 远程仓库配置成功" | Out-File -FilePath $LogFile -Append -Encoding UTF8
    Write-Host ""
} else {
    Write-Host "✅ 远程仓库已配置" -ForegroundColor Green
    Write-Host $RemoteOutput
    "[$(Get-Date)] 远程仓库已配置" | Out-File -FilePath $LogFile -Append -Encoding UTF8
    Write-Host ""
}

# 推送到GitHub
Write-Host "[8/8] 推送到GitHub..." -ForegroundColor Yellow
"[$(Get-Date)] 推送到GitHub" | Out-File -FilePath $LogFile -Append -Encoding UTF8
Write-Host ""

git branch -M main
git push -u origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 推送失败" -ForegroundColor Red
    "[$(Get-Date)] 推送失败，错误代码: $LASTEXITCODE" | Out-File -FilePath $LogFile -Append -Encoding UTF8
    Write-Host ""
    Write-Host "可能的原因:" -ForegroundColor Yellow
    Write-Host "1. GitHub用户名或仓库名称错误" -ForegroundColor White
    Write-Host "2. 需要GitHub认证（用户名/密码/Token）" -ForegroundColor White
    Write-Host "3. 网络连接问题" -ForegroundColor White
    Write-Host "4. 仓库不存在" -ForegroundColor White
    Write-Host ""
    Write-Host "解决方案:" -ForegroundColor Yellow
    Write-Host "1. 检查GitHub用户名和仓库名称是否正确" -ForegroundColor White
    Write-Host "2. 使用GitHub Personal Access Token进行认证" -ForegroundColor White
    Write-Host "3. 访问: https://github.com/settings/tokens" -ForegroundColor White
    Write-Host "4. 创建Token时选择 'repo' 权限" -ForegroundColor White
    Write-Host ""
    Write-Host "查看日志文件: $LogFile" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "按回车键退出"
    exit 1
}

Write-Host "✅ 推送成功" -ForegroundColor Green
"[$(Get-Date)] 推送成功" | Out-File -FilePath $LogFile -Append -Encoding UTF8
Write-Host ""

Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host "推送完成！" -ForegroundColor Green
Write-Host "==============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "访问你的GitHub仓库查看:" -ForegroundColor White
Write-Host "https://github.com/your-username/gemini-business2api" -ForegroundColor Cyan
Write-Host ""
Write-Host "接下来可以继续Zeabur部署:" -ForegroundColor White
Write-Host "1. 访问 https://dash.zeabur.com" -ForegroundColor White
Write-Host "2. 新建项目 -> 新建服务" -ForegroundColor White
Write-Host "3. 选择'预构建镜像'" -ForegroundColor White
Write-Host "4. 输入: cooooookk/gemini-business2api:latest" -ForegroundColor White
Write-Host "5. 配置环境变量" -ForegroundColor White
Write-Host "6. 部署！" -ForegroundColor White
Write-Host ""
Write-Host "日志文件: $LogFile" -ForegroundColor Yellow
Write-Host ""

Read-Host "按回车键退出"
