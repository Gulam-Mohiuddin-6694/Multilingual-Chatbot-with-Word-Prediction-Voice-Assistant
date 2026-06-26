import pickle
import os
from collections import defaultdict, Counter
import numpy as np

class WordPredictionEngine:
    def __init__(self):
        self.ngram_model = defaultdict(Counter)
        self.vocabulary = set()
        self.trained = False
    
    def train(self, sentences, n=2):
        """Train N-gram model on sentences"""
        for sentence in sentences:
            words = sentence.lower().split()
            self.vocabulary.update(words)
            
            # Build N-gram model
            for i in range(len(words) - n + 1):
                context = tuple(words[i:i+n-1])
                next_word = words[i+n-1]
                self.ngram_model[context][next_word] += 1
        
        self.trained = True
    
    def predict_next_words(self, text, top_k=5):
        """Predict next words based on input text"""
        if not self.trained:
            return []
        
        words = text.lower().strip().split()
        if not words:
            return []
        
        # Try bigram (last word as context)
        context = (words[-1],) if len(words) >= 1 else ()
        
        if context in self.ngram_model:
            predictions = self.ngram_model[context].most_common(top_k)
            return [word for word, _ in predictions]
        
        # Fallback: return most common words
        all_words = Counter()
        for counter in self.ngram_model.values():
            all_words.update(counter)
        
        return [word for word, _ in all_words.most_common(top_k)]
    
    def predict_sequences(self, text, top_k=3):
        """Predict complete sequences"""
        predictions = self.predict_next_words(text, top_k)
        sequences = []
        
        for pred in predictions:
            sequence = f"{text} {pred}"
            sequences.append(sequence)
        
        return sequences
    
    def save_model(self, filepath):
        """Save trained model"""
        with open(filepath, 'wb') as f:
            pickle.dump({
                'ngram_model': dict(self.ngram_model),
                'vocabulary': self.vocabulary,
                'trained': self.trained
            }, f)
    
    def load_model(self, filepath):
        """Load trained model"""
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                data = pickle.load(f)
                self.ngram_model = defaultdict(Counter, data['ngram_model'])
                self.vocabulary = data['vocabulary']
                self.trained = data['trained']
            return True
        return False
