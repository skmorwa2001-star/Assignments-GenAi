# Function to calculate total of all prices

def calculate_total(prices):
    # Sum (prices) add all values in the list
    return sum(prices)


# Function to add 5% tax on the total amount

def apply_tax(amount):
    # Add 5% tax to the given value
    return amount + (amount * 5/100)