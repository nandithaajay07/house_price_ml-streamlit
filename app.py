import streamlit as st
import numpy as np
import pickle

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))

# App Title
st.title("🏠 House Price Prediction App")

# User inputs
area = st.number_input("Enter Area (in sq ft)", step=100)
bedrooms = st.number_input("Enter Number of Bedrooms", step=1)
age = st.number_input("Enter Age of House (in years)", step=1)

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, age]])
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹{int(prediction[0]):,}")
st.caption("Note: Prediction is based on a small dataset and may not be accurate.")
