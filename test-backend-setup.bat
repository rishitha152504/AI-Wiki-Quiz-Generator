@echo off
echo ========================================================================
echo Backend Setup Diagnostic Tool
echo ========================================================================
echo.

echo Checking Python installation...
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Python is installed
    python --version
) else (
    echo [ERROR] Python is NOT installed or not in PATH
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo.
echo Checking project structure...
cd /d "%~dp0"
if exist backend (
    echo [OK] backend directory exists
    cd backend
    if exist run.py (
        echo [OK] run.py exists
    ) else (
        echo [ERROR] run.py NOT found in backend directory
        pause
        exit /b 1
    )
    if exist requirements.txt (
        echo [OK] requirements.txt exists
    ) else (
        echo [ERROR] requirements.txt NOT found
        pause
        exit /b 1
    )
    if exist .env (
        echo [OK] .env file exists
    ) else (
        echo [WARNING] .env file NOT found - backend will not start without it
    )
    if exist venv (
        echo [OK] venv directory exists
    ) else (
        echo [INFO] venv not found - will be created on first run
    )
) else (
    echo [ERROR] backend directory NOT found
    echo Current directory: %CD%
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo Diagnostic complete!
echo ========================================================================
echo.
echo If all checks passed, try running: start-backend.bat
echo.
pause
