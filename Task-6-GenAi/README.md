########### Assignment 6: Exception Handling ###########


# Task 1: Safe Division Utility

- Takes input of numerator and denominator from user
- Uses try-except to handle:
---> ValueError - non-numeric input
---> ZeroDivisionError - division by Zero
---> else - print result if no error found 
---> finally - prints "Operation Complete" means code run successfully.



# Task 2: Bill Calculator with Error Handling

- Prices list = [120, 350, 'abc', 500, -200, 800]
- Write code
 -- apply for loop to iterates through the list
 -- Uses the try-except to handle:
 -- In try use the if the if condition
   -- if price is not int and float then it is TypeError
   -- if price is negative then it is ValueError
 --except:
  -- if price is not int and float
  -- then skipped the price
 -- except:
  -- if price is negative 
  -- then skipped the price
 -- else:
 -- print the total bill    



 # Task 3: Custom Exception : Age Validator

 - write a function check_age(age)
 - if age <1 or age>120 then ok 
 - if age is out of range then raise a ValueError and give a message ("Age must be between 1 and 120)
 - In main code
  -- Take input from user
  -- calling function and check age is in range then print "Valid Age"
  -- if age is not in range then print "Error"


# Task 4: File Reader with Exception Handling

- Ask user to enter the file name
- try:
-- open the file and read file 
-- if file is found then print the first 3 lines of the file
- except:
  -- FileNotFound --> if the file is not found
  -- PermissionError --> if the file file permission is denied

- finally:
 print the "File operation attempted"



# Task 5: Mini Program :Safe Shopping Cart
- Create a cart list- cart=[]
- apply while loop and ask user to input the value to added their cart(while loop is used because no end condition is given)
--- Stops when user enters 'q' ---> apply break
--- apply try-except handling 
   - convert input into a float
   - ValueError --> if user enters invalid input
   - raise exception ---> if price is negative

- At the end print
 - Total items --> len(cart)
 - Total bill --> sum(cart)   

# Learning Objective
- try, except
- Mutiple except blocks
- else
- finally
- Raising custom exceptions(raise)
- Handling common build-in exceptions: ValueError , ZeroDivision, TypeError, FileNotFoundError


# How to run

Requirements
- Python 
- VS code or other code editor

Steps:
1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and run