@echo off
echo ========================================================================
echo Frontend Setup Diagnostic Tool
echo ========================================================================
echo.

echo Checking Node.js installation...
where node >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Node.js is installed
    node --version
) else (
    echo [ERROR] Node.js is NOT installed or not in PATH
    echo Please install Node.js from: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

echo.
echo Checking npm installation...
where npm >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] npm is installed
    npm --version
) else (
    echo [ERROR] npm is NOT found
    echo.
    pause
    exit /b 1
)

echo.
echo Checking project structure...
cd /d "%~dp0"
if exist frontend (
    echo [OK] frontend directory exists
    cd frontend
    if exist package.json (
        echo [OK] package.json exists
    ) else (
        echo [ERROR] package.json NOT found in frontend directory
        pause
        exit /b 1
    )
    if exist node_modules (
        echo [OK] node_modules exists
    ) else (
        echo [WARNING] node_modules NOT found - will need to run npm install
    )
) else (
    echo [ERROR] frontend directory NOT found
    echo Current directory: %CD%
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo All checks passed! Frontend should be ready to start.
echo ========================================================================
echo.
echo To start frontend, run: start-frontend.bat
echo.
pause
