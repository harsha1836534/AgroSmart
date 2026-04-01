import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load dataset
df = pd.read_csv(os.path.join(BASE, "data", "AgroQA Dataset.csv"), sep='\t')

# Clean data
df = df.dropna(subset=['Question', 'Answer'])

# Assume columns: Question, Answer
X = df['Question']
y = df['Answer']

# Vectorization
# Define custom stop words to filter out common non-agricultural terms
custom_stops = ['best', 'time', 'good', 'question', 'farmer', 'months', 'day', 'days', 'man', 'woman', 'agronomist']
stops = list(TfidfVectorizer(stop_words='english').get_stop_words()) + custom_stops

vectorizer = TfidfVectorizer(stop_words=stops, use_idf=False, ngram_range=(1, 1))
X_vec = vectorizer.fit_transform(X)

# Instead of training a classifier, we save the vectors and original text 
# for similarity matching at runtime
pickle.dump(vectorizer, open(os.path.join(BASE, "models", "vectorizer.pkl"), "wb"))
pickle.dump(X_vec, open(os.path.join(BASE, "models", "questions_vec.pkl"), "wb"))
pickle.dump(X.tolist(), open(os.path.join(BASE, "models", "questions.pkl"), "wb"))
pickle.dump(y.tolist(), open(os.path.join(BASE, "models", "answers.pkl"), "wb"))

print("NLP Search Corpus prepared and saved!")