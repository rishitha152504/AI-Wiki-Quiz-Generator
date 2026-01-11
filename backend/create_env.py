"""
Script to create .env file for the application
"""
import os

env_content = """# Database Configuration
# For SQLite (default - no setup required):
# Leave DATABASE_URL empty or unset

# For PostgreSQL (production):
# DATABASE_URL=postgresql://username:password@localhost:5432/wiki_quiz_db

# Gemini API Key (Required)
# Get your free API key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your_gemini_api_key_here
"""

env_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(env_path):
    print(".env file already exists!")
    response = input("Do you want to overwrite it? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled. .env file not modified.")
        exit(0)

with open(env_path, 'w') as f:
    f.write(env_content)

print("[SUCCESS] .env file created successfully!")
print("\n[IMPORTANT] Please edit .env and add your Gemini API key:")
print("   1. Get your free API key from: https://makersuite.google.com/app/apikey")
print("   2. Open backend/.env file")
print("   3. Replace 'your_gemini_api_key_here' with your actual API key")
print("\n[NOTE] Using SQLite database (no PostgreSQL setup required)")
