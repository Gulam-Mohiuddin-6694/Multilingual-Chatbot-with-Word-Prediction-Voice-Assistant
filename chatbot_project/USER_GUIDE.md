# User Guide - Multilingual Word Prediction Chatbot

## Table of Contents
1. [Getting Started](#getting-started)
2. [Features Overview](#features-overview)
3. [How to Use](#how-to-use)
4. [Tips & Tricks](#tips--tricks)
5. [FAQ](#faq)

## Getting Started

### Installation (First Time Only)

**Option 1: Automated (Windows)**
1. Double-click `start.bat`
2. Wait for installation to complete
3. Browser will open automatically

**Option 2: Manual**
```bash
# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

# Start server
cd backend
python app.py
```

### Running the Application

1. Open terminal/command prompt
2. Navigate to `chatbot_project/backend`
3. Run: `python app.py`
4. Open browser: `http://localhost:5000`

## Features Overview

### 1. Word Prediction
- **Real-time predictions** as you type
- **Top 5 word suggestions** for next word
- **Top 3 phrase suggestions** for complete sentences
- **Click to auto-complete** any prediction

### 2. Chatbot Conversation
- **Intelligent responses** based on context
- **Pattern matching** for common queries
- **Similarity-based** responses for complex questions
- **Maintains context** during conversation

### 3. Multilingual Support
- **3 Languages**: English, Hindi, Telugu
- **Auto-translation** between languages
- **Language detection** for input
- **Seamless switching** between languages

### 4. Voice Assistant
- **Voice Input**: Speak your message
- **Voice Output**: Hear bot responses
- **Multi-language voice** support
- **Browser-based** speech recognition

### 5. Interactive UI
- **Clean design** with gradient background
- **Real-time updates** for predictions
- **Chat history** display
- **Responsive layout** for all devices

## How to Use

### Basic Chat

1. **Type your message** in the input box
2. **Press Enter** or click "Send"
3. **View bot response** in chat window
4. **Continue conversation** naturally

Example:
```
You: Hello
Bot: Hello! How can I help you?

You: Tell me about AI
Bot: Artificial Intelligence is fascinating!
```

### Using Word Predictions

1. **Start typing** any message
2. **Watch predictions appear** in orange panel
3. **Click a word** to append it to your input
4. **Click a phrase** to replace entire input
5. **Continue typing** or send message

Example Flow:
```
Type: "How are"
Predictions show: [you] [they] [things]
Click: "you"
Input becomes: "How are you"
```

### Language Selection

1. **Click language dropdown** at top
2. **Select language**: English / Hindi / Telugu
3. **All interactions** switch to that language
4. **Predictions and responses** in selected language

### Voice Input

1. **Click microphone button** (red button)
2. **Allow microphone access** (first time)
3. **Speak your message** clearly
4. **Text appears** in input box
5. **Click Send** to submit

Tips for voice input:
- Speak clearly and at normal pace
- Use Chrome or Edge browser
- Ensure microphone is working
- Minimize background noise

### Voice Output

1. **Receive a bot response**
2. **Click "Speak Response"** button
3. **Listen to voice output**
4. **Adjust volume** as needed

### Clearing Chat

1. **Click "Clear Chat"** button
2. **Confirm** the action
3. **Chat resets** to initial state
4. **History is cleared**

## Tips & Tricks

### Getting Better Predictions

1. **Type more context**: "I am going to" gives better predictions than "I"
2. **Use complete words**: Predictions work on full words
3. **Try different phrases**: Experiment with various inputs
4. **Check suggested phrases**: Often more accurate than single words

### Chatbot Interaction

1. **Ask clear questions**: "What is AI?" works better than "AI?"
2. **Use keywords**: Include important words in your query
3. **Try variations**: Rephrase if response isn't helpful
4. **Be conversational**: Natural language works best

### Voice Features

1. **Speak naturally**: No need to speak slowly
2. **Pause before clicking**: Wait a moment after speaking
3. **Check language setting**: Match voice language to selected language
4. **Use headphones**: Better audio quality for voice output

### Multilingual Usage

1. **Switch languages anytime**: No need to restart
2. **Mix languages**: Bot will try to understand
3. **Use native script**: Type in Hindi/Telugu script if possible
4. **Translation quality**: English generally gives best results

## FAQ

### Q: Predictions not showing?
**A:** Wait 2-3 seconds after typing. Models need time to process.

### Q: Voice input not working?
**A:** 
- Use Chrome or Edge browser
- Allow microphone permissions
- Check microphone is connected and working
- Try refreshing the page

### Q: Bot gives generic responses?
**A:** 
- Try rephrasing your question
- Add more context to your message
- Use keywords related to your topic
- Check if language is set correctly

### Q: How to improve prediction accuracy?
**A:** 
- Type more words for better context
- Use common phrases and expressions
- Wait for model to fully train (first run)
- Add more training data to datasets

### Q: Can I add my own training data?
**A:** Yes! Add sentences to `dataset/english_data.csv` and restart server.

### Q: Port 5000 already in use?
**A:** Edit `backend/app.py` line 145, change port to 5001 or another.

### Q: How to stop the server?
**A:** Press `Ctrl+C` in the terminal where server is running.

### Q: Can I use this offline?
**A:** Partially. Translation and some voice features need internet.

### Q: How to update the application?
**A:** 
1. Stop the server
2. Update files
3. Restart server
4. Refresh browser

### Q: Where is chat history saved?
**A:** Currently in memory only. Clears when server restarts.

### Q: Can I customize the UI?
**A:** Yes! Edit `frontend/style.css` for styling changes.

## Keyboard Shortcuts

- **Enter**: Send message
- **Ctrl+L**: Focus on input box (browser default)
- **Ctrl+R**: Refresh page (browser default)

## Best Practices

1. **Start simple**: Begin with basic phrases
2. **Explore features**: Try all buttons and options
3. **Experiment**: Test different languages and inputs
4. **Provide feedback**: Note what works and what doesn't
5. **Be patient**: AI needs time to process complex queries

## Support

For issues or questions:
1. Check this guide first
2. Review README.md for technical details
3. Check console for error messages
4. Verify all dependencies are installed

## Advanced Usage

### Custom Training Data
Add your own sentences to:
- `dataset/english_data.csv`
- Create `dataset/hindi_data.csv`
- Create `dataset/telugu_data.csv`

Format: One sentence per line

### API Integration
Use the REST API endpoints:
- `/predict` - Get predictions
- `/chat` - Get responses
- `/change-language` - Switch language

See README.md for API documentation.

---

**Enjoy using the Multilingual Chatbot! 🤖**
