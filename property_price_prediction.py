import streamlit as st
import numpy as np
import pickle

st.title("Property Price Prediction Model")

with open("property_price_model.pkl", "rb") as file:
    model = pickle.load(file)

area = st.number_input("Area (sq ft)")
bedrooms = st.selectbox("Bedrooms", [1,2,3,4,5])
bathrooms = st.selectbox("Bathrooms", [1,2,3,4])
parking = st.selectbox("Parking Slots", [0,1,2,3])
location_score = st.slider("Location Score", 1, 10)
property_age = st.number_input("Property Age")
furnishing_status = st.selectbox("Furnishing Status", [0,1])

if st.button("Predict Property Price"):
    data = np.array([[area, bedrooms, bathrooms, parking, location_score, property_age, furnishing_status]])
    result = model.predict(data)
    st.success(f"Predicted Property Price: ₹ {result[0]:,.2f}")