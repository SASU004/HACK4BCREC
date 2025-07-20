import openai
import os

from dotenv import load_dotenv
load_dotenv()

# Try to get API key from config file first, then environment variable
try:
    from config import OPENAI_API_KEY as config_key
    api_key = config_key
except ImportError:
    api_key = os.getenv("OPENAI_API_KEY")

print(f"Teacher Bot - API Key found: {'Yes' if api_key else 'No'}")
print(f"Teacher Bot - API Key length: {len(api_key) if api_key else 0}")

if not api_key:
    print("❌ OpenAI API key not found. Please update config.py with your OPENAI_API_KEY.")
elif api_key == "your-api-key-here" or len(api_key) < 20:
    print("❌ Invalid OpenAI API key. Please check config.py and ensure you have a valid API key.")
else:
    openai.api_key = api_key



def load_transcript(file_path="transcript.txt"):
    """Load transcript from file with existence check and logging"""
    try:
        transcript_path = os.path.abspath(file_path)
        print(f"Attempting to load transcript from: {transcript_path}")
        
        if os.path.exists(transcript_path):
            file_size = os.path.getsize(transcript_path)
            print(f"Transcript file found. File size: {file_size} bytes")
            
            with open(transcript_path, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"Successfully loaded transcript. Content length: {len(content)} characters")
            return content
        else:
            print(f"Transcript file not found at: {transcript_path}")
            raise FileNotFoundError(f"Transcript file not found at: {transcript_path}")
    except Exception as e:
        print(f"Error loading transcript file: {str(e)}")
        raise

TEACHER_PROMPT_TEMPLATE = """
You are a friendly and patient teacher chatbot.

The following transcript is a detailed explanation of a topic extracted from a YouTube video:

--------------------TRANSCRIPT--------------------
{transcript}
--------------------------------------------------

Your job is to:
1. First explain the transcript content in simple, step-by-step way like you’re teaching a beginner.
2. If a question is asked, answer only based on the transcript, and make the answer very **clear, slow, beginner-friendly, and **beautifully explained.
3. If the answer is not in the transcript, politely say: "Sorry, that wasn't covered in the transcript."

Always assume the student knows nothing.

Now answer this question:
"{question}"
"""

def ask_teacher_bot(transcript, question, model="gpt-3.5-turbo"):
    # Try to get API key from config file first, then environment variable
    try:
        from config import OPENAI_API_KEY as config_key
        api_key = config_key
    except ImportError:
        api_key = os.getenv("OPENAI_API_KEY")
    
    print(f"Q&A - API Key found: {'Yes' if api_key else 'No'}")
    
    if not api_key:
        return "❌ OpenAI API key not found. Please update config.py with your OPENAI_API_KEY."
    
    if api_key == "your-api-key-here" or len(api_key) < 20:
        return "❌ Invalid OpenAI API key. Please check config.py and ensure you have a valid API key."
    
    prompt = TEACHER_PROMPT_TEMPLATE.format(transcript=transcript, question=question)

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error: {str(e)}"