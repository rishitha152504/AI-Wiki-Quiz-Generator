# Connection Guide - Wiki Quiz App

This guide will help you run and connect the frontend and backend properly.

## 🚀 Quick Start (Windows)

### Option 1: Using Batch Scripts (Easiest)

1. **Start Backend:**
   - Double-click `start-backend.bat` OR
   - Open PowerShell/Terminal and run:
     ```powershell
     .\start-backend.bat
     ```
   - Wait for: `Uvicorn running on http://0.0.0.0:8000`

2. **Start Frontend (New Terminal):**
   - Double-click `start-frontend.bat` OR
   - Open a NEW PowerShell/Terminal and run:
     ```powershell
     .\start-frontend.bat
     ```
   - Wait for browser to open at `http://localhost:3000`

### Option 2: Manual Setup

#### Backend Setup

1. **Open Terminal/PowerShell:**
   ```powershell
   cd backend
   ```

2. **Activate Virtual Environment:**
   ```powershell
   venv\Scripts\activate
   ```

3. **Create .env file** (if not exists):
   ```powershell
   # Create .env file in backend/ directory
   # Add these lines:
   GEMINI_API_KEY=your_actual_api_key_here
   # DATABASE_URL is optional - defaults to SQLite
   ```

4. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Start Server:**
   ```powershell
   python run.py
   ```

   ✅ Backend should be running at: `http://localhost:8000`
   ✅ API Docs at: `http://localhost:8000/docs`

#### Frontend Setup

1. **Open NEW Terminal/PowerShell:**
   ```powershell
   cd frontend
   ```

2. **Install Dependencies:**
   ```powershell
   npm install
   ```

3. **Start Development Server:**
   ```powershell
   npm start
   ```

   ✅ Frontend should open at: `http://localhost:3000`

## 🔍 Verify Connection

### Test Backend:
1. Open browser: `http://localhost:8000/api/health`
2. Should see: `{"status":"healthy","message":"Backend is running and ready","database":"connected"}`

### Test Frontend:
1. Open browser: `http://localhost:3000`
2. Check browser console (F12) - should see: `✅ Backend connection successful`
3. If you see error, backend is not running or not accessible

## 🔧 Troubleshooting

### Backend Won't Start

**Error: "GEMINI_API_KEY not set"**
- Solution: Create `backend/.env` file with:
  ```
  GEMINI_API_KEY=your_api_key_here
  ```
- Get API key from: https://makersuite.google.com/app/apikey

**Error: "Port 8000 already in use"**
- Solution: Kill process using port 8000:
  ```powershell
  netstat -ano | findstr :8000
  taskkill /PID <PID_NUMBER> /F
  ```
- Or change port in `backend/run.py`:
  ```python
  uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)
  ```
- Then update `frontend/src/App.js`:
  ```javascript
  const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8001';
  ```

**Error: "Module not found"**
- Solution: Make sure virtual environment is activated:
  ```powershell
  cd backend
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

### Frontend Won't Connect to Backend

**Error: "Cannot connect to backend"**
- ✅ Check backend is running: Open `http://localhost:8000/api/health`
- ✅ Check CORS: Backend allows `http://localhost:3000` (already configured)
- ✅ Check API URL: Frontend uses `http://localhost:8000` by default
- ✅ Check firewall: Windows Firewall might be blocking connection

**Error: "Network Error" or "CORS Error"**
- Solution: Make sure backend CORS includes your frontend URL
- Already configured in `backend/app/main.py` for `localhost:3000`

**Frontend shows "Loading..." forever**
- Check browser console (F12) for errors
- Check Network tab to see if API calls are failing
- Verify backend is actually running

### Database Issues

**SQLite (Default - No Setup Required)**
- Works out of the box
- Database file: `backend/wiki_quiz.db`
- No configuration needed

**PostgreSQL (Optional)**
- Create database: `createdb wiki_quiz_db`
- Add to `backend/.env`:
  ```
  DATABASE_URL=postgresql://username:password@localhost:5432/wiki_quiz_db
  ```

## 📝 Configuration Files

### Backend `.env` file location: `backend/.env`
```
GEMINI_API_KEY=your_api_key_here
# Optional: DATABASE_URL=postgresql://user:pass@localhost:5432/wiki_quiz_db
```

### Frontend `.env` file location: `frontend/.env` (optional)
```
REACT_APP_API_URL=http://localhost:8000
```

## ✅ Connection Checklist

- [ ] Backend server running on port 8000
- [ ] Can access `http://localhost:8000/api/health`
- [ ] Frontend server running on port 3000
- [ ] Can access `http://localhost:3000`
- [ ] Browser console shows "✅ Backend connection successful"
- [ ] No CORS errors in browser console
- [ ] Can generate a quiz successfully

## 🎯 Testing the Connection

1. **Start both servers** (backend and frontend)
2. **Open frontend**: `http://localhost:3000`
3. **Open browser console** (F12 → Console tab)
4. **Look for**: `✅ Backend connection successful`
5. **Try generating a quiz**:
   - Enter URL: `https://en.wikipedia.org/wiki/Alan_Turing`
   - Click "Generate Quiz"
   - Should work without errors!

## 🆘 Still Having Issues?

1. **Check both terminals** - Are both servers running?
2. **Check ports** - Are 8000 and 3000 available?
3. **Check .env file** - Does it exist and have correct API key?
4. **Check browser console** - What errors do you see?
5. **Test backend directly** - Can you access `http://localhost:8000/docs`?

## 📞 Quick Commands Reference

```powershell
# Backend
cd backend
venv\Scripts\activate
python run.py

# Frontend (new terminal)
cd frontend
npm start

# Test backend health
curl http://localhost:8000/api/health
# Or open in browser: http://localhost:8000/api/health
```
