import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load('fraud_detection_pipeline.pkl')

# Streamlit UI
st.title('💳 Fraud Detection App')
st.markdown("Enter transaction details below:")

transaction_type = st.selectbox("Transaction Type", ["TRANSFER", "PAYMENT", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance - Sender", min_value=0.0, value=1000.0)
newbalanceOrg = st.number_input("New Balance - Sender", min_value=0.0, value=900.0)
oldbalanceDest = st.number_input("Old Balance - Receiver", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance - Receiver", min_value=0.0, value=0.0)

if st.button("Predict"):
    # Prepare input DataFrame
    input_data = pd.DataFrame([{
        'type': transaction_type,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrg': newbalanceOrg,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Output result
    if prediction == 1:
        st.error("⚠️ This transaction is predicted to be FRAUDULENT.")
    else:
        st.success("✅ This transaction is predicted to be LEGITIMATE.")
