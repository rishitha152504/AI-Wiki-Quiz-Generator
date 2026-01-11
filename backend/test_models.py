"""
Test script to list available Gemini models
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key == "your_gemini_api_key_here":
    print("ERROR: GEMINI_API_KEY not set in .env file")
    exit(1)

genai.configure(api_key=api_key)

print("=" * 60)
print("Available Gemini Models")
print("=" * 60)

try:
    models = genai.list_models()
    print("\nModels that support generateContent:\n")
    
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            print(f"  - {model.name}")
            print(f"    Display Name: {model.display_name}")
            print(f"    Description: {model.description}")
            print()
    
    print("\n" + "=" * 60)
    print("Recommended model names to try:")
    print("=" * 60)
    
    # Common model name patterns
    model_patterns = [
        "gemini-pro",
        "gemini-1.5-pro",
        "gemini-1.5-flash",
        "models/gemini-pro",
        "models/gemini-1.5-pro",
        "models/gemini-1.5-flash",
    ]
    
    for pattern in model_patterns:
        # Check if any model matches
        matching = [m for m in models if pattern in m.name or pattern.replace('models/', '') in m.name]
        if matching:
            print(f"  [OK] {pattern} - Available")
        else:
            print(f"  [X] {pattern} - Not found")
    
except Exception as e:
    print(f"Error listing models: {e}")
    import traceback
    traceback.print_exc()
