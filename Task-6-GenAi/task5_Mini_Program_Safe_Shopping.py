# Task 5: Mini Program : Safe Shopping Cart

##Create a cart list
cart=[]

## runs a loop to ask user to enter prices
while True:
    value=input("Enter prices(or q for quiet): ")

    ## If user enter q break the loop print total items and total bill
    if value=='q':
        break

    try:
        ## Convert input to float
        price=float(value)
    
        ## if price is less than 0 then show a message that "Negative price not allowed"
        if price < 0:
            raise ValueError("Negative price not allowed")
    
        ## Added the price to the cart
        cart.append(price)
        print("Added:",price)

    except ValueError as e:
        print("Inavalid input:", e)

## Print the total items in the cart
print("Total items:", len(cart))

## Print the sum of the total cart
print("Total bill:", sum(cart))

