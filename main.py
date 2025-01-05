import streamlit as st
import joblib
import pandas as pd

model = joblib.load("D:/Personal projects/House price prediction/house_price_model.pkl")

st.title("House price prediction")

square_footage = st.number_input("Square Footage", min_value=500, max_value=5000,step=50)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=5,step=1)
age = st.number_input("Age", min_value=0, max_value=1000,step=1)

if st.button('Predict price'):
    input_data = pd.DataFrame({
        'Square_Footage':[square_footage],
        'Bedrooms' : [bedrooms],
        'Age' : [age]
    })

    predicted_price = model.predict(input_data)[0]

    st.write(f"The predicted house price is: ${predicted_price:,.2f}")
