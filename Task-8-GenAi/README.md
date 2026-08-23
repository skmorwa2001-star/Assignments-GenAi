### ---Assignment 8 : Streamlit (Basic App Building)----#####

# Task 1: Basic Streamlit App
- disply a title: "Welcome to Streamlit" ---> st.title()
- Shows a input box for entering your name  ---> st.text_input() 
- When user click a button diaplay --> Geet Me
- Make button by help of st.button()



# Task 2: Price calculator
- Make tile as Price Calculator
- Ask user to input the price --> st.number_input()
- make a slider discount percentage (slider from 0 to 50%) --> st.slider()
- click on button ,calculates discounted price 
----> discounted_price = (price*discount_percent)/100
----> final_price = price - discounted_price
- shows result using st.success()


# Task 3: Product Form
- Make title -> Product Form
- Make a sidebar to enter 
----> Make header for side bar --> st.sidebar.header()
----> product Name --> st.sidebar.text_input()
----> Category --> selectbox for category --> st.sidebar.selectbox()
----> Price --> st.sidebar.number_input()
- Make "Add Product" button   --> st.sidebar.button()
----> shows a success message
----> pprduct details --> st.write


# Task 4: Mini Dashboard
- Make a title --> Simple Sales Dashboard
- Description --> st.write()
- Lsit for months 
- dictionary of monthly sales helps to store monthy sales
- make a selectbox for months --> st.selectbox()
- Disply selected months's sales ---> st.write()
- Display the bar chart ---> st.bar_chart(list(sales.values()))



# Learniing Objective
- Creating Streamlit apps
- Text inputs , number input , buttons , selectbox , sidebar
- Displaying results using st.write , st.success , st.error , st.table
- Simple calculations & visual display


# How to run

Requirements
- Python 
- VS code or other code editor

Steps:
1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and write--> py -m streamlit run file_name.py or streamlit run file_name.py