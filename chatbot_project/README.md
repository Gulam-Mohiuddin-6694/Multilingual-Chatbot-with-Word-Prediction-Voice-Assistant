<<<<<<< HEAD
=======
# Multilingual Word Prediction Chatbot with Voice Assistant

A fully functional NLP-based chatbot web application that predicts the next sequence of words and generates relevant responses with multilingual support and voice assistant capabilities.

## Features

- **Word Prediction**: Predicts next possible words and phrases using N-gram language model
- **Chatbot Response Generation**: Generates intelligent responses using NLP techniques
- **Multilingual Support**: Supports English, Hindi, and Telugu languages
- **Voice Assistant**: Voice input and output capabilities
- **Interactive UI**: Clean, modern web interface with real-time predictions
- **Auto-complete**: Click predictions to auto-fill input
- **Chat History**: Maintains conversation history during session

## Technology Stack

### Backend
- Python 3.8+
- Flask (Web Framework)
- NLTK (Natural Language Processing)
- scikit-learn (Machine Learning)
- googletrans (Translation)
- gTTS (Text-to-Speech)
- SpeechRecognition (Voice Input)

### Frontend
- HTML5
- CSS3
- JavaScript (ES6+)
- Bootstrap 5
- Font Awesome Icons

## Project Structure

```
chatbot_project/
│
├── dataset/                    # Training datasets
│
├── models/                     # Trained models
│   └── word_prediction_model.pkl
│
├── backend/                    # Backend modules
│   ├── app.py                 # Main Flask application
│   ├── prediction_engine.py   # Word prediction engine
│   ├── chatbot_engine.py      # Chatbot response generator
│   ├── voice_module.py        # Voice assistant module
│   └── language_module.py     # Multilingual support
│
├── frontend/                   # Frontend files
│   ├── index.html             # Main UI
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic
│
├── utils/                      # Utility modules
│   ├── preprocessing.py       # Text preprocessing
│   └── dataset_loader.py      # Dataset management
│
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Edge, Firefox)

### Setup Steps

1. **Navigate to project directory**
```bash
cd chatbot_project
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
```

3. **Activate virtual environment**

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Download NLTK data**
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

## Running the Application

1. **Start the Flask server**
```bash
cd backend
python app.py
```

2. **Open your browser**
Navigate to: `http://localhost:5000`

3. **Start chatting!**
- Type messages or use voice input
- See real-time word predictions
- Switch between languages
- Click predictions to auto-complete

## Usage Guide

### Text Input
1. Type your message in the input box
2. See predictions appear in real-time
3. Click on predicted words to add them
4. Click on suggested phrases to replace input
5. Press Enter or click Send

### Voice Input
1. Click the microphone button
2. Speak your message
3. The text will appear in the input box
4. Send the message

### Voice Output
1. After receiving a bot response
2. Click "Speak Response" button
3. Listen to the bot's voice response

### Language Selection
1. Use the language dropdown
2. Select English, Hindi, or Telugu
3. All interactions will be in selected language

### Predictions
- **Next Words**: Individual word predictions
- **Suggested Phrases**: Complete phrase predictions
- Click any prediction to use it

## API Endpoints

### POST /predict
Predict next words for given text
```json
Request:
{
  "text": "How are",
  "language": "english"
}

Response:
{
  "predictions": ["you", "they", "things"],
  "sequences": ["How are you", "How are they", "How are things"]
}
```

### POST /chat
Generate chatbot response
```json
Request:
{
  "message": "Hello",
  "language": "english"
}

Response:
{
  "response": "Hello! How can I help you?"
}
```

### POST /change-language
Change current language
```json
Request:
{
  "language": "hindi"
}

Response:
{
  "success": true,
  "language": "hindi"
}
```

### POST /clear-history
Clear chat history
```json
Response:
{
  "success": true
}
```

## Model Details

### Word Prediction Engine
- **Algorithm**: N-gram Language Model (Bigram)
- **Training**: Trained on conversational datasets
- **Output**: Top 5 word predictions, Top 3 phrase predictions

### Chatbot Engine
- **Approach**: Hybrid (Pattern matching + TF-IDF similarity)
- **Features**: Context-aware responses
- **Fallback**: Default responses for unknown inputs

### Multilingual Support
- **Translation**: Google Translate API
- **Language Detection**: langdetect library
- **Supported Languages**: English, Hindi, Telugu

## Performance Optimization

- **Caching**: Prediction results cached
- **Debouncing**: Input predictions debounced (300ms)
- **Lazy Loading**: Models loaded on startup
- **Efficient Tokenization**: Optimized preprocessing pipeline

## Browser Compatibility

- Chrome 90+ (Recommended)
- Edge 90+
- Firefox 88+
- Safari 14+

**Note**: Voice features work best in Chrome and Edge

## Troubleshooting

### Issue: Module not found
**Solution**: Install all dependencies
```bash
pip install -r requirements.txt
```

### Issue: NLTK data not found
**Solution**: Download NLTK data
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### Issue: Voice input not working
**Solution**: 
- Use Chrome or Edge browser
- Allow microphone permissions
- Check microphone is connected

### Issue: Port 5000 already in use
**Solution**: Change port in app.py
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## Future Enhancements

- [ ] Transformer-based prediction models
- [ ] More languages support
- [ ] User authentication
- [ ] Persistent chat history
- [ ] Advanced voice commands
- [ ] Mobile app version
- [ ] Custom model training interface

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open-source and available under the MIT License.

## Contact

For questions or support, please open an issue in the repository.

## Acknowledgments

- NLTK for NLP tools
- Flask for web framework
- Google Translate for translation services
- Bootstrap for UI components
- Font Awesome for icons

---

**Built with ❤️ using Python, Flask, and NLP**
>>>>>>> 674e431 (first commit)
# Multilingual-Chatbot-with-Word-Prediction-Voice-Assistant-NLP-
