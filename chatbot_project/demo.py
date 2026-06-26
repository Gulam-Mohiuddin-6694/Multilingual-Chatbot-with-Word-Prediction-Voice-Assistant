"""
Demo Script - Multilingual Chatbot
This script demonstrates the chatbot's capabilities
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.prediction_engine import WordPredictionEngine
from backend.chatbot_engine import ChatbotEngine
from backend.language_module import LanguageModule
from utils.dataset_loader import DatasetLoader

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_section(text):
    """Print formatted section"""
    print(f"\n--- {text} ---")

def demo_prediction():
    """Demo word prediction"""
    print_header("WORD PREDICTION DEMO")
    
    # Initialize
    engine = WordPredictionEngine()
    loader = DatasetLoader()
    datasets = loader.load_default_data()
    
    print("\n📚 Training prediction model...")
    engine.train(datasets['english'])
    print("✓ Model trained!")
    
    # Test predictions
    test_inputs = [
        "how are",
        "i am",
        "what is",
        "tell me"
    ]
    
    for text in test_inputs:
        print_section(f"Input: '{text}'")
        
        # Get predictions
        words = engine.predict_next_words(text, top_k=5)
        sequences = engine.predict_sequences(text, top_k=3)
        
        print(f"Next Words: {', '.join(words)}")
        print(f"Sequences:")
        for seq in sequences:
            print(f"  • {seq}")

def demo_chatbot():
    """Demo chatbot responses"""
    print_header("CHATBOT CONVERSATION DEMO")
    
    # Initialize
    engine = ChatbotEngine()
    loader = DatasetLoader()
    datasets = loader.load_default_data()
    
    print("\n🤖 Training chatbot...")
    engine.train(datasets['english'])
    print("✓ Chatbot ready!")
    
    # Test conversations
    test_messages = [
        "Hello",
        "How are you?",
        "What is your name?",
        "Tell me about AI",
        "Thank you",
        "Goodbye"
    ]
    
    print_section("Conversation")
    for message in test_messages:
        response = engine.generate_response(message)
        print(f"\nYou: {message}")
        print(f"Bot: {response}")

def demo_language():
    """Demo language features"""
    print_header("MULTILINGUAL SUPPORT DEMO")
    
    # Initialize
    module = LanguageModule()
    
    print_section("Language Detection")
    
    test_texts = [
        ("Hello, how are you?", "english"),
        ("नमस्ते, आप कैसे हैं?", "hindi"),
        ("నమస్కారం, మీరు ఎలా ఉన్నారు?", "telugu")
    ]
    
    for text, expected in test_texts:
        detected = module.detect_language(text)
        print(f"\nText: {text}")
        print(f"Detected: {detected}")
        print(f"Expected: {expected}")
        print(f"✓ Correct!" if detected == expected else "⚠ Different")

def demo_full_workflow():
    """Demo complete workflow"""
    print_header("COMPLETE WORKFLOW DEMO")
    
    # Initialize all components
    pred_engine = WordPredictionEngine()
    chat_engine = ChatbotEngine()
    lang_module = LanguageModule()
    loader = DatasetLoader()
    
    print("\n🔧 Initializing system...")
    datasets = loader.load_default_data()
    pred_engine.train(datasets['english'])
    chat_engine.train(datasets['english'])
    print("✓ System ready!")
    
    print_section("User Interaction Flow")
    
    # Simulate user typing
    user_input = "how are"
    print(f"\n1. User types: '{user_input}'")
    
    # Get predictions
    predictions = pred_engine.predict_next_words(user_input, top_k=3)
    print(f"2. Predictions shown: {predictions}")
    
    # User completes message
    complete_message = "how are you"
    print(f"3. User completes: '{complete_message}'")
    
    # Get response
    response = chat_engine.generate_response(complete_message)
    print(f"4. Bot responds: '{response}'")
    
    # Language switch
    print(f"\n5. User switches to Hindi")
    lang_module.set_language('hindi')
    print(f"   Current language: {lang_module.current_language}")

def show_statistics():
    """Show project statistics"""
    print_header("PROJECT STATISTICS")
    
    loader = DatasetLoader()
    datasets = loader.load_default_data()
    
    print("\n📊 Dataset Statistics:")
    for lang, data in datasets.items():
        print(f"  {lang.capitalize()}: {len(data)} sentences")
    
    print("\n🎯 Features:")
    features = [
        "Word Prediction",
        "Chatbot Responses",
        "Multilingual Support (3 languages)",
        "Voice Input/Output",
        "Real-time Predictions",
        "Interactive UI",
        "REST API"
    ]
    for feature in features:
        print(f"  ✓ {feature}")
    
    print("\n🛠️ Technologies:")
    technologies = [
        "Python 3.8+",
        "Flask",
        "NLTK",
        "scikit-learn",
        "HTML/CSS/JavaScript",
        "Bootstrap 5"
    ]
    for tech in technologies:
        print(f"  • {tech}")

def main():
    """Run all demos"""
    print("\n" + "🤖 "*20)
    print("  MULTILINGUAL WORD PREDICTION CHATBOT")
    print("  Interactive Demo")
    print("🤖 "*20)
    
    try:
        # Run demos
        demo_prediction()
        demo_chatbot()
        demo_language()
        demo_full_workflow()
        show_statistics()
        
        print_header("DEMO COMPLETE")
        print("\n✅ All features demonstrated successfully!")
        print("\n🚀 To run the web application:")
        print("   cd backend")
        print("   python app.py")
        print("\n📖 For more information, see README.md")
        
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        print("Please ensure all dependencies are installed:")
        print("  pip install -r requirements.txt")

if __name__ == "__main__":
    main()
