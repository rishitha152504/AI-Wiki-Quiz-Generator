# 🎯 START HERE - Wiki Quiz App

## ⚡ Fastest Way to Run (Windows)

### 1️⃣ Start Backend
**Double-click:** `start-backend.bat`

Wait for: `Uvicorn running on http://0.0.0.0:8000`

### 2️⃣ Start Frontend (New Window)
**Double-click:** `start-frontend.bat`

Browser opens automatically at `http://localhost:3000`

### 3️⃣ Test It!
1. Enter URL: `https://en.wikipedia.org/wiki/Alan_Turing`
2. Click "Generate Quiz"
3. Wait ~30 seconds
4. Done! 🎉

---

## ⚠️ First Time? Setup Required

### Backend Setup (One-time)
1. Create file: `backend/.env`
2. Add this line:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
3. Get API key: https://makersuite.google.com/app/apikey

### That's it! No database setup needed (uses SQLite by default)

---

## ✅ Verify Everything Works

### Test Backend:
Open browser: http://localhost:8000/api/health
Should see: `{"status":"healthy"}`

### Test Frontend:
1. Open: http://localhost:3000
2. Press F12 (open console)
3. Should see: `✅ Backend connection successful`

---

## 🆘 Having Issues?

### Backend won't start?
- Check `backend/.env` file exists
- Verify it has `GEMINI_API_KEY=...`
- Make sure port 8000 is free

### Frontend can't connect?
- Make sure backend is running first!
- Check browser console (F12) for errors
- Verify backend at: http://localhost:8000/api/health

### Need more help?
- See `QUICK_START.md` for detailed steps
- See `CONNECTION_GUIDE.md` for troubleshooting

---

## 📁 Project Structure

```
QUIZ/
├── backend/          # FastAPI backend
│   ├── app/          # Application code
│   ├── .env          # Configuration (create this!)
│   └── run.py        # Start server
├── frontend/         # React frontend
│   ├── src/          # Source code
│   └── package.json  # Dependencies
├── start-backend.bat # Windows: Start backend
├── start-frontend.bat# Windows: Start frontend
└── START_HERE.md     # This file!
```

---

## 🎓 What This App Does

1. **Input:** Wikipedia article URL
2. **Process:** Scrapes article, uses AI to generate quiz
3. **Output:** Interactive quiz with questions, answers, explanations

**Features:**
- ✅ Generate quizzes from Wikipedia
- ✅ View quiz history
- ✅ Take interactive quizzes
- ✅ Score tracking
- ✅ Multiple difficulty levels

---

**Ready? Start with step 1 above!** 🚀
