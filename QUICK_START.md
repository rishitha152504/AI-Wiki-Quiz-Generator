# 🚀 Quick Start - Run & Connect

## Windows Users (Easiest Method)

### Step 1: Start Backend
Double-click **`start-backend.bat`** or run in PowerShell:
```powershell
.\start-backend.bat
```
Wait until you see: `Uvicorn running on http://0.0.0.0:8000`

### Step 2: Start Frontend (New Terminal)
Double-click **`start-frontend.bat`** or run in PowerShell:
```powershell
.\start-frontend.bat
```
Browser will open automatically at `http://localhost:3000`

## ⚠️ First Time Setup

### Backend Setup (One-time)
1. Create `backend/.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
2. Get API key from: https://makersuite.google.com/app/apikey

### Frontend Setup (One-time)
- Dependencies install automatically when you run `start-frontend.bat`

## ✅ Verify Connection

1. **Backend Health Check:**
   - Open: http://localhost:8000/api/health
   - Should see: `{"status":"healthy"}`

2. **Frontend Connection:**
   - Open: http://localhost:3000
   - Open browser console (F12)
   - Should see: `✅ Backend connection successful`

## 🎯 Test It!

1. Go to "Generate Quiz" tab
2. Enter: `https://en.wikipedia.org/wiki/Alan_Turing`
3. Click "Generate Quiz"
4. Wait ~30 seconds
5. Quiz appears! 🎉

## 🔧 Troubleshooting

**Backend won't start?**
- Check if port 8000 is in use
- Verify `backend/.env` file exists with `GEMINI_API_KEY`

**Frontend can't connect?**
- Make sure backend is running first
- Check browser console for errors
- Verify backend is at `http://localhost:8000`

**Need more help?**
- See `CONNECTION_GUIDE.md` for detailed troubleshooting
