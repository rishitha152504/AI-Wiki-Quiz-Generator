@echo off
echo ========================================================================
echo Starting Wiki Quiz Frontend...
echo ========================================================================
echo.

cd /d "%~dp0"
echo Current directory: %CD%
echo.

if not exist frontend (
    echo ERROR: Cannot find frontend directory!
    echo Please run this script from the project root directory (QUIZ folder)
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

echo Found frontend directory. Changing to frontend folder...
cd frontend
echo Now in: %CD%
echo.

REM Check if Node.js is installed
where node >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Node.js is not installed or not in PATH!
    echo Please install Node.js from: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

echo Node.js found. Checking npm...
where npm >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: npm is not found!
    echo.
    pause
    exit /b 1
)

echo npm found. Checking for node_modules...
if not exist node_modules (
    echo node_modules not found. Installing dependencies...
    echo This may take a few minutes...
    echo.
    call npm install
    if %ERRORLEVEL% NEQ 0 (
        echo.
        echo ERROR: Failed to install dependencies!
        echo.
        pause
        exit /b 1
    )
    echo.
    echo Dependencies installed successfully!
    echo.
) else (
    echo node_modules found. Skipping installation.
    echo.
)

echo ========================================================================
echo Starting React development server...
echo Frontend will be available at http://localhost:3000
echo Browser should open automatically...
echo ========================================================================
echo.
echo Press Ctrl+C to stop the server
echo.

call npm start

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to start frontend server!
    echo.
    echo Possible issues:
    echo - Port 3000 might be in use
    echo - npm dependencies might be corrupted
    echo - Try running: npm install
    echo.
    pause
)