"""
Script to view all Wikipedia URLs stored in the database
Displays a formatted table of all processed articles
"""
from app.database import SessionLocal
from app.models import WikiArticle
from datetime import datetime

def view_all_urls():
    """Display all Wikipedia URLs stored in the database"""
    db = SessionLocal()
    
    try:
        # Get all articles ordered by creation date
        articles = db.query(WikiArticle).order_by(WikiArticle.created_at.desc()).all()
        
        if not articles:
            print("\n" + "="*80)
            print("No articles found in database.")
            print("="*80)
            return
        
        print("\n" + "="*80)
        print("DATABASE: All Processed Wikipedia URLs")
        print("="*80)
        print(f"\nTotal Articles: {len(articles)}\n")
        
        # Print table header
        print(f"{'ID':<5} {'Title':<40} {'URL':<50} {'Created At':<20}")
        print("-" * 120)
        
        # Print each article
        for article in articles:
            # Truncate title and URL if too long
            title = article.title[:37] + "..." if len(article.title) > 40 else article.title
            url = article.url[:47] + "..." if len(article.url) > 50 else article.url
            created = article.created_at.strftime("%Y-%m-%d %H:%M") if article.created_at else "N/A"
            
            print(f"{article.id:<5} {title:<40} {url:<50} {created:<20}")
        
        print("-" * 120)
        print(f"\nTotal: {len(articles)} articles")
        
        # Additional statistics
        print("\n" + "="*80)
        print("STATISTICS")
        print("="*80)
        
        # Count articles with quizzes
        articles_with_quizzes = sum(1 for a in articles if a.quiz and len(a.quiz) > 0)
        print(f"Articles with quizzes: {articles_with_quizzes}/{len(articles)}")
        
        # Show unique URLs
        unique_urls = set(a.url for a in articles)
        print(f"Unique URLs: {len(unique_urls)}")
        
        # Show date range
        if articles:
            dates = [a.created_at for a in articles if a.created_at]
            if dates:
                oldest = min(dates)
                newest = max(dates)
                print(f"Date range: {oldest.strftime('%Y-%m-%d')} to {newest.strftime('%Y-%m-%d')}")
        
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\nERROR: Failed to query database: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


def view_detailed_info(article_id: int = None):
    """View detailed information about a specific article or all articles"""
    db = SessionLocal()
    
    try:
        if article_id:
            article = db.query(WikiArticle).filter(WikiArticle.id == article_id).first()
            if not article:
                print(f"\nArticle with ID {article_id} not found!")
                return
            
            articles = [article]
        else:
            articles = db.query(WikiArticle).order_by(WikiArticle.created_at.desc()).all()
        
        for article in articles:
            print("\n" + "="*80)
            print(f"ARTICLE ID: {article.id}")
            print("="*80)
            print(f"Title: {article.title}")
            print(f"URL: {article.url}")
            print(f"Created: {article.created_at}")
            print(f"Summary: {article.summary[:200] if article.summary else 'N/A'}...")
            
            if article.sections:
                print(f"Sections: {len(article.sections)} sections")
                print(f"  {', '.join(article.sections[:5])}")
            
            if article.quiz:
                print(f"Quiz Questions: {len(article.quiz)} questions")
            
            if article.related_topics:
                print(f"Related Topics: {', '.join(article.related_topics[:5])}")
            
            print("="*80)
        
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # View detailed info for specific article
        try:
            article_id = int(sys.argv[1])
            view_detailed_info(article_id)
        except ValueError:
            print("Usage: python view_database.py [article_id]")
            print("Example: python view_database.py 1")
    else:
        # View all URLs in table format
        view_all_urls()
