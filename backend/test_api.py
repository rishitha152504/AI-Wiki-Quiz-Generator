"""
Simple script to test the API endpoints
Run this after starting the backend server
"""
import requests
import json
import time

API_BASE_URL = "http://localhost:8000"

def test_root():
    """Test root endpoint"""
    print("Testing root endpoint...")
    response = requests.get(f"{API_BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")

def test_generate_quiz(url):
    """Test quiz generation"""
    print(f"Testing quiz generation for: {url}")
    print("This may take 30-60 seconds...")
    
    response = requests.post(
        f"{API_BASE_URL}/api/quiz/generate",
        json={"url": url}
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        data = response.json()
        print(f"Article ID: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Quiz Questions: {len(data['quiz'])}")
        print(f"Related Topics: {len(data['related_topics'])}")
        return data['id']
    else:
        print(f"Error: {response.json()}")
        return None

def test_history():
    """Test history endpoint"""
    print("\nTesting history endpoint...")
    response = requests.get(f"{API_BASE_URL}/api/quiz/history")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        articles = response.json()
        print(f"Total articles: {len(articles)}")
        for article in articles[:3]:  # Show first 3
            print(f"  - {article['id']}: {article['title']}")

def test_get_quiz(article_id):
    """Test get quiz by ID"""
    print(f"\nTesting get quiz by ID: {article_id}")
    response = requests.get(f"{API_BASE_URL}/api/quiz/{article_id}")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Title: {data['title']}")
        print(f"Questions: {len(data['quiz'])}")

if __name__ == "__main__":
    print("=" * 50)
    print("Wiki Quiz API Test Script")
    print("=" * 50)
    
    # Test root
    try:
        test_root()
    except Exception as e:
        print(f"Error connecting to API: {e}")
        print("Make sure the backend server is running on port 8000")
        exit(1)
    
    # Test quiz generation
    test_url = "https://en.wikipedia.org/wiki/Alan_Turing"
    article_id = test_generate_quiz(test_url)
    
    if article_id:
        # Wait a bit for processing
        time.sleep(2)
        
        # Test history
        test_history()
        
        # Test get quiz
        test_get_quiz(article_id)
    
    print("\n" + "=" * 50)
    print("Testing complete!")
    print("=" * 50)
