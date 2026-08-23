# Task 1: Safe Division Utility

try:
    # input numerator and denominator value
    numerator=float(input("Enter numerator: "))
    denominator=float(input("Enter denominator: "))

    result = numerator / denominator

# ValueError handles non-numeric input
except ValueError:
    print("Error: Please a valid number")

# ZeroDivisionError handles division by zero
except ZeroDivisionError:
    print("Error: Denominator cannot be 0")

# prints result if no error occurs
else:
    print("Result:", result)

finally:
    print("Operation Complete")            