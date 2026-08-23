# ------------ Assignment 10: Pandas (Series, Dataframe, Functions, Filtering & Anaylsis)----------- #

## Task 1: Pandas Series Basics
1. Import pandas as pd
2. Create a Pandas Series from a list
  - marks = [78,85,90,66,72]
  - pd.Series(marks) --> Create Series
3. Print:
  - Series Values ---> data='Marks' , indexing='Subject' ,type(marks)
4. Access:
  - marks[0] ---> first element access
  - marks[-2:]


## Task 2: Mathematical Operations on Series
- Create same Series marks
1. print(marks+5) ---> add 5 grace marks to all students
2. print(marks-2) ---> subtract 2 marks from all values
3. print(marks*1.05) ---> Multiply all marks by 1.05
4. print(marks/2) ----> Divide all marks by 2


## Task 3: Python Functionalities on Series
- import pandas as pd
- Create same Series marks
1. Find:
  - marks.max() ---> Maximum marks in Series
  - marks.min() ---> Minimum marks in Series
  - marks.sum() ---> Sum of marks
  - marks.mean() --> Average marks
2. Apply a lambda function to check wheather each student has passed(>=70)
  - marks.apply(lambda x:x>=70) ---> check if marks >=70 then return True otherwise False
  - passed.sum() ----> it count the True==1 or False==0 then it sum  the how many students passed

## Task 4: Create a DataFrame
- Create a DataFrame students
   --- pd.DataFrame(students)  ----> to convert dictionary to dataframe
- for 3 rows ---> students.head(3) ---> head() ---> Displays 5 rows to pass any attributes in it
- for last 2 rows --> students.tail(2) ---> tail() ---> display the last 5 rows
- shape() ----> it provides the idea about (rows, columns)
- columns() ----> it provides the idea about the columns names


## Task 5: Important DataFrame Functions
- Using the similiar dataframe
1. 
  - .info() ---> it provides the idea about names, data types, and non-null values
  -  .describe() ---> it provides the idea about the statistical summary(count, mean, std, mean, min, max) for numeric columns
  - .head() ---> it provides idea about first 5 rows
  - .tail() ---> it provides idea about last 5 rows
2. 
  - sorted_values(by='Marks',asecding=False) ----> sorts the DataFrame by marks in descending order
3. 
  - reset_index(drop=True) ---> Resets the index after sorting and removes the old index


## Task 6: Filtering & Conditional Selection
1. Students who scored more than 75 marks 
- Used a conditional filter (marks>70) to display students who scored more than 70 marks
2. Students beloning to subject math
- Filtered the DataFrame where the subject column is equal to math
3. Students who scored more than average marks
- first calculate the average by - df['Marks'].mean()
- then display only those students whose marks are greater than average
4. Students who failed (marks<70)
- Selected students whose marks are less than 70 --> (Marks<70>)



## Task 7: Grouping & Basic Analysis
1. find the average marks per students 
- Grouped students according to their subjects using ---> groupby()
- Calculates the average marks using --> .mean()
2. Count number marks per subject
- Used .count() after function to find the total number of students in each subject
3. Find maximum marks per subject
- Used the .max() function to find the highest marks scored in each subject


## Task 8: Pandas Plotting (Simple Graphs)
1. Plot a bar graph of student names VS marks
- Used df.plot() with kind=bar
- The x-axis represents student names and y-axis represents marks
2. Plot a line graph of marks
- Used Series.plot() with kind=line
- Displays the trend of students marks in sequence
3. Plot a histogram of marks
- Used Series.plot() with kind= hist
- Shows the distribution of marks



## Task 9: Mini Case : Sales Data Analysis
- Create dataframe
 sales={
  'Day':['Mon','Tue','Wed','Thu','Fri'],
  'Revenue':[1200,1500,900,2000,1800]
 }    
  -----> pd.DataFrame(sales)
- Perfroms:
1. Total Revenue  ----> df_sales['Revenue'].sum()
2. Average daily revenue ---> df_sales['Revenue'].mean()
3. Days with highest revenue ----> df_sales['Revenue'].max()
4. Days where revenue > average ---> Boolean filtering
5. Plot revenue vs day ----> df_sales.plot()



# Learning Objective
- Pandas Series ---> Creates a series, access 
- Mathematical operations  ---> add, subtract, mul, div
- Python functionalities --> .mean(), .max(), .min(), .sum()
- Creating and working with dataframe ---> Create DataFrame, working
- Important DataFrame functions ----> .info(), .describe(), .head(), .tail(), .shape(), .columns(), sorted_value(), reset_index() 
- Filtering & Basic analysis 
- Simple plotting using pandas ---> df.plot()




# How to run

Requirements
- Python 
- VS code or other code editor

Steps:
1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and write--> py -m streamlit run file_name.py or streamlit run file_name.py