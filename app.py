import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('laptop_price_model.pkl')

# Title of the app
st.title("Laptop Price Predictor")

# Input fields for user to enter laptop specifications
ram = st.selectbox("RAM", [4, 8, 16, 32, 64])
storage = st.selectbox("Storage", [128, 256, 512, 1024, 2048, 4096])
processor = st.selectbox("Processor", ['i3', 'i5', 'i7', 'i9', 'AMD RYZEN 5', 'AMD RYZEN 9'])
company = st.selectbox(" Company", ['Dell', 'HP', 'Lenovo', 'Apple', 'Acer', 'Samsung'])
screen_resolution = st.selectbox("Screen Resolution", ['1920x1080', '1366x768', '3840x2160', '2560x1440'])
memory = st.selectbox("Memory Type", ['HDD', 'SSD'])
operating_system = st.selectbox("Operating System", ['Windows', 'Linux', 'macOS'])
gpu = st.selectbox("GPU", ['INTEL', 'AMD', 'NVIDIA'])

# Button to predict the price
if st.button("Predict Price"):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        'RAM': [ram],
        'Storage': [storage],
        'Processor': [processor],
        'Company': [company],
        'Screen_Resolution': [screen_resolution],
        'Memory': [memory],
        'Operating_System': [operating_system],
        'GPU': [gpu]
    })
    
    # Make prediction
    predicted_price = model.predict(input_data)
    
    # Display the predicted price
    st.write(f"The predicted price of the laptop is: ₹{predicted_price[0]:,.2f}")