@echo off
echo ========================================================================
echo Python Installation Checker
echo ========================================================================
echo.

echo Checking for Python installation...
echo.

REM Check python command
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] 'python' command found!
    python --version
    echo.
    goto :check_py
) else (
    echo [NOT FOUND] 'python' command not found
    echo.
)

:check_py
REM Check py launcher
where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] 'py' launcher found!
    py --version
    echo.
    goto :check_python3
) else (
    echo [NOT FOUND] 'py' launcher not found
    echo.
)

:check_python3
REM Check python3 command
where python3 >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] 'python3' command found!
    python3 --version
    echo.
    goto :summary
) else (
    echo [NOT FOUND] 'python3' command not found
    echo.
)

:summary
echo ========================================================================
echo Summary
echo ========================================================================
echo.

where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo ✅ Python is installed and accessible!
    echo.
    echo You can now run: fix-backend-python.bat
    echo.
    pause
    exit /b 0
)

where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo ✅ Python launcher (py) is available!
    echo.
    echo You can use 'py' instead of 'python' in commands.
    echo Example: py -m venv venv
    echo.
    pause
    exit /b 0
)

echo ❌ Python is NOT installed or not in PATH!
echo.
echo ========================================================================
echo SOLUTION: Install Python
echo ========================================================================
echo.
echo 1. Go to: https://www.python.org/downloads/
echo 2. Download Python 3.12 (or latest)
echo 3. Run installer
echo 4. IMPORTANT: Check "Add Python to PATH" ✅
echo 5. Click "Install Now"
echo 6. Restart your computer
echo 7. Run this script again to verify
echo.
echo For detailed instructions, see: INSTALL_PYTHON_GUIDE.md
echo.
pause
