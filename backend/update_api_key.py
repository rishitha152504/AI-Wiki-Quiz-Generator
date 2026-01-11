"""
Helper script to update Gemini API key in .env file
"""
import os
import sys

def update_api_key():
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    
    if not os.path.exists(env_path):
        print("ERROR: .env file not found!")
        print("Please run: python create_env.py first")
        return False
    
    # Read current .env
    with open(env_path, 'r') as f:
        content = f.read()
    
    # Check if already has a real key
    if "GEMINI_API_KEY=your_gemini_api_key_here" not in content:
        print("API key already configured in .env file.")
        response = input("Do you want to update it? (y/n): ")
        if response.lower() != 'y':
            print("Cancelled.")
            return False
    
    print("\n" + "="*60)
    print("Gemini API Key Setup")
    print("="*60)
    print("\n1. Get your free API key from:")
    print("   https://makersuite.google.com/app/apikey")
    print("\n2. Sign in with Google account")
    print("3. Click 'Create API Key'")
    print("4. Copy the key (starts with AIzaSy...)\n")
    
    api_key = input("Paste your API key here: ").strip()
    
    if not api_key:
        print("ERROR: No API key provided!")
        return False
    
    if not api_key.startswith("AIzaSy"):
        print("WARNING: API key should start with 'AIzaSy'")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return False
    
    # Update .env file
    updated_content = content.replace(
        "GEMINI_API_KEY=your_gemini_api_key_here",
        f"GEMINI_API_KEY={api_key}"
    )
    
    if "GEMINI_API_KEY=" in content and "GEMINI_API_KEY=your_gemini_api_key_here" not in content:
        # Replace existing key
        import re
        updated_content = re.sub(
            r'GEMINI_API_KEY=.*',
            f'GEMINI_API_KEY={api_key}',
            content
        )
    
    with open(env_path, 'w') as f:
        f.write(updated_content)
    
    print("\n[SUCCESS] API key updated in .env file!")
    print("\nNext steps:")
    print("1. Restart your backend server (Ctrl+C then python run.py)")
    print("2. Try generating a quiz again!")
    print("\n" + "="*60)
    
    return True

if __name__ == "__main__":
    try:
        update_api_key()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
    except Exception as e:
        print(f"\nERROR: {e}")
