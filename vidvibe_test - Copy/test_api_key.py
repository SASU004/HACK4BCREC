#!/usr/bin/env python3
"""
Simple script to test if the OpenAI API key is properly configured.
Run this script to check if your .env file is working correctly.
"""

import os
from dotenv import load_dotenv

def test_api_key():
    print("🔍 Testing OpenAI API Key Configuration...")
    print("=" * 50)
    
    # Load .env file
    load_dotenv()
    
    # Try to get API key from multiple sources
    api_key = None
    
    # Try config.py first, then environment variable
    try:
        from config import OPENAI_API_KEY as config_key
        api_key = config_key
        print("✅ config.py loaded: Yes")
    except ImportError:
        api_key = os.getenv("OPENAI_API_KEY")
        print("✅ Config files loaded: No (using .env)")
    
    print(f"✅ API Key found: {'Yes' if api_key else 'No'}")
    
    if api_key:
        print(f"✅ API Key length: {len(api_key)} characters")
        print(f"✅ API Key starts with 'sk-': {'Yes' if api_key.startswith('sk-') else 'No'}")
        
        if api_key == "your-api-key-here":
            print("❌ ERROR: You're using the placeholder text. Replace 'your-api-key-here' with your actual API key.")
        elif len(api_key) < 20:
            print("❌ ERROR: API key seems too short. Valid OpenAI API keys are longer.")
        elif not api_key.startswith('sk-'):
            print("❌ ERROR: API key doesn't start with 'sk-'. This might not be a valid OpenAI API key.")
        else:
            print("✅ API Key looks valid!")
            
            # Test OpenAI connection
            try:
                import openai
                openai.api_key = api_key
                
                # Try a simple API call
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": "Hello! This is a test."}],
                    max_tokens=10
                )
                print("✅ OpenAI API connection successful!")
                print(f"✅ Response received: {response.choices[0].message.content}")
                
            except Exception as e:
                print(f"❌ OpenAI API test failed: {str(e)}")
                print("💡 This might be due to:")
                print("   - Invalid API key")
                print("   - No credits in your OpenAI account")
                print("   - Network connectivity issues")
    else:
        print("❌ ERROR: No API key found!")
        print("💡 To fix this:")
        print("   1. Open config.py in the project root")
        print("   2. Replace 'your-api-key-here' with your actual OpenAI API key")
        print("   3. Save the file and restart the application")
        print("   OR")
        print("   1. Create a file named '.env' in the project root")
        print("   2. Add this line to the file:")
        print("      OPENAI_API_KEY=your-actual-api-key-here")
        print("   3. Replace 'your-actual-api-key-here' with your real OpenAI API key")
        print("   4. Restart the application")

if __name__ == "__main__":
    test_api_key() 