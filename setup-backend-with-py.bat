@echo off
echo ========================================================================
echo Backend Setup Using Python Launcher (py)
echo ========================================================================
echo.

cd /d "%~dp0\backend"

echo Checking for Python launcher (py)...
where py >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python launcher (py) not found!
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Python launcher found!
py --version
echo.

echo Removing old virtual environment (if exists)...
if exist venv (
    rmdir /s /q venv
    echo Old venv removed.
) else (
    echo No old venv found.
)
echo.

echo Creating new virtual environment...
echo This may take a minute...
py -m venv venv
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to create virtual environment!
    echo.
    pause
    exit /b 1
)
echo Virtual environment created successfully!
echo.

echo Activating virtual environment...
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

echo Checking .env file...
if not exist .env (
    echo.
    echo WARNING: .env file not found!
    echo Please create backend/.env file with:
    echo   GEMINI_API_KEY=your_api_key_here
    echo.
    pause
    exit /b 1
) else (
    echo .env file found.
    echo.
)

echo Installing dependencies...
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
echo.
echo ========================================================================
echo Setup complete! Starting server...
echo ========================================================================
echo.
echo Server will be available at: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo Health Check: http://localhost:8000/api/health
echo.
echo IMPORTANT: Keep this window open while the server is running!
echo Press Ctrl+C to stop the server
echo.
echo ========================================================================
echo.

python run.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to start server!
    echo.
    pause
)
