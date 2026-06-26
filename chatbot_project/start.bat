@echo off
echo ========================================
echo Multilingual Chatbot - Quick Start
echo ========================================
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt

echo.
echo Step 2: Downloading NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

echo.
echo Step 3: Starting the server...
cd backend
python app.py

pause
