@echo off
echo ========================================================================
echo Starting Wiki Quiz Backend Server...
echo ========================================================================
echo.

cd /d "%~dp0"
echo Current directory: %CD%
echo.

if not exist backend (
    echo ERROR: Cannot find backend directory!
    echo Please run this script from the project root directory (QUIZ folder)
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

echo Found backend directory. Changing to backend folder...
cd backend
echo Now in: %CD%
echo.

REM Check if Python is installed
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    echo After installing Python:
    echo 1. Restart your computer
    echo 2. Run this script again
    echo.
    pause
    exit /b 1
)

echo Python found. Checking version...
python --version
echo.

REM Check if virtual environment exists
if not exist venv (
    echo Virtual environment not found. Creating venv...
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
) else (
    echo Virtual environment found.
    echo.
)

echo Activating virtual environment...
call venv\Scripts\activate
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to activate virtual environment!
    echo.
    pause
    exit /b 1
)

echo Virtual environment activated.
echo.

REM Check if .env file exists
if not exist .env (
    echo.
    echo WARNING: .env file not found!
    echo Please create backend/.env file with:
    echo   GEMINI_API_KEY=your_api_key_here
    echo.
    echo You can copy backend/.env.example to backend/.env and edit it.
    echo.
    pause
    exit /b 1
) else (
    echo .env file found.
    echo.
)

echo Installing/updating dependencies...
echo This may take a few minutes on first run...
echo.
pip install -r requirements.txt --quiet
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

echo ========================================================================
echo Starting FastAPI server on http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo Health Check: http://localhost:8000/api/health
echo ========================================================================
echo.
echo Press Ctrl+C to stop the server
echo.

python run.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to start backend server!
    echo.
    echo Possible issues:
    echo - Check if port 8000 is already in use
    echo - Check if .env file has correct GEMINI_API_KEY
    echo - Check Python and dependencies are installed correctly
    echo.
    pause
)