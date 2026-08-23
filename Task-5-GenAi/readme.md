----------------------- Assignment 5 -------------------------


# Task 1: Create a Simple Module(math.utils.py)
- Create a math_utils.py module
- Define the functions
-- Addition(a, b) ---> return a+b
-- Subtraction(a, b) ---> return a-b
-- Square (n) ---> return n*n

- Create a main.py module and import the modules in two different ways
--- import math_utils
--- from math_utils import square

- Test all functions


# Task 2: Create Another Module(string_utils.py)
- Create a module string_utils.py
1. capitalize_words(text) ---> returns text with each word capitalized
--- Using title() converts the first letter of every word into capital
2. reverse_string(text) --> return reveresed string
--- [::-1] is python slicing
--- it reads the string from end to start
--- so it string gets reversed
3. word_count(text) --> returns number of words in the text
--- split() breaks the sentence into a list of words
--- len() counts how many words are in the list

import the module in main.py and test all functions



# Task 3: Create a Simple Package(shop_package)
Create a package named task3_shop_package containing-->
1. discount.py
2. billing.py
3. __init__.py

1. discount.py
---- for apply_discount(price, discount)
- Calculate discount amount--> price*percent/100
- then subtract from original price
--- price = discounted_price

---- for flat_discount(price)
- return price - 50

2. billing.py
---- calculate_total(prices)
- prices is a list
- sum(prices) adds all values in the list
- return total bill

---- tax (5%)
- calculate 5% tax--> amount * 5/100
-Add to the original amount

3. __init__.py
- This file makes shop_package a Python package
- It also allows direct import of the functions from the package



# Task 4: Importing the package in main.py
--- import shop_package.discount as disc
- discount.py is impported from the package
- as disc gives a short name to the module

--- from shop_package.billing import calculate_total
- This import only the calculate.total() function from billing.py



# Learning Objective
- Creating python modules (.py files)
- Importing modules
- Creating packages using __init__.py
- Using from module import function and import module


# How to run

Requirements
- Python 
- VS code or other code editor

Steps:
1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and run