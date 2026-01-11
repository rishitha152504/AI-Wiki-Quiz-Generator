@echo off
echo ========================================================================
echo Creating .env file for backend
echo ========================================================================
echo.

cd /d "%~dp0\backend"

if exist .env (
    echo .env file already exists!
    echo.
    choice /C YN /M "Do you want to overwrite it"
    if errorlevel 2 goto :end
    if errorlevel 1 goto :create
)

:create
echo Creating .env file...
(
echo # Google Gemini API Key
echo # Get your free API key from: https://makersuite.google.com/app/apikey
echo # Replace 'your_api_key_here' with your actual API key
echo GEMINI_API_KEY=your_api_key_here
) > .env

echo.
echo ========================================================================
echo .env file created successfully!
echo ========================================================================
echo.
echo Location: %CD%\.env
echo.
echo NEXT STEPS:
echo 1. Open the .env file in Notepad
echo 2. Replace 'your_api_key_here' with your actual API key
echo 3. Get your API key from: https://makersuite.google.com/app/apikey
echo 4. Save the file
echo.
echo ========================================================================
pause

:end
