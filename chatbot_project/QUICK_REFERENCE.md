# Quick Reference Card

## 🚀 Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

# Run application
cd backend
python app.py

# Run tests
python test_system.py

# Run demo
python demo.py
```

## 📂 File Structure

```
backend/
  app.py              - Main Flask application
  prediction_engine.py - Word prediction (N-gram)
  chatbot_engine.py   - Response generation
  language_module.py  - Translation & detection
  voice_module.py     - Speech recognition/synthesis

frontend/
  index.html          - UI structure
  style.css           - Styling
  script.js           - Frontend logic

utils/
  preprocessing.py    - Text preprocessing
  dataset_loader.py   - Dataset management
```

## 🔌 API Endpoints

```
POST /predict          - Get word predictions
POST /chat             - Get chatbot response
POST /text-to-speech   - Convert text to speech
POST /change-language  - Switch language
POST /clear-history    - Clear chat history
GET  /get-history      - Get chat history
```

## 💻 Code Examples

### Prediction Engine
```python
from backend.prediction_engine import WordPredictionEngine

engine = WordPredictionEngine()
engine.train(sentences)
predictions = engine.predict_next_words("how are", top_k=5)
sequences = engine.predict_sequences("how are", top_k=3)
```

### Chatbot Engine
```python
from backend.chatbot_engine import ChatbotEngine

engine = ChatbotEngine()
engine.train(conversations)
response = engine.generate_response("Hello")
```

### Language Module
```python
from backend.language_module import LanguageModule

module = LanguageModule()
lang = module.detect_language("Hello")
translated = module.translate("Hello", "hindi")
```

## 🎨 UI Components

```javascript
// Send message
sendMessage()

// Handle predictions
handleInputChange()

// Voice input
startVoiceInput()

// Speak response
speakLastResponse()

// Change language
changeLanguage()
```

## 🔧 Configuration

Edit `config.json`:
```json
{
  "server": {"port": 5000},
  "prediction": {"top_k_words": 5},
  "languages": {"default": "english"}
}
```

## 📊 Key Classes

| Class | Purpose | Location |
|-------|---------|----------|
| WordPredictionEngine | N-gram predictions | prediction_engine.py |
| ChatbotEngine | Response generation | chatbot_engine.py |
| LanguageModule | Translation | language_module.py |
| VoiceModule | Speech I/O | voice_module.py |
| TextPreprocessor | Text cleaning | preprocessing.py |
| DatasetLoader | Data loading | dataset_loader.py |

## 🌐 Supported Languages

| Language | Code | Voice Support |
|----------|------|---------------|
| English  | en   | ✅ |
| Hindi    | hi   | ✅ |
| Telugu   | te   | ✅ |

## 🎯 Common Tasks

### Add Training Data
1. Edit `dataset/english_data.csv`
2. Add sentences (one per line)
3. Restart server

### Change Port
1. Edit `backend/app.py`
2. Change line: `app.run(port=5000)`
3. Restart server

### Customize UI
1. Edit `frontend/style.css` for colors
2. Edit `frontend/index.html` for layout
3. Refresh browser

### Add New Language
1. Add to `language_module.py`
2. Add dataset file
3. Update UI dropdown

## 🐛 Debugging

```python
# Enable debug mode
app.run(debug=True)

# Check logs
print(f"Predictions: {predictions}")

# Test components
python test_system.py
```

## 📦 Dependencies

```
flask          - Web framework
nltk           - NLP toolkit
scikit-learn   - ML library
googletrans    - Translation
gTTS           - Text-to-speech
SpeechRecognition - Voice input
```

## ⚡ Performance Tips

- Use caching for predictions
- Debounce input (300ms)
- Lazy load models
- Optimize dataset size
- Use CDN for frontend libraries

## 🔒 Security Notes

- Sanitize user input
- Validate API requests
- Use HTTPS in production
- Rate limit API calls
- Secure API keys

## 📱 Browser Support

| Browser | Version | Voice Support |
|---------|---------|---------------|
| Chrome  | 90+     | ✅ Full |
| Edge    | 90+     | ✅ Full |
| Firefox | 88+     | ⚠️ Limited |
| Safari  | 14+     | ⚠️ Limited |

## 🎓 Learning Resources

- NLTK Documentation: https://www.nltk.org/
- Flask Documentation: https://flask.palletsprojects.com/
- Web Speech API: https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API

## 📞 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port in use | Change port in app.py |
| NLTK data missing | Run nltk.download() |
| Voice not working | Use Chrome/Edge |
| Import errors | pip install -r requirements.txt |

## 🎉 Quick Test

```bash
# Test prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"how are","language":"english"}'

# Test chat
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello","language":"english"}'
```

## 📝 Notes

- Models train on first run (~5 seconds)
- Voice requires microphone permissions
- Translation needs internet connection
- Chat history clears on server restart

---

**Keep this card handy for quick reference! 📌**
