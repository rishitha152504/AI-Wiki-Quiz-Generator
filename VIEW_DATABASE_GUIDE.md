# View Database Data - Complete Guide

## Methods to View Stored Wikipedia URLs

There are **3 ways** to view all processed Wikipedia URLs stored in your database:

---

## Method 1: Using Python Script (Recommended) ⭐

### Step 1: Run the Script

```powershell
cd backend
.\venv\Scripts\activate
python view_database.py
```

### Step 2: View Output

You'll see a formatted table showing:
- ID
- Title
- URL
- Created At

**Example Output:**
```
================================================================================
DATABASE: All Processed Wikipedia URLs
================================================================================

Total Articles: 5

ID    Title                                    URL                                                  Created At          
------------------------------------------------------------------------------------------------------------------------
5     Alan Turing                               https://en.wikipedia.org/wiki/Alan_Turing           2025-01-15 10:30
4     Python Programming Language               https://en.wikipedia.org/wiki/Python_(programming... 2025-01-15 09:15
...
```

### View Detailed Info for Specific Article

```powershell
python view_database.py 1
```

This shows detailed information about article ID 1.

---

## Method 2: Using Frontend (Web Interface)

### Step 1: Start Frontend

```powershell
cd frontend
npm start
```

### Step 2: View in Browser

1. **Go to:** http://localhost:3000
2. **Click:** "Past Quizzes" tab
3. **See table** with all URLs

The table shows:
- ID
- Title
- Wikipedia URL (clickable)
- Created At
- Actions (View Quiz button)

---

## Method 3: Using API Endpoint (Direct)

### Option A: Browser

1. **Open browser**
2. **Go to:** http://localhost:8000/api/quiz/history
3. **See JSON** with all articles

### Option B: New Endpoint (Just URLs)

**Go to:** http://localhost:8000/api/quiz/urls

Returns:
```json
{
  "total": 5,
  "urls": [
    {
      "id": 1,
      "url": "https://en.wikipedia.org/wiki/Alan_Turing",
      "title": "Alan Turing",
      "created_at": "2025-01-15T10:30:00",
      "quiz_count": 8
    },
    ...
  ]
}
```

---

## Method 4: Direct Database Query (PostgreSQL)

If using PostgreSQL, you can query directly:

### Using pgAdmin

1. **Open pgAdmin**
2. **Connect to database:** `wiki_quiz_db`
3. **Run query:**
   ```sql
   SELECT id, url, title, created_at 
   FROM wiki_articles 
   ORDER BY created_at DESC;
   ```

### Using psql Command Line

```powershell
psql -U postgres -d wiki_quiz_db
```

Then run:
```sql
SELECT id, url, title, created_at FROM wiki_articles ORDER BY created_at DESC;
```

---

## Quick Commands Reference

### View All URLs (Python Script)
```powershell
cd backend
.\venv\Scripts\activate
python view_database.py
```

### View Specific Article Details
```powershell
python view_database.py 1
```

### View via API (Browser)
- All data: http://localhost:8000/api/quiz/history
- Just URLs: http://localhost:8000/api/quiz/urls

### View via Frontend
- http://localhost:3000 → "Past Quizzes" tab

---

## What Data is Stored

For each Wikipedia URL, the database stores:

- **id** - Unique identifier
- **url** - Wikipedia article URL
- **title** - Article title
- **summary** - First paragraph summary
- **sections** - List of article sections
- **quiz** - Generated quiz questions (JSON)
- **related_topics** - Related topics (JSON)
- **key_entities** - People, organizations, locations (JSON)
- **created_at** - When quiz was generated
- **updated_at** - Last update time

---

## Export Data (Optional)

### Export to CSV

You can modify `view_database.py` to export to CSV:

```python
import csv

# Add to view_database.py
def export_to_csv():
    db = SessionLocal()
    articles = db.query(WikiArticle).all()
    
    with open('wiki_urls.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Title', 'URL', 'Created At'])
        for article in articles:
            writer.writerow([article.id, article.title, article.url, article.created_at])
    
    print("Exported to wiki_urls.csv")
```

---

## Summary

✅ **Easiest:** Use frontend "Past Quizzes" tab
✅ **Most detailed:** Use Python script `view_database.py`
✅ **For developers:** Use API endpoints
✅ **For database admins:** Query PostgreSQL directly

**All methods show the same data - choose what's easiest for you!** 🚀
