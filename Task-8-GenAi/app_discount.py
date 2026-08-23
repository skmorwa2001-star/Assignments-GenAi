# Task 2: Price Calculator 

import streamlit as st

# titile
st.title("Price Calculator")

# input the price
price=st.number_input("Enter the Product price")

# discount slider
discount=st.slider("Select the discount percentage :",0 ,50, 10)
st.write(f"Selected percentage: {discount}")

# Button to calculate discounted price
if st.button("Calculate Price"):
    # Discount amount
    discounted_amount=(price*discount)/100

    # final discounted price
    final_price=price - discounted_amount
    
    #Show result using success box
    st.success(f"Final Price after {discount}% discount: {final_price}")


     # Comparsion table
    st.subheader("Price Compression")
    table_data=[
        ["Original Price",price],
        ["Discound %",f"{discount}%"],
        ["Final Price",final_price]
    ]
    st.table(table_data)