import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# Load the saved model
model = joblib.load(r"C:\Users\ASUS\OneDrive\Desktop\Sample\Telecom_Churn_Prediction.pkl")

# Creating the function to make predictions
def predict_churn(customer_data):
    prediction = model.predict(customer_data)
    return prediction

# Creating Streamlit app
def app():
    # Inserting image
    image = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Sample\WhatsApp Image 2023-03-29 at 12.26.53 PM.jpeg")
    st.image(image)

    # Create a form for the user to input customer data
    st.title("Telecom Churn Prediction")
    st.subheader("Prediction for new data :")
    st.sidebar.subheader("Enter the following details of the customer :")

    account_length = st.sidebar.number_input("Account length", 0, 250)
    voice_messages = st.sidebar.number_input("Number of voice messages", 0, 50)
    intl_plan = st.sidebar.selectbox("International plan", ["Yes", "No"])
    intl_mins = st.sidebar.number_input("International minutes", 0, 50)
    intl_calls = st.sidebar.number_input("International calls", 0, 20)
    day_mins = st.sidebar.number_input("Day minutes", 0, 500)
    eve_charge = st.sidebar.number_input("Evening charge", 0, 60)
    night_mins = st.sidebar.number_input("Night minutes", 0, 500)
    customer_calls = st.sidebar.number_input("Customer service calls", 0, 10)

    customer_data = pd.DataFrame({
        "account_length": [account_length],
        "voice_messages": [voice_messages],
        "intl_plan": [intl_plan],
        "intl_mins": [intl_mins],
        "intl_calls": [intl_calls],
        "day_mins": [day_mins],
        "eve_charge": [eve_charge],
        "night_mins": [night_mins],
        "customer_calls": [customer_calls]
    })

    # Convert the "International Plan" column to a binary indicator
    customer_data['intl_plan'] = customer_data['intl_plan'].apply(lambda x: 1 if x == 'Yes' else 0)

    # Make a prediction & display the result
    if st.button("Predict"):
        with st.spinner('Making prediction...'):
            result = predict_churn(customer_data)
            if result == 0:
                st.write("This customer is not likely to churn.")
            else:
                st.write("This customer is likely to churn.")

# Calling the app function to run the Streamlit app
if __name__ == '__main__':
    app()
