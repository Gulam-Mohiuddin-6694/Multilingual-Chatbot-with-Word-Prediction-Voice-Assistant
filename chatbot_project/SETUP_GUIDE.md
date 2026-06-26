# Quick Setup Guide

## Automated Setup (Windows)

Simply double-click `start.bat` to automatically:
1. Install all dependencies
2. Download NLTK data
3. Start the server

## Manual Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download NLTK Data
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

### 3. Start Server
```bash
cd backend
python app.py
```

### 4. Open Browser
Navigate to: http://localhost:5000

## First Time Usage

1. **Wait for models to train** (takes ~5 seconds on first run)
2. **Select your language** from the dropdown
3. **Start typing** to see predictions
4. **Click predictions** to auto-complete
5. **Use voice button** for voice input (Chrome/Edge recommended)

## Features to Try

- Type "How are" and see predictions
- Click on predicted words
- Switch between English, Hindi, Telugu
- Use voice input (microphone button)
- Click "Speak Response" to hear bot's voice
- Clear chat to start fresh

## Troubleshooting

**Port already in use?**
- Edit `backend/app.py` line 145
- Change port from 5000 to another (e.g., 5001)

**Voice not working?**
- Use Chrome or Edge browser
- Allow microphone permissions

**Predictions not showing?**
- Wait for models to finish training
- Check console for errors

## Need Help?

Check README.md for detailed documentation.
