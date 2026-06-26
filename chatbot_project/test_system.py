"""
Test script to verify all components of the chatbot system
"""
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    try:
        from backend.prediction_engine import WordPredictionEngine
        from backend.chatbot_engine import ChatbotEngine
        from backend.language_module import LanguageModule
        from utils.dataset_loader import DatasetLoader
        from utils.preprocessing import TextPreprocessor
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import error: {e}")
        return False

def test_dataset_loader():
    """Test dataset loading"""
    print("\nTesting dataset loader...")
    try:
        from utils.dataset_loader import DatasetLoader
        loader = DatasetLoader()
        datasets = loader.load_default_data()
        
        assert 'english' in datasets
        assert 'hindi' in datasets
        assert 'telugu' in datasets
        assert len(datasets['english']) > 0
        
        print(f"✓ Dataset loaded: {len(datasets['english'])} English sentences")
        return True
    except Exception as e:
        print(f"✗ Dataset loader error: {e}")
        return False

def test_preprocessing():
    """Test text preprocessing"""
    print("\nTesting preprocessing...")
    try:
        from utils.preprocessing import TextPreprocessor
        preprocessor = TextPreprocessor()
        
        text = "Hello, how are you doing today?"
        tokens = preprocessor.preprocess(text)
        
        assert len(tokens) > 0
        print(f"✓ Preprocessing works: '{text}' -> {tokens}")
        return True
    except Exception as e:
        print(f"✗ Preprocessing error: {e}")
        return False

def test_prediction_engine():
    """Test word prediction engine"""
    print("\nTesting prediction engine...")
    try:
        from backend.prediction_engine import WordPredictionEngine
        from utils.dataset_loader import DatasetLoader
        
        engine = WordPredictionEngine()
        loader = DatasetLoader()
        datasets = loader.load_default_data()
        
        # Train
        engine.train(datasets['english'])
        
        # Test prediction
        predictions = engine.predict_next_words("how are", top_k=3)
        sequences = engine.predict_sequences("how are", top_k=2)
        
        print(f"✓ Predictions for 'how are': {predictions}")
        print(f"✓ Sequences: {sequences}")
        return True
    except Exception as e:
        print(f"✗ Prediction engine error: {e}")
        return False

def test_chatbot_engine():
    """Test chatbot response generation"""
    print("\nTesting chatbot engine...")
    try:
        from backend.chatbot_engine import ChatbotEngine
        from utils.dataset_loader import DatasetLoader
        
        engine = ChatbotEngine()
        loader = DatasetLoader()
        datasets = loader.load_default_data()
        
        # Train
        engine.train(datasets['english'])
        
        # Test response
        response = engine.generate_response("Hello")
        
        assert len(response) > 0
        print(f"✓ Response for 'Hello': {response}")
        return True
    except Exception as e:
        print(f"✗ Chatbot engine error: {e}")
        return False

def test_language_module():
    """Test language module"""
    print("\nTesting language module...")
    try:
        from backend.language_module import LanguageModule
        
        module = LanguageModule()
        
        # Test language detection
        lang = module.detect_language("Hello, how are you?")
        print(f"✓ Language detection: 'Hello, how are you?' -> {lang}")
        
        # Test language setting
        module.set_language('hindi')
        print(f"✓ Language set to: {module.current_language}")
        
        return True
    except Exception as e:
        print(f"✗ Language module error: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("="*50)
    print("CHATBOT SYSTEM TEST SUITE")
    print("="*50)
    
    tests = [
        test_imports,
        test_dataset_loader,
        test_preprocessing,
        test_prediction_engine,
        test_chatbot_engine,
        test_language_module
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "="*50)
    print("TEST RESULTS")
    print("="*50)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ All tests passed! System is ready to use.")
    else:
        print(f"\n✗ {total - passed} test(s) failed. Please check errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
