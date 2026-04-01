import streamlit as st
import os
import sys

# Add project root to sys.path so 'src' is importable
app_dir = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(app_dir)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.chatbot import get_answer
from src.recommend import recommend_crop

st.set_page_config(page_title="AgroSmart", page_icon="🌾")
st.title("🌾 AgroSmart Assistant")

option = st.selectbox("Choose Service", ["Ask Question", "Crop Recommendation"])

if option == "Ask Question":
    query = st.text_input("Ask your farming question")
    if st.button("Submit") and query:
        with st.spinner("Thinking..."):
            response = get_answer(query)
            st.info(f"**Answer:** {response}")

else:
    st.subheader("Crop Recommendation")
    st.write("Enter Soil data below:")

    col1, col2 = st.columns(2)
    with col1:
        N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=90)
        P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=42)
        K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=43)
        ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
    
    with col2:
        temp = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=20.0)
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=82.0)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=200.0)

    if st.button("Recommend"):
        data = [N, P, K, temp, humidity, ph, rainfall]
        with st.spinner("Analyzing..."):
            crop = recommend_crop(data)
            st.success(f"Best Crop for your soil: **{crop.upper()}**")