"""
Simple script to test backend connection
Run this to verify your backend is accessible
"""
import requests
import sys

def test_backend():
    """Test if backend is running and accessible"""
    try:
        print("Testing backend connection...")
        print("=" * 50)
        
        # Test health endpoint
        health_url = "http://localhost:8000/api/health"
        print(f"1. Testing health endpoint: {health_url}")
        response = requests.get(health_url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ SUCCESS: {data.get('message', 'Backend is healthy')}")
        else:
            print(f"   ❌ FAILED: Status code {response.status_code}")
            return False
        
        # Test root endpoint
        root_url = "http://localhost:8000/"
        print(f"\n2. Testing root endpoint: {root_url}")
        response = requests.get(root_url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ SUCCESS: {data.get('message', 'API is running')}")
        else:
            print(f"   ❌ FAILED: Status code {response.status_code}")
            return False
        
        # Test CORS (simulate frontend request)
        print(f"\n3. Testing CORS configuration...")
        response = requests.options(
            "http://localhost:8000/api/health",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "GET"
            },
            timeout=5
        )
        
        if response.status_code in [200, 204]:
            print(f"   ✅ SUCCESS: CORS is configured correctly")
        else:
            print(f"   ⚠️  WARNING: CORS might not be configured (status: {response.status_code})")
        
        print("\n" + "=" * 50)
        print("✅ All tests passed! Backend is ready to accept connections.")
        print("\nNext steps:")
        print("  1. Start frontend: cd frontend && npm start")
        print("  2. Open browser: http://localhost:3000")
        print("  3. Check browser console for connection status")
        return True
        
    except requests.exceptions.ConnectionError:
        print("\n" + "=" * 50)
        print("❌ ERROR: Cannot connect to backend!")
        print("\nPossible issues:")
        print("  1. Backend is not running")
        print("  2. Backend is running on a different port")
        print("  3. Firewall is blocking the connection")
        print("\nSolution:")
        print("  1. Start backend: cd backend && python run.py")
        print("  2. Wait for: 'Uvicorn running on http://0.0.0.0:8000'")
        print("  3. Run this test again")
        return False
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_backend()
    sys.exit(0 if success else 1)
