# 🌾 AgroSmart Assistant

AgroSmart is an AI-powered agricultural assistant designed to help farmers make better decisions. It provides a specialized **Farming Chatbot** for answering common agricultural questions and a **Crop Recommendation System** that suggests the best crops to plant based on soil nutrients and environmental factors.

---

## 🚀 Getting Started

### 1. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 2. Train the AI Models
Before running the app for the first time, or if you update the data, train the models:
```bash
.\train_models.bat
```
*This will process the datasets in `/data` and save the trained models in `/models`.*

### 3. Run the Application
Start both the Flask API and the Streamlit UI with:
```bash
.\start-servers.bat
```
- **Backend API:** http://127.0.0.1:5000
- **Frontend UI:** Typically http://localhost:8501

---

## 🛠️ Features

### 1. Smart Farming Chatbot
The chatbot uses **Semantic Search (Cosine Similarity)** to match your questions against a database of thousands of agronomy records. 
- **Higher Accuracy:** It understands the context of your question rather than just looking at words.
- **Reliability:** It only answers if the confidence is high, preventing incorrect "guesses."

### 2. Crop Recommendation
Input your soil data (Nitrogen, Phosphorus, Potassium, pH) and environmental factors (Temperature, Humidity, Rainfall), and the system uses a **Random Forest Classifier** to recommend the most suitable crop for your land.

---

## ❓ Sample Questions to Ask

Here are some examples of questions you can ask the chatbot to see how it works:

1. **"How can I control pests as a farmer?"**
2. **"When is the best time to harvest beans?"**
3. **"Apart from hand weeding, what other method is used to weed maize?"**
4. **"How can I know the qualities of a good fertilizer?"**
5. **"What are the indicators of a matured cassava crop?"**
6. **"Which month is good for planting maize?"**
7. **"How can I control bean weevils apart from using insecticide?"**
8. **"What is the best way to prevent soil erosion?"**
9. **"How long does it take for beans to germinate?"**
10. **"What causes yellowing of leaves in maize?"**
11. **"How can I transport maize safely?"**
12. **"Why should I weed my cassava garden?"**
13. **"Can I use stem cuttings for cassava planting?"**
14. **"How do I apply fertilizer to my crops?"**
15. **"What is the recommended spacing for planting beans?"**

---

## 📂 Project Structure

- `app/`: Contains the Flask API (`app.py`) and Streamlit UI (`ui.py`).
- `src/`: Core logic for the chatbot and model training.
- `data/`: Datasets for training (AgroQA and Crop Recommendation).
- `models/`: Storage for the trained machine learning models.
- `requirements.txt`: List of necessary Python libraries.

---
*Developed with ❤️ for the farming community.*
