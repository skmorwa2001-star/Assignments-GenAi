# Function to apply percentage discount on price

def apply_discount(price, percent):
    # Calculate discount amount and subtract from original price
    discounted_price = price - (price * percent/100)
    return discounted_price


# Function to apply flat discount of 50

def flat_discount(price):
    return price - 50