import streamlit as st
import requests

st.title("VaultGuard AI")
st.write("Enter the required features below to generate a prediction.")

# 1. Wrap your fields in a form component
with st.form("prediction_form"):
    st.subheader("Input Features")
    
    # Text Inputs
    sender_account = st.text_input("Sender Account", value="C-12345")
    reciever_account = st.text_input("Receiver Account", value="C-67890")
    
    # Numeric Inputs (Integers and Floats)
    amount = st.number_input("Amount", min_value=0.0, max_value=1e7, value=1000.0)
    hour_of_day = st.number_input("Hour of Day (0-23)", min_value=0, max_value=23, value=12)
    dest_prev_amount_sum = st.number_input("Destination Previous Amount Sum", min_value=0, value=500)
    dest_prev_txn_count = st.number_input("Destination Previous Transaction Count", min_value=0, value=5)
    dest_txn_count_24h = st.number_input("Destination Transaction Count in Last 24 Hours", min_value=0, value=2)

    # Categorical Inputs (Dropdowns and Radio Buttons)
    type = st.selectbox("Transfer Type", ["TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT", "PAYMENT"])
    dest_is_first_txn = st.checkbox("Is this the first transaction for the destination account?")

    # 2. Add the submit/predict button at the bottom of the form
    submit_button = st.form_submit_button(label="Predict")

# 3. Handle the button click event
if submit_button:
    # This block only runs AFTER the button is clicked
    st.success("Form submitted successfully!")

    #log_cols   = ["amount", "dest_prev_amount_sum", "dest_prev_txn_count", "dest_txn_count_24h"]
    #cat_cols   = ["type"]
    #flag_cols  = ["is_night", "dest_is_first_txn", "amount_1M_to_10M", "amount_is_10M"]

    
    # Prepare the payload (this matches exactly what your FastAPI backend will expect)
    input_data = {
        "amount": amount,
        "dest_prev_amount_sum": dest_prev_amount_sum,
        "dest_prev_txn_count": dest_prev_txn_count,
        "dest_txn_count_24h": dest_txn_count_24h,
        "type": type,
        "is_night": 1 if hour_of_day >=0 and hour_of_day < 6 else 0,
        "dest_is_first_txn": dest_is_first_txn,  # Assuming you have a way to determine this
        "amount_1M_to_10M": 1 if amount >= 1e6 and amount < 1e7 else 0,
        "amount_is_10M": 1 if amount >= 1e7 else 0,
    }
    is_fraud = {
        "is_fraud": True
    }

    is_not_fraud = {
        "is_fraud": False
    }
    
    # For now, we mock the prediction output
    st.subheader("Prediction Results")


    if input_data["type"] != "TRANSFER" and input_data["type"] != "CASH_OUT":
        st.json(is_not_fraud)
    else:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        st.json(response.json())

        

    