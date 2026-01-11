@echo off
echo ========================================================================
echo Fixing Backend Python Virtual Environment
echo ========================================================================
echo.

cd /d "%~dp0\backend"

echo Step 1: Checking Python installation...
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

python --version
echo Python found!
echo.

echo Step 2: Removing old virtual environment...
if exist venv (
    echo Deleting old venv folder...
    rmdir /s /q venv
    echo Old venv removed.
) else (
    echo No old venv found.
)
echo.

echo Step 3: Creating new virtual environment...
echo This may take a minute...
python -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to create virtual environment!
    echo.
    pause
    exit /b 1
)
echo Virtual environment created successfully!
echo.

echo Step 4: Activating virtual environment...
call venv\Scripts\activate
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to activate virtual environment!
    echo.
    pause
    exit /b 1
)
echo Virtual environment activated!
echo.

echo Step 5: Installing dependencies...
echo This may take a few minutes...
echo.
pip install --upgrade pip
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to install dependencies!
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo Setup complete! Virtual environment is ready.
echo ========================================================================
echo.
echo Now you can start the backend with:
echo   python run.py
echo.
echo Or use: start-backend.bat
echo.
pause
