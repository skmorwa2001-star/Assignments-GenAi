# Task 4: Mini Dashboard

import streamlit as st

# title
st.title("Simple Sales Dashboard")
st.write("The dashboard shows monthly sales data.")

# List of months
months=["January","February","March","April"]

# Static dictionary of monthly
sales={
    "January":1200,
    "Febuary":1500,
    "March":900,
    "April":2000
}

# Select months
selected_month=st.selectbox("Select the Month", months)

#Display selected months's sales
st.write(f"Sales in {selected_month}")
value=sales[selected_month]

#Display a bar chart
st.subheader("Monthly Sales Chart")
st.bar_chart(list(sales.values()))
