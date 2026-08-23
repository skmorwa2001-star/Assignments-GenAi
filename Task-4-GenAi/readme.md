### Assignment 4 : File Handling(Read, Write, Append, Modes)

# Task 1 :Write sales records to a file
-Created a list of sales amounts
-Created a sales_data.txt file in the same folder
-Open the sales_data.txt file in writing mode
-Add sale records on a new line in the file
-Close file
-Reopen the file and print its contents


# Task 2 : Read file Different Ways
-Read the data and print it.
-read the first line
-read all lines and converting them into a list of integers


# Task 3: Append New Sales
-append new sales value [5000, 2500, 1700]
-after appending , reopen and print file
-(Optical)--> print the total of lines after appending


# Task 4: Generate Summary Report from file
-read all sales values from sales_data.txt
-convert into integers
-calculate , Total sales , Highest Sale , Lowest Sale , Average Sale 


# Task 5: Create Product into File (User Input)
-Ask user for 3 products names & their prices
-Write into a new file products.txt 
-Format: ProductName  |  Price
-Read the file and print it


# Task 6: Read file Safety (Error Handling inside file handling Only)
-Ask the user for a filename to open
-If the file exists, read and print it
-If it does not exist , print: "File not found. Please check the filename"


# Task 7: Mini Project - Export Discounted Price
-Create a dictionary
-prices={
    "Mouse":50,
    "Keyword":800,
    "Monitor":7000,
    "Pendrive":400,
    "Camera":5000
}
-Ask the user for discount percentage
-Write discounted price into discount_report.txt 
-Using: Product | Original Price | Discounted Price
-After writing, read the file and print it to the terminal


# Learning Objective
-Opening files in different modes (r,w,a,r+,w+)
-Reading using .read(), .readline() , .readlines()
-Writing and appending to files
-Basic data extraction from the text
-Ensuring safe file operation using with blocks


# How to run

Requirements
-Python 
-VS code or other code editor

Steps:
1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and run