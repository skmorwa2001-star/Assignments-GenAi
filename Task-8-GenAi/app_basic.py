# Task 1: Basic Streamlit App

import streamlit as st

# title
st.title("Welcome to Streamlit!")

# input box
input_name=st.text_input("Enter your name")

# button
if st.button("Greet Me"):
    st.write(f"Hello,{input_name}")
    