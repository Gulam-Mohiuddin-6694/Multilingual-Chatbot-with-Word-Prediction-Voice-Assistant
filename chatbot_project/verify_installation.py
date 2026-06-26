"""
Installation Verification Script
Checks if all dependencies and components are properly installed
"""

import sys
import subprocess

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_status(check, status, message=""):
    symbol = "✓" if status else "✗"
    status_text = "PASS" if status else "FAIL"
    print(f"{symbol} {check}: {status_text} {message}")

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    required = (3, 8)
    status = version >= required
    message = f"(Found: {version.major}.{version.minor}.{version.micro})"
    print_status("Python Version", status, message)
    return status

def check_pip():
    """Check if pip is available"""
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      capture_output=True, check=True)
        print_status("pip", True)
        return True
    except:
        print_status("pip", False)
        return False

def check_module(module_name, import_name=None):
    """Check if a Python module is installed"""
    if import_name is None:
        import_name = module_name
    
    try:
        __import__(import_name)
        print_status(f"Module: {module_name}", True)
        return True
    except ImportError:
        print_status(f"Module: {module_name}", False, "- Run: pip install " + module_name)
        return False

def check_nltk_data():
    """Check if NLTK data is downloaded"""
    try:
        import nltk
        required_data = ['punkt', 'stopwords', 'wordnet']
        all_present = True
        
        for data in required_data:
            try:
                nltk.data.find(f'tokenizers/{data}' if data == 'punkt' else f'corpora/{data}')
            except LookupError:
                all_present = False
                break
        
        print_status("NLTK Data", all_present, 
                    "" if all_present else "- Run: python -c \"import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')\"")
        return all_present
    except:
        print_status("NLTK Data", False)
        return False

def check_project_structure():
    """Check if project structure is correct"""
    import os
    
    required_dirs = ['backend', 'frontend', 'utils', 'dataset', 'models']
    required_files = [
        'backend/app.py',
        'backend/prediction_engine.py',
        'backend/chatbot_engine.py',
        'frontend/index.html',
        'frontend/style.css',
        'frontend/script.js',
        'requirements.txt'
    ]
    
    all_present = True
    
    for dir_name in required_dirs:
        if not os.path.isdir(dir_name):
            print_status(f"Directory: {dir_name}", False)
            all_present = False
    
    for file_name in required_files:
        if not os.path.isfile(file_name):
            print_status(f"File: {file_name}", False)
            all_present = False
    
    if all_present:
        print_status("Project Structure", True)
    
    return all_present

def check_imports():
    """Check if project modules can be imported"""
    try:
        sys.path.append('.')
        from backend.prediction_engine import WordPredictionEngine
        from backend.chatbot_engine import ChatbotEngine
        from backend.language_module import LanguageModule
        from utils.preprocessing import TextPreprocessor
        from utils.dataset_loader import DatasetLoader
        
        print_status("Project Imports", True)
        return True
    except Exception as e:
        print_status("Project Imports", False, f"- Error: {str(e)}")
        return False

def main():
    """Run all checks"""
    print_header("INSTALLATION VERIFICATION")
    print("\nChecking system requirements and dependencies...\n")
    
    results = []
    
    # Check Python and pip
    print_header("System Requirements")
    results.append(check_python_version())
    results.append(check_pip())
    
    # Check required modules
    print_header("Python Dependencies")
    modules = [
        ('flask', 'flask'),
        ('nltk', 'nltk'),
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('scikit-learn', 'sklearn'),
        ('transformers', 'transformers'),
        ('torch', 'torch'),
        ('googletrans', 'googletrans'),
        ('SpeechRecognition', 'speech_recognition'),
        ('gTTS', 'gtts'),
        ('langdetect', 'langdetect'),
        ('flask-cors', 'flask_cors')
    ]
    
    for module_name, import_name in modules:
        results.append(check_module(module_name, import_name))
    
    # Check NLTK data
    print_header("NLTK Data")
    results.append(check_nltk_data())
    
    # Check project structure
    print_header("Project Structure")
    results.append(check_project_structure())
    
    # Check imports
    print_header("Project Modules")
    results.append(check_imports())
    
    # Summary
    print_header("VERIFICATION SUMMARY")
    passed = sum(results)
    total = len(results)
    percentage = (passed / total) * 100
    
    print(f"\nPassed: {passed}/{total} ({percentage:.1f}%)")
    
    if passed == total:
        print("\n✅ All checks passed! Your installation is complete.")
        print("\n🚀 You can now run the application:")
        print("   cd backend")
        print("   python app.py")
    else:
        print(f"\n⚠️ {total - passed} check(s) failed.")
        print("\n📋 To fix issues:")
        print("   1. Install missing dependencies: pip install -r requirements.txt")
        print("   2. Download NLTK data: python -c \"import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')\"")
        print("   3. Verify project structure is intact")
        print("   4. Run this script again to verify")
    
    print("\n" + "="*60)
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
