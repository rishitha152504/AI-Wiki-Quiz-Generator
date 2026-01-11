# Fix: Frontend Not Starting

## Problem
After pressing "Continue" in the frontend startup script, nothing happens.

## Quick Fix Steps

### Step 1: Check Node.js Installation

1. Open PowerShell or Command Prompt
2. Type: `node --version`
3. If you see an error, Node.js is not installed

**If Node.js is NOT installed:**
- Download from: https://nodejs.org/
- Install the LTS version
- Restart your computer after installation
- Try again

### Step 2: Run Diagnostic Tool

1. Double-click: `test-frontend-setup.bat`
2. This will check everything and tell you what's wrong

### Step 3: Manual Start (If Scripts Don't Work)

Open PowerShell in the QUIZ folder and run:

```powershell
cd frontend
npm install
npm start
```

---

## Common Issues & Solutions

### Issue 1: "Node.js is not recognized"
**Solution:** 
- Install Node.js from https://nodejs.org/
- Restart computer
- Try again

### Issue 2: "npm is not recognized"
**Solution:**
- Node.js installation includes npm
- Reinstall Node.js
- Restart computer

### Issue 3: Script runs but nothing happens
**Solution:**
- Open PowerShell manually
- Navigate to: `C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\frontend`
- Run: `npm start`
- This will show you the actual error

### Issue 4: Port 3000 already in use
**Solution:**
- Close other programs using port 3000
- Or change port in `package.json` (add: `"start": "set PORT=3001 && react-scripts start"`)

---

## Manual Start Method (Always Works)

1. **Open PowerShell**
   - Press Windows key
   - Type "PowerShell"
   - Right-click → "Run as Administrator" (optional)

2. **Navigate to frontend folder:**
   ```powershell
   cd "C:\Users\dines\OneDrive\Documents\Kln doucments\Rishitha\QUIZ\frontend"
   ```

3. **Install dependencies (if needed):**
   ```powershell
   npm install
   ```

4. **Start the server:**
   ```powershell
   npm start
   ```

5. **Browser should open automatically at http://localhost:3000**

---

## What Should Happen

When you run `npm start`, you should see:
```
Compiled successfully!

You can now view wiki-quiz-frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000

Note that the development build is not optimized.
```

If you see errors instead, copy the error message and check:
- Is Node.js installed? (`node --version`)
- Is npm installed? (`npm --version`)
- Are you in the frontend directory?
- Is port 3000 free?

---

## Still Not Working?

Run the diagnostic tool:
```
test-frontend-setup.bat
```

This will tell you exactly what's wrong!
