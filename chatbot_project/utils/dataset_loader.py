import os
import pandas as pd

class DatasetLoader:
    def __init__(self, dataset_dir='dataset'):
        self.dataset_dir = dataset_dir
        self.datasets = {
            'english': [],
            'hindi': [],
            'telugu': []
        }
    
    def load_from_csv(self, filename):
        """Load data from CSV file"""
        filepath = os.path.join(self.dataset_dir, filename)
        if os.path.exists(filepath):
            try:
                df = pd.read_csv(filepath)
                return df['text'].tolist()
            except:
                return []
        return []
    
    def load_default_data(self):
        """Load default training data"""
        # Try to load from CSV files first
        english_csv = self.load_from_csv('english_data.csv')
        hindi_csv = self.load_from_csv('hindi_data.csv')
        telugu_csv = self.load_from_csv('telugu_data.csv')
        
        # English conversational data
        english_data = english_csv if english_csv else [
            "Hello, how are you?",
            "I am doing great, thank you!",
            "What is your name?",
            "My name is AI Assistant.",
            "How can I help you today?",
            "Tell me about artificial intelligence.",
            "Artificial intelligence is the simulation of human intelligence.",
            "Machine learning is a subset of AI.",
            "Deep learning uses neural networks.",
            "Natural language processing helps computers understand text.",
            "How are you doing?",
            "What are you doing?",
            "Where are you going?",
            "I am learning Python programming.",
            "Python is a great programming language.",
            "I love machine learning and AI.",
            "The weather is nice today.",
            "What is the time now?",
            "Can you help me with this?",
            "Thank you for your help!",
            "Have a great day!",
            "See you later!",
            "Good morning, how are things?",
            "Everything is going well.",
            "I am working on a project.",
            "This is an interesting topic.",
            "Tell me more about it.",
            "I would like to know more.",
            "Can you explain this concept?",
            "That makes sense now.",
        ]
        
        # Hindi conversational data
        hindi_data = hindi_csv if hindi_csv else [
            "नमस्ते, आप कैसे हैं?",
            "मैं ठीक हूं, धन्यवाद!",
            "आपका नाम क्या है?",
            "मेरा नाम एआई सहायक है।",
            "मैं आपकी कैसे मदद कर सकता हूं?",
            "आज मौसम अच्छा है।",
            "मुझे मशीन लर्निंग पसंद है।",
            "यह बहुत अच्छा है।",
        ]
        
        # Telugu conversational data
        telugu_data = telugu_csv if telugu_csv else [
            "నమస్కారం, మీరు ఎలా ఉన్నారు?",
            "నేను బాగున్నాను, ధన్యవాదాలు!",
            "మీ పేరు ఏమిటి?",
            "నా పేరు AI అసిస్టెంట్.",
            "నేను మీకు ఎలా సహాయం చేయగలను?",
            "ఈరోజు వాతావరణం బాగుంది.",
            "నాకు మెషిన్ లెర్నింగ్ అంటే ఇష్టం.",
            "ఇది చాలా బాగుంది.",
        ]
        
        self.datasets['english'] = english_data
        self.datasets['hindi'] = hindi_data
        self.datasets['telugu'] = telugu_data
        
        return self.datasets
    
    def get_all_data(self):
        """Get all loaded data"""
        return self.datasets
