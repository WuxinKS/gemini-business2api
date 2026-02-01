@echo off
REM Zeabur快速部署脚本 (Windows版本)

echo ============================================================
echo Zeabur快速部署脚本 (Windows版本)
echo ============================================================
echo.

REM 检查必要的工具
echo 检查必要的工具...

where git >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Git未安装，请先安装Git
    echo 下载地址: https://git-scm.com/downloads
    pause
    exit /b 1
)

where curl >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ curl未安装，请先安装curl
    echo Windows 10+通常已包含curl
    pause
    exit /b 1
)

echo ✅ 所有必要的工具已安装

REM 检查是否已初始化Git仓库
echo.
echo 检查Git仓库...

if not exist ".git" (
    echo Git仓库未初始化，正在初始化...
    git init
    echo ✅ Git仓库初始化完成
) else (
    echo ✅ Git仓库已存在
)

REM 检查是否有远程仓库
echo.
echo 检查远程仓库...

git remote get-url origin >nul 2>nul
if %errorlevel% neq 0 (
    echo ⚠️ 未配置远程仓库
    echo.
    echo 请执行以下步骤：
    echo 1. 在GitHub创建新仓库
    echo 2. 运行: git remote add origin https://github.com/your-username/gemini-business2api.git
    echo 3. 运行: git push -u origin main
    echo.
    set /p continue="是否继续？(y/n): "
    if /i not "%continue%"=="y" (
        exit /b 1
    )
) else (
    echo ✅ 远程仓库已配置
    for /f "delims=" %%i in ('git remote get-url origin') do set REMOTE_URL=%%i
    echo   远程地址: %REMOTE_URL%
)

REM 添加所有文件
echo.
echo 添加文件到Git...

git add .

REM 检查是否有更改
git diff --cached --quiet >nul 2>nul
if %errorlevel% equ 0 (
    echo ⚠️ 没有需要提交的更改
) else (
    echo 正在提交更改...
    git commit -m "Update for Zeabur deployment"
    echo ✅ 更改已提交
)

REM 推送到远程仓库
echo.
echo 推送到远程仓库...

git remote get-url origin >nul 2>nul
if %errorlevel% equ 0 (
    echo 正在推送...
    git push -u origin main
    if %errorlevel% neq 0 (
        echo 尝试推送master分支...
        git push -u origin master
    )
    echo ✅ 代码已推送到GitHub
)

REM 显示部署说明
echo.
echo ============================================================
echo 部署说明
echo ============================================================
echo.
echo 1. 登录Zeabur控制台: https://dash.zeabur.com
echo 2. 点击"新建项目"
echo 3. 选择"从Git仓库导入"
echo 4. 授权GitHub并选择你的仓库
echo 5. 等待Zeabur克隆代码
echo.
echo 服务配置：
echo   - 构建命令: 见 ZEBUR_DEPLOYMENT.md
echo   - 启动命令: 见 ZEBUR_DEPLOYMENT.md
echo   - 端口: 7860
echo   - 环境变量: 见 ZEBUR_DEPLOYMENT.md
echo.
echo 详细部署指南: ZEBUR_DEPLOYMENT.md
echo 部署检查清单: ZEBUR_CHECKLIST.md
echo.
echo ============================================================
echo ✅ 准备完成！
echo ============================================================
echo.
pause
