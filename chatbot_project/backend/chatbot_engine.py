import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ChatbotEngine:
    def __init__(self):
        self.responses = {}
        self.vectorizer = TfidfVectorizer()
        self.trained = False
        self.corpus = []
        self.response_map = {}
    
    def train(self, conversations):
        """Train chatbot with conversation data"""
        self.corpus = conversations
        
        # Build response patterns - keep simple for all languages
        self.response_map = {}
        
        # Use first few sentences as patterns
        for i in range(min(len(conversations), 10)):
            key = conversations[i].lower()[:20]  # First 20 chars as key
            self.response_map[key] = conversations[i]
        
        if len(self.corpus) > 0:
            try:
                self.vectorizer.fit(self.corpus)
                self.trained = True
            except:
                self.trained = False
    
    def generate_response(self, user_input):
        """Generate response based on user input"""
        user_input_lower = user_input.lower()
        
        # Check for pattern matches
        for pattern, response in self.response_map.items():
            if pattern in user_input_lower:
                # Return next sentence from corpus
                idx = self.corpus.index(response)
                if idx + 1 < len(self.corpus):
                    return self.corpus[idx + 1]
                return response
        
        # Use similarity matching if trained
        if self.trained and len(self.corpus) > 0:
            try:
                user_vec = self.vectorizer.transform([user_input])
                corpus_vec = self.vectorizer.transform(self.corpus)
                similarities = cosine_similarity(user_vec, corpus_vec)[0]
                
                if similarities.max() > 0.1:
                    best_match_idx = similarities.argmax()
                    # Return next sentence
                    if best_match_idx + 1 < len(self.corpus):
                        return self.corpus[best_match_idx + 1]
                    return self.corpus[best_match_idx]
            except:
                pass
        
        # Return random response from corpus
        if len(self.corpus) > 0:
            return random.choice(self.corpus)
        
        return "I understand."
