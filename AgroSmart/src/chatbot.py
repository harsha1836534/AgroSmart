import pickle
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

_vectorizer = None
_questions_vec = None
_questions = None
_answers = None

def _load_models():
    global _vectorizer, _questions_vec, _questions, _answers
    if _vectorizer is None:
        base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models")
        _vectorizer = pickle.load(open(os.path.join(base, "vectorizer.pkl"), "rb"))
        _questions_vec = pickle.load(open(os.path.join(base, "questions_vec.pkl"), "rb"))
        _questions = pickle.load(open(os.path.join(base, "questions.pkl"), "rb"))
        _answers = pickle.load(open(os.path.join(base, "answers.pkl"), "rb"))

def get_answer(query):
    _load_models()
    
    # Transform query and calculate similarity with all stored questions
    query_vec = _vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, _questions_vec).flatten()
    
    # Find the best match
    best_match_idx = np.argmax(similarities)
    best_score = similarities[best_match_idx]
    
    # Threshold check to avoid nonsensical answers
    if best_score < 0.7:
        return "I'm sorry, I don't have specific information on that topic in my database. Please try asking about crops, pests, or harvesting methods."
        
    return _answers[best_match_idx]