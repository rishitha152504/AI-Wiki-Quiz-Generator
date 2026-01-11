"""
Test script to diagnose scraping issues
"""
import sys
sys.path.insert(0, '.')

from app.scraper import WikipediaScraper

def test_url(url):
    print(f"\nTesting URL: {url}")
    print("=" * 60)
    
    scraper = WikipediaScraper()
    
    try:
        result = scraper.scrape_article(url)
        print("[SUCCESS] Scraping completed!")
        print(f"Title: {result['title']}")
        print(f"Summary length: {len(result['summary'])} chars")
        print(f"Sections: {len(result['sections'])} found")
        print(f"Content text length: {len(result['content_text'])} chars")
        print(f"Entities - People: {len(result['key_entities']['people'])}")
        print(f"Entities - Organizations: {len(result['key_entities']['organizations'])}")
        print(f"Entities - Locations: {len(result['key_entities']['locations'])}")
        
        if len(result['content_text']) < 100:
            print("\n[WARNING] Content text is very short. This might cause LLM issues.")
        
        return True
    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_urls = [
        "https://en.wikipedia.org/wiki/Barbie_doll",
        "https://en.wikipedia.org/wiki/Alan_Turing"
    ]
    
    for url in test_urls:
        test_url(url)
        print()
