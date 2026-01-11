# Quick Setup Guide

## Prerequisites Check

Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ Node.js 16+ installed
- ✅ PostgreSQL 12+ installed and running
- ✅ Google Gemini API key (get free tier at https://makersuite.google.com/app/apikey)

## Step-by-Step Setup

### 1. Database Setup

```bash
# Create PostgreSQL database
createdb wiki_quiz_db

# Or using psql
psql -U postgres
CREATE DATABASE wiki_quiz_db;
\q
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
# Copy .env.example to .env and edit with your credentials
# Windows:
copy .env.example .env
# Linux/Mac:
cp .env.example .env

# Edit .env file with your database URL and Gemini API key
# DATABASE_URL=postgresql://username:password@localhost:5432/wiki_quiz_db
# GEMINI_API_KEY=your_api_key_here

# Initialize database tables
python init_db.py

# Start backend server
python run.py
```

Backend should now be running at `http://localhost:8000`

### 3. Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend should now be running at `http://localhost:3000`

### 4. Test the Application

1. Open browser to `http://localhost:3000`
2. Go to "Generate Quiz" tab
3. Enter a Wikipedia URL: `https://en.wikipedia.org/wiki/Alan_Turing`
4. Click "Generate Quiz"
5. Wait for processing (may take 10-30 seconds)
6. View generated quiz
7. Try "Take Quiz Mode" to test interactively
8. Go to "Past Quizzes" tab to see history

## Troubleshooting

### Backend won't start
- Check PostgreSQL is running: `pg_isready`
- Verify DATABASE_URL in .env is correct
- Ensure virtual environment is activated
- Check all dependencies installed: `pip list`

### Frontend won't start
- Clear node_modules: `rm -rf node_modules && npm install`
- Check Node.js version: `node --version` (should be 16+)
- Verify backend is running on port 8000

### API errors
- Check GEMINI_API_KEY is set correctly
- Verify API key is valid and has quota
- Check backend logs for detailed error messages
- Ensure CORS is configured correctly

### Database errors
- Verify PostgreSQL is running
- Check database exists: `psql -l | grep wiki_quiz_db`
- Ensure user has permissions
- Try recreating database: `dropdb wiki_quiz_db && createdb wiki_quiz_db`

## Verification Checklist

- [ ] Backend server running on port 8000
- [ ] Frontend server running on port 3000
- [ ] Database connection successful
- [ ] Can generate quiz from Wikipedia URL
- [ ] Quiz appears in history tab
- [ ] Details modal opens correctly
- [ ] Take Quiz mode works

## Next Steps

- Test with different Wikipedia articles
- Review generated quiz quality
- Check database for stored data
- Explore API documentation at `http://localhost:8000/docs`
