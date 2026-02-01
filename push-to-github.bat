@echo off
REM 推送修改到GitHub脚本
REM 使用方法: 双击运行或在命令行执行 push-to-github.bat

echo ==============================================================
echo 推送修改到GitHub
echo ==============================================================
echo.

REM 检查Git是否安装
echo [1/7] 检查Git安装...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git未安装，请先安装Git
    echo 访问: https://git-scm.com/downloads
    pause
    exit /b 1
)
echo ✅ Git已安装
echo.

REM 进入项目目录
echo [2/7] 进入项目目录...
cd /d "%~dp0"
if %errorlevel% neq 0 (
    echo ❌ 无法进入项目目录
    pause
    exit /b 1
)
echo ✅ 已进入项目目录
echo.

REM 检查Git状态
echo [3/7] 检查Git状态...
git status
echo.

REM 添加所有修改
echo [4/7] 添加所有修改...
git add .
if %errorlevel% neq 0 (
    echo ❌ 添加文件失败
    pause
    exit /b 1
)
echo ✅ 文件添加成功
echo.

REM 提交修改
echo [5/7] 提交修改...
git commit -m "feat: 添加Zeabur部署文档和青果代理集成

- 添加完整的Zeabur部署文档
- 集成青果代理到注册流程
- 添加DuckMail邮箱服务
- 修复代理URL格式问题
- 添加部署脚本和配置文件
- 添加测试文件"
if %errorlevel% neq 0 (
    echo ❌ 提交失败
    pause
    exit /b 1
)
echo ✅ 提交成功
echo.

REM 检查远程仓库
echo [6/7] 检查远程仓库...
git remote -v >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  未配置远程仓库
    echo.
    echo 请输入你的GitHub用户名:
    set /p USERNAME="GitHub用户名: "
    echo.
    echo 请输入仓库名称（默认: gemini-business2api）:
    set /p REPO="仓库名称: "
    if "%REPO%"=="" set REPO=gemini-business2api
    echo.
    echo 配置远程仓库: https://github.com/%USERNAME%/%REPO%.git
    git remote add origin https://github.com/%USERNAME%/%REPO%.git
    if %errorlevel% neq 0 (
        echo ❌ 配置远程仓库失败
        pause
        exit /b 1
    )
    echo ✅ 远程仓库配置成功
    echo.
) else (
    echo ✅ 远程仓库已配置
    echo.
)

REM 推送到GitHub
echo [7/7] 推送到GitHub...
git branch -M main
git push -u origin main
if %errorlevel% neq 0 (
    echo ❌ 推送失败
    echo.
    echo 可能的原因:
    echo 1. GitHub用户名或仓库名称错误
    echo 2. 需要GitHub认证
    echo 3. 网络连接问题
    echo.
    echo 请检查后重试
    pause
    exit /b 1
)
echo ✅ 推送成功
echo.

echo ==============================================================
echo 推送完成！
echo ==============================================================
echo.
echo 访问你的GitHub仓库查看:
echo https://github.com/your-username/gemini-business2api
echo.
echo 接下来可以继续Zeabur部署:
echo 1. 访问 https://dash.zeabur.com
echo 2. 新建项目 -^> 新建服务
echo 3. 选择"预构建镜像"
echo 4. 输入: cooooookk/gemini-business2api:latest
echo 5. 配置环境变量
echo 6. 部署！
echo.

pause
