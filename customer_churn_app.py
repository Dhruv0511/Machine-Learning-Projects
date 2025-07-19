import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained pipeline
scaler = joblib.load('scaler.pkl') 
model = joblib.load('model.pkl')

# Streamlit UI
st.title('Churn Prediction App')

st.divider()

st.write("Enter details below and hit the predict button to get predictions:")

st.divider()

gender = st.selectbox("Gender Type", ["MALE", "FEMALE"])

age = st.number_input("Age", min_value=10, max_value=100, value=30)

tenure = st.number_input("Tenure", min_value=0, max_value=130, value=10)

monthlycharge = st.number_input("MonthlyCharge", min_value=30, max_value=150)

st.divider()

Predictbutton = st.button('Predict!')

if Predictbutton:
    gender_selected = 1 if gender == 'FEMALE' else 0
    
    X = [age, gender_selected, tenure, monthlycharge]
    
    X_array = scaler.transform([np.array(X)])
    
    prediction = model.predict(X_array)[0]

    predicted = 'Yes' if prediction == 1 else 'No'

    st.write(f"Predicted: {predicted}")
else:
    st.write("Please enter the values and use the Predict button.")

	