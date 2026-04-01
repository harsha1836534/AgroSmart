import streamlit as st
import requests

st.title("🌾 AgroSmart Assistant")

option = st.selectbox("Choose Service", ["Ask Question", "Crop Recommendation"])

if option == "Ask Question":
    query = st.text_input("Ask your farming question")
    if st.button("Submit"):
        res = requests.post("http://127.0.0.1:5000/chat", json={"query": query})
        st.write(res.json()["response"])

else:
    st.write("Enter Soil Data")

    N = st.number_input("Nitrogen")
    P = st.number_input("Phosphorus")
    K = st.number_input("Potassium")
    temp = st.number_input("Temperature")
    humidity = st.number_input("Humidity")
    ph = st.number_input("pH")
    rainfall = st.number_input("Rainfall")

    if st.button("Recommend"):
        data = [N, P, K, temp, humidity, ph, rainfall]
        res = requests.post("http://127.0.0.1:5000/recommend", json={"data": data})
        st.write("Recommended Crop:", res.json()["crop"])