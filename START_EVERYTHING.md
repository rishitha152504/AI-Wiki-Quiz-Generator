# 🚀 Start Everything - Quick Guide

## Complete Setup in 3 Steps

### Step 1: Start Backend ⚙️

1. **Go to QUIZ folder:**
   `C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ`

2. **Double-click:** `setup-backend-with-py.bat`

3. **Wait for:**
   ```
   INFO:     Uvicorn running on http://0.0.0.0:8000
   ```

4. **Keep this window open!**

5. **Test it:** Open http://localhost:8000/api/health in browser
   - Should see: `{"status":"healthy"}`

---

### Step 2: Start Frontend 🎨

1. **Still in QUIZ folder**

2. **Double-click:** `start-frontend.bat`

3. **Browser opens at:** http://localhost:3000

4. **Keep this window open too!**

5. **Check connection:** Press F12 → Console tab
   - Should see: `✅ Backend connection successful`

---

### Step 3: Test the App! 🎉

1. **In browser** (http://localhost:3000)
2. **Click "Generate Quiz" tab**
3. **URL is already filled:** `https://en.wikipedia.org/wiki/Alan_Turing`
4. **Click "Generate Quiz"**
5. **Wait ~30 seconds**
6. **Quiz appears!** 🎊

---

## ✅ What You Should Have Running

- **Backend window:** Shows "Uvicorn running on http://0.0.0.0:8000"
- **Frontend window:** Shows "Compiled successfully"
- **Browser:** Shows Wiki Quiz App at http://localhost:3000

---

## 🔧 If Something Doesn't Work

### Backend not starting?
- Check Python is installed: `python --version`
- Make sure `.env` file exists in `backend/` folder
- Try running `setup-backend-with-py.bat` again

### Frontend not connecting?
- Make sure backend is running first
- Check: http://localhost:8000/api/health works
- Refresh browser (F5)
- Check browser console (F12) for errors

### Quiz not generating?
- Make sure both backend and frontend are running
- Check backend window for errors
- Check browser console (F12) for errors
- Try a different Wikipedia URL

---

**That's it! Follow these 3 steps and you're done!** 🚀
