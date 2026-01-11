@echo off
echo ========================================================================
echo Complete Backend Setup and Start
echo ========================================================================
echo.

cd /d "%~dp0\backend"

echo Step 1: Checking Python installation...
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python found!
python --version
echo.

echo Step 2: Removing old virtual environment (if exists)...
if exist venv (
    echo Deleting old venv...
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

echo Step 5: Checking .env file...
if not exist .env (
    echo.
    echo WARNING: .env file not found!
    echo Please create backend/.env file with:
    echo   GEMINI_API_KEY=your_api_key_here
    echo.
    pause
    exit /b 1
) else (
    echo .env file found. Good!
    echo.
)

echo Step 6: Installing dependencies...
echo This may take 3-5 minutes on first run...
echo Please wait...
echo.
pip install --upgrade pip --quiet
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
echo ✅ Setup Complete! Starting Backend Server...
echo ========================================================================
echo.
echo Backend will be available at:
echo   - Main API: http://localhost:8000
echo   - API Docs: http://localhost:8000/docs
echo   - Health Check: http://localhost:8000/api/health
echo.
echo ⚠️  IMPORTANT: Keep this window open while the server is running!
echo    Press Ctrl+C to stop the server
echo.
echo ========================================================================
echo.

python run.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to start server!
    echo.
    echo Possible issues:
    echo - Port 8000 might be in use
    echo - Check .env file has correct GEMINI_API_KEY
    echo.
    pause
)
