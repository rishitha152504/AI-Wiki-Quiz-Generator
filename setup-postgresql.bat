@echo off
echo ========================================================================
echo PostgreSQL Setup Helper
echo ========================================================================
echo.

echo This script will help you set up PostgreSQL for the Wiki Quiz App.
echo.
echo Prerequisites:
echo - PostgreSQL must be installed
echo - Database must be created (wiki_quiz_db)
echo - You need your PostgreSQL username and password
echo.

pause

cd /d "%~dp0\backend"

echo.
echo Step 1: Checking virtual environment...
if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run setup-backend.bat first
    echo.
    pause
    exit /b 1
)

echo Virtual environment found.
echo.

echo Step 2: Activating virtual environment...
call venv\Scripts\activate
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to activate virtual environment!
    echo.
    pause
    exit /b 1
)
echo Virtual environment activated.
echo.

echo Step 3: Installing PostgreSQL driver (psycopg2-binary)...
pip install psycopg2-binary
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to install psycopg2-binary!
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================================================
echo PostgreSQL Driver Installed!
echo ========================================================================
echo.
echo Next steps:
echo 1. Make sure PostgreSQL is installed and running
echo 2. Create database: wiki_quiz_db
echo 3. Update backend/.env file with DATABASE_URL:
echo.
echo    DATABASE_URL=postgresql://postgres:your_password@localhost:5432/wiki_quiz_db
echo.
echo 4. Replace 'your_password' with your PostgreSQL password
echo 5. Restart backend server
echo.
echo For detailed instructions, see: POSTGRESQL_SETUP.md
echo.
pause
