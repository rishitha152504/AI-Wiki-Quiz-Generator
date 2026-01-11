# Frontend-Backend Connection Guide

## ✅ Connection Status

Your frontend and backend are **already properly configured** to connect! Here's what's set up:

---

## Backend Configuration

### CORS (Cross-Origin Resource Sharing)

The backend is configured to accept requests from the frontend:

**File:** `backend/app/main.py`

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Default React port
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://localhost:3001",  # Alternative port
        "http://localhost:8080",  # Alternative port
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

✅ **This allows your frontend to connect!**

---

## Frontend Configuration

### API Base URL

**File:** `frontend/src/App.js`

```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
```

✅ **Defaults to `http://localhost:8000` (backend port)**

### Optional: Custom API URL

If your backend runs on a different port, create `frontend/.env`:

```env
REACT_APP_API_URL=http://localhost:8000
```

---

## Backend Endpoints

The backend provides these endpoints:

1. **Health Check:** `GET /api/health`
2. **Generate Quiz:** `POST /api/quiz/generate`
3. **Get History:** `GET /api/quiz/history`
4. **Get Quiz Details:** `GET /api/quiz/{id}`
5. **Delete Quiz:** `DELETE /api/quiz/{id}`

All endpoints are accessible at: `http://localhost:8000`

---

## How to Test Connection

### Step 1: Start Backend

```powershell
cd backend
.\venv\Scripts\activate
python run.py
```

**Should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2: Start Frontend

```powershell
cd frontend
npm start
```

**Should see:**
```
Compiled successfully!
Local: http://localhost:3000
```

### Step 3: Test in Browser

1. **Open:** http://localhost:3000
2. **Press F12** (Developer Tools)
3. **Go to Console tab**
4. **Look for:** `✅ Backend connection successful`

### Step 4: Test Health Endpoint

1. **Open new tab:** http://localhost:8000/api/health
2. **Should see:**
   ```json
   {"status":"healthy","message":"Backend is running and ready","database":"connected"}
   ```

---

## Connection Architecture

```
Frontend (React)          Backend (FastAPI)
localhost:3000    ────►    localhost:8000
     │                          │
     │  HTTP Requests           │
     │  (axios)                 │
     │                          │
     └──────────────────────────┘
          CORS Enabled ✅
          Ports: 3000 → 8000 ✅
          Methods: GET, POST ✅
```

---

## Troubleshooting Connection Issues

### Problem: "Cannot connect to backend"

**Check:**
1. Backend is running (see backend window)
2. Backend shows: `Uvicorn running on http://0.0.0.0:8000`
3. Test: http://localhost:8000/api/health works in browser

**Solution:**
- Start backend if not running
- Check backend window for errors
- Verify port 8000 is not in use

### Problem: "CORS error" in browser console

**Check:**
1. Frontend URL matches CORS allowed origins
2. Backend CORS configuration is correct

**Solution:**
- Frontend should use `http://localhost:3000` (default)
- Or update CORS in `backend/app/main.py` to include your frontend URL

### Problem: "Network Error" or "ECONNREFUSED"

**Check:**
1. Backend is running
2. Port 8000 is accessible
3. No firewall blocking connection

**Solution:**
- Start backend
- Check Windows Firewall settings
- Try: http://localhost:8000/api/health in browser

### Problem: Frontend shows "Loading..." forever

**Check:**
1. Backend is responding (test /api/health)
2. Browser console for errors (F12)
3. Network tab in browser (F12 → Network)

**Solution:**
- Check backend logs for errors
- Verify API endpoint URLs in frontend
- Check CORS configuration

---

## Verification Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000 (or 3001)
- [ ] http://localhost:8000/api/health works
- [ ] Browser console shows "✅ Backend connection successful"
- [ ] No CORS errors in console
- [ ] Can generate quizzes successfully

---

## No Changes Needed!

✅ **Frontend and backend are already properly configured!**

The connection should work automatically when both servers are running.

---

**Your frontend-backend connection is ready! Just start both servers and test!** 🚀
