import os
import sys

# Add project root to sys.path so 'src' is importable
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from flask import Flask, request, jsonify
from src.chatbot import get_answer
from src.recommend import recommend_crop

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to AgroSmart API. Services available: /chat (POST) and /recommend (POST)"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get("query", "")
    try:
        response = get_answer(query)
    except Exception as e:
        response = f"Error: {e}"
    return jsonify({"response": response})

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    features = data.get("data", [])
    try:
        crop = recommend_crop(features)
    except Exception as e:
        crop = f"Error: {e}"
    return jsonify({"crop": crop})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)