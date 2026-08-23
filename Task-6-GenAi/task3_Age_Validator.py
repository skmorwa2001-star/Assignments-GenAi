# Task 3: Custom Exception : Age Validator

# function to check age in between 1 to 120
def check_age(age):
    if age<1 or age>120 :
        raise ValueError ("Age must be between 1 and 120")
    
# ask age from user and check if the age is valid or not
try:
    age=int(input("Enter age: "))
    check_age(age)
    print("Valid Age")

except ValueError as ve:
    print("Error:", ve)
