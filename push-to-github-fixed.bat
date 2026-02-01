@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM 推送修改到GitHub脚本（改进版）
REM 使用方法: 双击运行或在命令行执行 push-to-github-fixed.bat

REM 创建日志文件
set LOG_FILE=%~dp0push-github-log.txt
echo 推送日志 - %date% %time% > "%LOG_FILE%"
echo ======================================== >> "%LOG_FILE%"

echo ==============================================================
echo 推送修改到GitHub（改进版）
echo ==============================================================
echo.
echo 日志文件: %LOG_FILE%
echo 如果脚本闪退，请查看日志文件了解错误详情
echo.
echo 按任意键继续...
pause >nul

REM 检查Git是否安装
echo.
echo [1/8] 检查Git安装...
echo [%date% %time%] 检查Git安装... >> "%LOG_FILE%"

git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git未安装或未添加到PATH
    echo [%date% %time%] Git未安装 >> "%LOG_FILE%"
    echo.
    echo 请检查:
    echo 1. Git是否已安装
    echo 2. Git是否添加到系统PATH
    echo 3. 访问: https://git-scm.com/downloads
    echo.
    echo 按任意键退出...
    pause >nul
    exit /b 1
)

for /f "tokens=*" %%i in ('git --version') do set GIT_VERSION=%%i
echo ✅ Git已安装: %GIT_VERSION%
echo [%date% %time%] Git版本: %GIT_VERSION% >> "%LOG_FILE%"
echo.

REM 进入项目目录
echo [2/8] 进入项目目录...
echo [%date% %time%] 进入项目目录: %~dp0 >> "%LOG_FILE%"

cd /d "%~dp0"
if %errorlevel% neq 0 (
    echo ❌ 无法进入项目目录
    echo [%date% %time%] 无法进入项目目录 >> "%LOG_FILE%"
    echo.
    echo 按任意键退出...
    pause >nul
    exit /b 1
)

set CURRENT_DIR=%cd%
echo ✅ 已进入项目目录: %CURRENT_DIR%
echo [%date% %time%] 当前目录: %CURRENT_DIR% >> "%LOG_FILE%"
echo.

REM 检查是否是Git仓库
echo [3/8] 检查Git仓库...
echo [%date% %time%] 检查Git仓库 >> "%LOG_FILE%"

if not exist ".git" (
    echo ⚠️  当前目录不是Git仓库，正在初始化...
    echo [%date% %time%] 初始化Git仓库 >> "%LOG_FILE%"
    git init
    if %errorlevel% neq 0 (
        echo ❌ Git初始化失败
        echo [%date% %time%] Git初始化失败 >> "%LOG_FILE%"
        echo.
        echo 按任意键退出...
        pause >nul
        exit /b 1
    )
    echo ✅ Git仓库初始化成功
    echo [%date% %time%] Git仓库初始化成功 >> "%LOG_FILE%"
) else (
    echo ✅ 已是Git仓库
    echo [%date% %time%] 已是Git仓库 >> "%LOG_FILE%"
)
echo.

REM 检查Git状态
echo [4/8] 检查Git状态...
echo [%date% %time%] 检查Git状态 >> "%LOG_FILE%"
echo.

git status
echo [%date% %time%] Git状态检查完成 >> "%LOG_FILE%"
echo.

REM 添加所有修改
echo [5/8] 添加所有修改...
echo [%date% %time%] 添加所有修改 >> "%LOG_FILE%"

git add .
if %errorlevel% neq 0 (
    echo ❌ 添加文件失败
    echo [%date% %time%] 添加文件失败，错误代码: %errorlevel% >> "%LOG_FILE%"
    echo.
    echo 按任意键退出...
    pause >nul
    exit /b 1
)
echo ✅ 文件添加成功
echo [%date% %time%] 文件添加成功 >> "%LOG_FILE%"
echo.

REM 提交修改
echo [6/8] 提交修改...
echo [%date% %time%] 提交修改 >> "%LOG_FILE%"

git commit -m "feat: 添加Zeabur部署文档和青果代理集成

- 添加完整的Zeabur部署文档
- 集成青果代理到注册流程
- 添加DuckMail邮箱服务
- 修复代理URL格式问题
- 添加部署脚本和配置文件
- 添加测试文件"
if %errorlevel% neq 0 (
    echo ⚠️  提交失败或没有需要提交的修改
    echo [%date% %time%] 提交失败，错误代码: %errorlevel% >> "%LOG_FILE%"
    echo.
    echo 可能是:
    echo 1. 没有需要提交的修改
    echo 2. 提交信息格式问题
    echo.
    echo 继续执行推送...
) else (
    echo ✅ 提交成功
    echo [%date% %time%] 提交成功 >> "%LOG_FILE%"
)
echo.

REM 检查远程仓库
echo [7/8] 检查远程仓库...
echo [%date% %time%] 检查远程仓库 >> "%LOG_FILE%"

git remote -v >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  未配置远程仓库
    echo [%date% %time%] 未配置远程仓库 >> "%LOG_FILE%"
    echo.
    echo 请输入你的GitHub用户名:
    set /p USERNAME="GitHub用户名: "
    echo.
    echo 请输入仓库名称（默认: gemini-business2api）:
    set /p REPO="仓库名称: "
    if "!REPO!"=="" set REPO=gemini-business2api
    echo.
    echo 配置远程仓库: https://github.com/!USERNAME!/!REPO!.git
    echo [%date% %time%] 配置远程仓库: https://github.com/!USERNAME!/!REPO!.git >> "%LOG_FILE%"
    
    git remote add origin https://github.com/!USERNAME!/!REPO!.git
    if %errorlevel% neq 0 (
        echo ❌ 配置远程仓库失败
        echo [%date% %time%] 配置远程仓库失败，错误代码: %errorlevel% >> "%LOG_FILE%"
        echo.
        echo 按任意键退出...
        pause >nul
        exit /b 1
    )
    echo ✅ 远程仓库配置成功
    echo [%date% %time%] 远程仓库配置成功 >> "%LOG_FILE%"
    echo.
) else (
    echo ✅ 远程仓库已配置
    git remote -v
    echo [%date% %time%] 远程仓库已配置 >> "%LOG_FILE%"
    echo.
)

REM 推送到GitHub
echo [8/8] 推送到GitHub...
echo [%date% %time%] 推送到GitHub >> "%LOG_FILE%"
echo.

git branch -M main
git push -u origin main
if %errorlevel% neq 0 (
    echo ❌ 推送失败
    echo [%date% %time%] 推送失败，错误代码: %errorlevel% >> "%LOG_FILE%"
    echo.
    echo 可能的原因:
    echo 1. GitHub用户名或仓库名称错误
    echo 2. 需要GitHub认证（用户名/密码/Token）
    echo 3. 网络连接问题
    echo 4. 仓库不存在
    echo.
    echo 解决方案:
    echo 1. 检查GitHub用户名和仓库名称是否正确
    echo 2. 使用GitHub Personal Access Token进行认证
    echo 3. 访问: https://github.com/settings/tokens
    echo 4. 创建Token时选择 'repo' 权限
    echo.
    echo 查看日志文件: %LOG_FILE%
    echo.
    echo 按任意键退出...
    pause >nul
    exit /b 1
)

echo ✅ 推送成功
echo [%date% %time%] 推送成功 >> "%LOG_FILE%"
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
echo 日志文件: %LOG_FILE%
echo.

pause
