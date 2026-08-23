# First way
import modules_assignment.math_utils

# Test the add function
print("Addition of a and b is : ", modules_assignment.math_utils.add(10,5))

# Test the subtract function
print("Subtraction of a and b is : ", modules_assignment.math_utils.subtract(100,5))

# Test the square function
print("Square of n is : ", modules_assignment.math_utils.square(5))

# Second way
from modules_assignment.math_utils import square

print("Square of n is : ", square(5))


# String module test

import modules_assignment.string_utils

text="hello, my name is sunil kumar"

print("Original Text:",text)
print("Capitalized:",modules_assignment.string_utils.capitalize_words(text))
print("Reversed:",modules_assignment.string_utils.reverse_string(text))
print("Word Count:",modules_assignment.string_utils.word_count(text))



# Import the shop_package

import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax


# Example
## 1000 price par 10% discount apply hoga
print("Discounted Price:",disc.apply_discount(1000, 10))

# List of product
prices= [100, 200, 300]

# Using calculate.total() from billing.py
## ye list ke saare prices ka total nikalega

total=calculate_total(prices)
print("Total Bill:", total)

# Using apply_tax() from billing.py
## Total amount par 5% tax add hoga

print("Total with tax:", apply_tax(total))