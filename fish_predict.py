# Welcome to Cursor



# 1. Try generating with command K on a new line. Ask for a pytorch script of a feedforward neural network
# 2. Then, select the outputted code and hit chat. Ask if there's a bug. Ask how to improve.
# 3. Try selecting some code and hitting edit. Ask the bot to add residual layers.
# 4. To try out cursor on your own projects, go to the file menu (top left) and open a folder.
from sklearn.linear_model import LinearRegression
import numpy as np
import streamlit as st

# Function to predict fish weight
def predict_fish_weight(vertical_length, diagonal_length, cross_length, height, width):
    # Dummy model for demonstration purposes
    model = LinearRegression()
    X = np.array([vertical_length, diagonal_length, cross_length, height, width]).reshape(1, -1)
    prediction = model.predict(X)
    return prediction[0]

# Streamlit web app
st.title("Fish Weight Predictor")
st.write("Enter the fish measurements below:")

vertical_length = st.number_input("Vertical Length", min_value=0.0)
diagonal_length = st.number_input("Diagonal Length", min_value=0.0)
cross_length = st.number_input("Cross Length", min_value=0.0)
height = st.number_input("Height", min_value=0.0)
width = st.number_input("Width", min_value=0.0)

if st.button("Predict"):
    prediction = predict_fish_weight(vertical_length, diagonal_length, cross_length, height, width)
    st.write(f"The predicted fish weight is: {prediction:.2f}")
