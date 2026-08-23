# Task 2: Bill Calculator with Error Handling

prices=[120, 350, 'abe', 500, -200, 800]

total=0

for price in prices:
    try:
        # if price are not int and float type then TypeError raise
        if type(price)!=int and type(price)!=float:
            raise TypeError

        # if price is negative value then also ValueError Raise
        if price < 0:
            raise ValueError("Negative price not allowed")
    
        total = total + price
        print("Added:",price ,"Total:",total)

    # any str and input is Skipped
    except TypeError:
        print("Skipped",price,"- not a number")

    # any negative number is skipped
    except ValueError as ve:
        print("Skipped:",price,"-",ve)  

# final total of bill is print
print("Final Total:", total)           