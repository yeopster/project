import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('project/saved_steps.pkl', 'rb'))

# Streamlit app
st.title("Prediction of Cannula Distorted")
