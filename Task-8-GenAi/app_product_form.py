# Task 3: Product Form 

import streamlit as st

# Title
st.title("Product Form")

# Sidebar inputs
st.sidebar.header("Enter Product Details")

product_name=st.sidebar.text_input("Product Name")
category=st.sidebar.selectbox(
    "Cateogory",
    ["Electronic","Clothing","Books","Food","Accessories"]
)
price=st.sidebar.number_input("Price")

# Sidebar button
if st.sidebar.button("Add Product"):
    # Success message
    st.success("Product added successfully")


    # display product details
    st.subheader("Product Details")
    st.write(f"Product Name : {product_name}")
    st.write(f"Category : {category}")
    st.write(f"Price : {price}")