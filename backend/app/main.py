"""
FastAPI main application
Handles Wikipedia article processing and quiz generation
"""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import os
import requests
from dotenv import load_dotenv

from app.database import get_db, engine, Base
from app.models import WikiArticle
from app.schemas import WikiArticleResponse, WikiArticleCreate, WikiArticleList
from app.scraper import WikipediaScraper
from app.llm_service import LLMQuizGenerator

load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Wiki Quiz API",
    description="API for generating quizzes from Wikipedia articles",
    version="1.0.0"
)

# CORS middleware - Allow all localhost ports for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://localhost:3001",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
scraper = WikipediaScraper()
groq_api_key = os.getenv("GROQ_API_KEY")

# Validate API key
if not groq_api_key or groq_api_key == "your_groq_api_key_here":
    print("\n" + "="*60)
    print("ERROR: Groq API Key not configured!")
    print("="*60)
    print("Please follow these steps:")
    print("1. Get your free API key from: https://console.groq.com/keys")
    print("2. Open backend/.env file")
    print("3. Add: GROQ_API_KEY=your_actual_api_key")
    print("4. Restart the server")
    print("="*60 + "\n")
    raise ValueError(
        "GROQ_API_KEY not set. Please configure it in backend/.env file. "
        "Get your free key from: https://console.groq.com/keys"
    )

llm_generator = LLMQuizGenerator(groq_api_key)


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Wiki Quiz API is running"}


@app.get("/api/health")
def health_check():
    """Health check endpoint for connection testing"""
    return {
        "status": "healthy",
        "message": "Backend is running and ready",
        "database": "connected"
    }


@app.post("/api/quiz/generate", response_model=WikiArticleResponse, status_code=status.HTTP_201_CREATED)
def generate_quiz(article: WikiArticleCreate, db: Session = Depends(get_db)):
    """
    Generate quiz from Wikipedia article URL
    
    1. Check if article already exists in database (caching)
    2. Scrape Wikipedia article
    3. Generate quiz using LLM
    4. Store in database
    5. Return structured response
    """
    # Check if article already exists (caching) - This saves API calls!
    existing_article = db.query(WikiArticle).filter(WikiArticle.url == article.url).first()
    if existing_article:
        print(f"Returning cached quiz for: {article.url} (saves API quota!)")
        return existing_article

    try:
        # Step 1: Scrape Wikipedia article
        scraped_data = scraper.scrape_article(article.url)
        
        # Validate scraped content
        content_text = scraped_data.get('content_text', '')
        if not content_text or len(content_text) < 100:
            raise ValueError(
                f"Failed to extract sufficient content from the Wikipedia article. "
                f"This might be a disambiguation page, redirect, or page with very little content. "
                f"Please try a specific article URL. "
                f"Extracted {len(content_text)} characters. "
                f"\n\nTip: Use specific article URLs like: "
                f"\n- https://en.wikipedia.org/wiki/Python_(programming_language) (instead of just 'Python')"
                f"\n- https://en.wikipedia.org/wiki/Java_(programming_language) (instead of just 'Java')"
            )
        
        # Step 2: Generate quiz using LLM
        llm_result = llm_generator.generate_quiz(
            article_title=scraped_data['title'],
            article_content=scraped_data['content_text'],
            sections=scraped_data['sections']
        )
        
        # Step 3: Create database record
        db_article = WikiArticle(
            url=article.url,
            title=scraped_data['title'],
            summary=scraped_data['summary'],
            raw_html=scraped_data['raw_html'],
            key_entities=scraped_data['key_entities'],
            sections=scraped_data['sections'],
            quiz=llm_result['quiz'],
            related_topics=llm_result['related_topics']
        )
        
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        
        return db_article
        
    except ValueError as e:
        error_detail = str(e)
        print(f"Quiz generation error: {error_detail}")  # Log for debugging
        raise HTTPException(status_code=400, detail=error_detail)
    except requests.RequestException as e:
        error_detail = f"Failed to fetch Wikipedia article: {str(e)}"
        print(f"Network error: {error_detail}")
        raise HTTPException(status_code=400, detail=error_detail)
    except Exception as e:
        db.rollback()
        error_detail = f"Internal server error: {str(e)}"
        print(f"Unexpected error: {error_detail}")
        import traceback
        traceback.print_exc()  # Print full traceback for debugging
        raise HTTPException(status_code=500, detail=error_detail)


@app.get("/api/quiz/history", response_model=List[WikiArticleList])
def get_quiz_history(db: Session = Depends(get_db)):
    """Get list of all previously generated quizzes"""
    articles = db.query(WikiArticle).order_by(WikiArticle.created_at.desc()).all()
    return articles


@app.get("/api/quiz/urls")
def get_all_urls(db: Session = Depends(get_db)):
    """Get all Wikipedia URLs stored in database as a simple list"""
    articles = db.query(WikiArticle).order_by(WikiArticle.created_at.desc()).all()
    return {
        "total": len(articles),
        "urls": [
            {
                "id": article.id,
                "url": article.url,
                "title": article.title,
                "created_at": article.created_at.isoformat() if article.created_at else None,
                "quiz_count": len(article.quiz) if article.quiz else 0
            }
            for article in articles
        ]
    }


@app.get("/api/quiz/{article_id}", response_model=WikiArticleResponse)
def get_quiz_details(article_id: int, db: Session = Depends(get_db)):
    """Get detailed quiz information by article ID"""
    article = db.query(WikiArticle).filter(WikiArticle.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.delete("/api/quiz/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quiz(article_id: int, db: Session = Depends(get_db)):
    """Delete a quiz by article ID"""
    article = db.query(WikiArticle).filter(WikiArticle.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(article)
    db.commit()
    return None
