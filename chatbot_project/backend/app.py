from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.prediction_engine import WordPredictionEngine
from backend.chatbot_engine import ChatbotEngine
from backend.language_module import LanguageModule
from backend.voice_module import VoiceModule
from utils.dataset_loader import DatasetLoader

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Initialize modules
prediction_engines = {}
chatbot_engines = {}
language_module = LanguageModule()
voice_module = VoiceModule()
dataset_loader = DatasetLoader()

# Global state
current_language = 'english'
chat_history = []

# Load and train models
def initialize_models():
    """Initialize and train all models"""
    print("Loading datasets...")
    datasets = dataset_loader.load_default_data()
    
    print("Training prediction models...")
    # Train for each language
    for lang, data in datasets.items():
        print(f"  Training {lang} model with {len(data)} sentences...")
        
        # Create prediction engine for this language
        pred_engine = WordPredictionEngine()
        pred_engine.train(data)
        prediction_engines[lang] = pred_engine
        
        # Create chatbot engine for this language
        chat_engine = ChatbotEngine()
        chat_engine.train(data)
        chatbot_engines[lang] = chat_engine
    
    print("Models initialized successfully!")

# Initialize on startup
initialize_models()

@app.route('/')
def index():
    """Serve main page"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict next words"""
    try:
        data = request.json
        text = data.get('text', '')
        language = data.get('language', 'english')
        
        if not text:
            return jsonify({'predictions': [], 'sequences': []})
        
        # Get the prediction engine for this language
        pred_engine = prediction_engines.get(language, prediction_engines.get('english'))
        
        # Get predictions
        predictions = pred_engine.predict_next_words(text, top_k=5)
        sequences = pred_engine.predict_sequences(text, top_k=3)
        
        return jsonify({
            'predictions': predictions,
            'sequences': sequences
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """Generate chatbot response"""
    try:
        data = request.json
        user_message = data.get('message', '')
        language = data.get('language', 'english')
        
        if not user_message:
            return jsonify({'response': 'Please say something!'})
        
        # Get the chatbot engine for this language
        chat_engine = chatbot_engines.get(language, chatbot_engines.get('english'))
        
        # Generate response
        response = chat_engine.generate_response(user_message)
        
        # Store in history
        chat_history.append({
            'user': user_message,
            'bot': response
        })
        
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/voice-to-text', methods=['POST'])
def voice_to_text():
    """Convert voice to text using local microphone"""
    try:
        data = request.json
        language = data.get('language', 'english') if data else 'english'
        
        # Listen directly from the microphone using the backend voice module
        text = voice_module.listen_from_microphone(language)
        
        # Handle known errors
        if isinstance(text, str) and (text.startswith("Error:") or text.startswith("Could not")):
            return jsonify({'error': text}), 400
            
        return jsonify({
            'text': text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    """Convert text to speech"""
    try:
        data = request.json
        text = data.get('text', '')
        language = data.get('language', 'english')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Generate speech
        audio_path = voice_module.text_to_speech(text, language)
        
        if audio_path and os.path.exists(audio_path):
            return send_file(audio_path, mimetype='audio/mpeg')
        else:
            return jsonify({'error': 'Could not generate speech'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/change-language', methods=['POST'])
def change_language():
    """Change current language"""
    try:
        data = request.json
        language = data.get('language', 'english')
        
        global current_language
        current_language = language
        language_module.set_language(language)
        
        return jsonify({'success': True, 'language': language})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear chat history"""
    try:
        global chat_history
        chat_history = []
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get-history', methods=['GET'])
def get_history():
    """Get chat history"""
    try:
        return jsonify({'history': chat_history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Multilingual Chatbot Server...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
