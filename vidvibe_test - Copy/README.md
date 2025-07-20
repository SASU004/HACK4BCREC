# Vid Vibe - YouTube Video Learning Assistant

A Flask web application that transcribes YouTube videos, generates summaries, and allows users to ask questions about the content using AI.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up OpenAI API Key

**Option A: Update config.py (Recommended)**
1. Open `config.py` in the project root
2. Replace `"your-api-key-here"` with your actual OpenAI API key:
```python
OPENAI_API_KEY = "sk-your-actual-api-key-here"
```

**Option B: Create a .env file**
1. Create a file named `.env` in the project root
2. Add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**Option C: Set Environment Variable**
```bash
# Windows
set OPENAI_API_KEY=sk-your-actual-api-key-here

# macOS/Linux
export OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 3. Get Your OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and add it to your `.env` file

### 4. Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## Features

- **YouTube Video Transcription**: Extract transcripts from YouTube videos
- **AI-Powered Summaries**: Generate concise summaries using GPT-3.5
- **Audio Generation**: Convert summaries to speech
- **Interactive Q&A**: Ask questions about video content
- **Dark Mode**: Toggle between light and dark themes
- **Responsive Design**: Works on desktop and mobile devices

## Usage

1. **Generate Transcript**: Paste a YouTube URL and click "Generate Transcript"
2. **View Summary**: The AI will automatically generate a summary
3. **Listen to Audio**: Play the audio version of the summary
4. **Ask Questions**: Use the Q&A section to ask specific questions about the content

## Troubleshooting

### "OpenAI API key not found" Error
- Ensure you've updated `config.py` with your API key (recommended)
- Or ensure you've created a `.env` file with your API key
- Check that the API key is valid and has sufficient credits
- Restart the application after adding the API key

### "Failed to generate transcript" Error
- Verify the YouTube URL is valid
- Ensure the video has captions/subtitles enabled
- Check your internet connection

### "Failed to generate summary" Error
- Verify your OpenAI API key is correct
- Check your OpenAI account has sufficient credits
- Ensure the transcript was generated successfully

## File Structure

```
vidvibe/
├── app.py              # Main Flask application
├── config.py           # API key configuration (update this - recommended)
├── yt_transcribe.py    # YouTube transcription and summarization
├── teacher_bot.py      # AI Q&A functionality
├── generate_audio.py   # Text-to-speech generation
├── templates/          # HTML templates
├── static/            # CSS and JavaScript files
├── requirements.txt   # Python dependencies
└── .env              # Environment variables (optional)
```

## Dependencies

- Flask
- youtube-transcript-api
- openai
- python-dotenv
- gtts (Google Text-to-Speech)
- yt-dlp

## License

This project is for educational purposes. 