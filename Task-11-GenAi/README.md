# ----------------- Assignment 11 -----------------#

## Task 1: Line Plot (Sales Trend)
- Collect a dataset of Superstore from Kaggle
- Convert the dataset into DataFrame
- from info() ---> collect inforamtion about the data type
  ---> Convert it into correct data type
1. Create a line plot showing sales trend over months
- Convert the Order Date column into datetime data type  --> pd.to_datetime()
- Create a new column of Month   --> df['Month']=df['Order Date'].dt.month_name()
- Analysis the monthly total sales ---> groupby('Month')['Sales'].sum()
- Convert it into sequence ---> sorted_index()
2. Add:
- title ----> Monthly Sales Trend
- x ---> data.index    ----------> xlabel=Month
- y ---> data.values    -------------> ylabel=Sales
- Plot the graph


## Task 2: Scatter Plot()
- Create a scatter plot showing relationship between the respective numerical columns
- on x-axis ---> Profit
- on y-axis ---> Sales
- Plot Scatter ----> plt.scatter(x,y)
- Add labels ---> xlabel, ylabel
- Add Title also


## Task 3: Bar Plot()
- From the given kaggle data set
- Category Based total sales ---> df.groupby()
- Make a varible for it ---> data
1. Create a vertical bat chart 
- X-axis ---> data.index
- Y-axis ----> data.values
- Plot bar graph --> plt.bar()
- add title and label ---> plt.title ,plt.xlabel , plt.ylabel
2. Create a horizontal bar chart
- only changes the ylabel and xlabel ---> interchange
- Plot horizontal bar ---> plt.barh()
- Same as vertical bar graph


## Task 4: Multiple Bar Plot()
- Create a multiple bar chart comparing Sales and Profit for different years using the superstore dataset
- Convert the Order Date column to Year
- Group data by Year and calculate total Sales and Profit
- Create a Multiple bar chart using Matplotlib
- Add title, xlabel, ylabel, and legend
- A Multiple bar chart comparing Sales and Profit for each year



## Task 5: Stacked Bar Chart()
- Create a stacked bar chart showing Profit and Discount by Category 
- Group data by Category
- Calculate total Profit and Discount
- Create a stacked bar chart using bottom parameter
- Add title ,xlabel, ylabel, and legend
- A Stacked bar chart displaying Profit and Discount for each Category


## Task 6: Histrogram (Marks Distribution)
- Create a histrogram showing Numeric Distribution for Profit
- Select the Profit column
- Use plt.hist(df['Profit'])
- Add title , xlabel , ylabel, and title
- Display the histrogram
- A histrogram showing the distribution of Profit values in the Dataset


## Task 7: Pie Chart (Market Share)
- Create a pie chart representing the sales contribution of each product category 
- Group sales by category
- Create a pie chart ---> plt.pie()
- Display percentage values using ---> autopct()
- Add title , legend , and highlight one category using ---> explode , also using ----> shadow
- A Pie Chart showing the percentage contribution of each category to total sales


## Learning Objective
- Line Plot
- Scatter Plot
- Bar Plot (Vertical & Horizontal)
- Multiple Bars
- Stacked Bar Charts
- Histogram
- Pie Chart


## How to run

Requirements
- Python 
- VS code or other code editor

Steps:
1. Open the folder in VS code
2. Open the required file
3. Click the run button 