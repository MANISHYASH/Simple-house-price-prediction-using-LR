# House Price Prediction using Linear Regression

This project demonstrates a machine learning model that predicts house prices based on input features such as **Square Footage**, **Number of Bedrooms**, and **Age** of the house. The model was built using **Linear Regression** and is deployed as a **Streamlit** application.

## Project Overview

The model is trained on a dataset with features like:
- **Square Footage**: The area of the house in square feet.
- **Number of Bedrooms**: The number of bedrooms in the house.
- **Age**: The age of the house in years.

The trained model is saved using **joblib** and loaded into a Streamlit app that allows users to input these features and predict the price of a house.

## Requirements

Before running the project, make sure to install the required libraries:

pip install streamlit joblib pandas scikit-learn

# How to Use

1. clone the respository:
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction

2. Download or Prepare the Dataset: The model is already trained, but you can train your own model if you'd like. Please refer to the training process in the code if you'd like to regenerate the model.

3. Save the Trained Model: The model is saved in a .pkl file. Make sure the model file (house_price_model.pkl) is in the same directory as the Streamlit app file (main.py).

4. Run the Streamlit Application: To run the app, use the following command in your terminal:
   streamlit run main.py
   
5. Interact with the App: Open the app in your web browser (it should automatically open after running the command). You will be prompted to input:

  * Square Footage of the house
  * Number of Bedrooms
  * Age of the house
  
  Click the "Predict Price" button to see the predicted price of the house. 

# Project structure
The project directory contains the following files:

* house_price_predictor.py: The Streamlit app that accepts user input and predicts the house price.
* house_price_model.pkl: The trained Linear Regression model.
* house_price_dataset.csv: (Optional) The dataset used to train the model (if you want to regenerate the model).
* README.md: Project overview and instructions.

# Future Improvements

* Incorporate more features such as location, number of bathrooms, and proximity to amenities to improve prediction accuracy.
* Implement additional machine learning models (e.g., Random Forest, XGBoost) for better performance.
    

