#!/usr/bin/env python3
"""
Setup script to help configure your OpenAI API key.
This script will help you set up your API key in config.py
"""

import os

def setup_api_key():
    print("🔧 OpenAI API Key Setup")
    print("=" * 40)
    
    # Check if config.py exists
    if not os.path.exists("config.py"):
        print("❌ config.py not found. Creating it...")
        with open("config.py", "w") as f:
            f.write('OPENAI_API_KEY = "your-api-key-here"\n')
    
    # Read current API key
    try:
        from config import OPENAI_API_KEY
        current_key = OPENAI_API_KEY
    except:
        current_key = "your-api-key-here"
    
    print(f"Current API key: {current_key}")
    
    if current_key == "your-api-key-here":
        print("\n💡 To set up your API key:")
        print("1. Open config.py in your editor")
        print("2. Replace 'your-api-key-here' with your actual OpenAI API key")
        print("3. Save the file")
        print("4. Run this script again to verify")
        
        # Ask if user wants to input the key directly
        print("\n🤔 Would you like to enter your API key now? (y/n): ", end="")
        try:
            response = input().lower().strip()
            if response in ['y', 'yes']:
                print("Enter your OpenAI API key: ", end="")
                new_key = input().strip()
                
                if new_key and new_key != "your-api-key-here":
                    # Update the file
                    with open("config.py", "w") as f:
                        f.write(f'OPENAI_API_KEY = "{new_key}"\n')
                    print("✅ API key updated successfully!")
                    
                    # Test the key
                    print("\n🧪 Testing API key...")
                    try:
                        from config import OPENAI_API_KEY
                        print(f"✅ API key loaded: {OPENAI_API_KEY[:10]}...")
                        print(f"✅ Length: {len(OPENAI_API_KEY)} characters")
                        if OPENAI_API_KEY.startswith("sk-"):
                            print("✅ Format looks correct (starts with 'sk-')")
                        else:
                            print("⚠️  Warning: API key doesn't start with 'sk-'")
                    except Exception as e:
                        print(f"❌ Error loading API key: {e}")
                else:
                    print("❌ Invalid API key. Please try again.")
            else:
                print("📝 Please manually update config.py with your API key.")
        except KeyboardInterrupt:
            print("\n\n📝 Please manually update config.py with your API key.")
    else:
        print("✅ API key is already configured!")
        print(f"✅ Length: {len(current_key)} characters")
        if current_key.startswith("sk-"):
            print("✅ Format looks correct (starts with 'sk-')")
        else:
            print("⚠️  Warning: API key doesn't start with 'sk-'")

if __name__ == "__main__":
    setup_api_key() 