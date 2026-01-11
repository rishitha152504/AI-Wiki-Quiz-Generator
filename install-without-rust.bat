@echo off
echo ========================================================================
echo Installing Dependencies (Using Pre-built Wheels - No Rust Needed)
echo ========================================================================
echo.

cd /d "%~dp0\backend"

if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run setup-backend.bat first
    echo.
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to activate virtual environment!
    echo.
    pause
    exit /b 1
)
echo.

echo Upgrading pip to latest version...
python -m pip install --upgrade pip --quiet
echo.

echo Installing dependencies with pre-built wheels...
echo This may take a few minutes...
echo.

REM Install packages one by one to avoid compilation issues
pip install fastapi>=0.104.1 --quiet
pip install "uvicorn[standard]>=0.24.0" --quiet
pip install sqlalchemy>=2.0.23 --quiet
pip install beautifulsoup4>=4.12.2 --quiet
pip install requests>=2.31.0 --quiet
pip install langchain>=0.1.0 --quiet
pip install langchain-google-genai>=0.0.6 --quiet
pip install google-generativeai>=0.3.2 --quiet
pip install "pydantic>=2.9.0" --quiet
pip install pydantic-settings>=2.1.0 --quiet
pip install python-dotenv>=1.0.0 --quiet
pip install lxml>=4.9.3 --quiet

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Some packages failed to install!
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo ✅ Installation Complete!
echo ========================================================================
echo.
echo All dependencies installed successfully using pre-built wheels.
echo No Rust compilation was needed!
echo.
echo You can now start the backend with: python run.py
echo Or use: setup-backend.bat
echo.
pause
