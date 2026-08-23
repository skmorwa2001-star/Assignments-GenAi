# ------Assignment 7 : Object-Oriented Programming (OOP)------

# Task 1 :Basic Class & Object Creation
- Create a class Product
- Pass Attribute --> name, price, category
- Make function for method
 -- get_info() ----> print the details of product 
- Create two objects as p1 and p2
- Calling the get_info() 
- to get the details of products


# Task 2 : Constructor & Encapsulation
- Modify the class Product class
- Make price a Private attribute --> __price
  -- Private attribute avoid the direct access
  -- Access / Update the private attribute we use getter and setter methods
  -- Getter method used for read the private attribute
  -- Setter method used for updatee the private attribute
- if new_price>0 then update the price
- if new_price is 0 or negative then print the invalid message


# Task 3 : Inheritance (Single-Level)
- Create a subclass ElectroincProduct that inherits from Product 
---> means that ElectronicProduct is a child class and Product is parent class
---> child class can use parent class attributes and methods.
- Additional attribute ---> warrenty_years
- Use super().__init__(name,price,category) ---> calls the constructor of Product class and initizes
- Overriding the warrenty_years in get_info() method function



# Task 4 : Poymorphism
- Product class as Parent class
- Common attributes (name,price,category)
- Create child class as Laptop(Product) ---> inherits the parents properties
- also add one extra attribute --> ram
- Call constructor of parent class ---> super().__init__(...)
-for extra attribute ---> self.ram=ram
- Create other child class Mobile(Product)
- also add extra attribute --> camera
- Both child classes overriding get.info()
- Both laptop and mobile put in a list
- apply loop which call get_info() on each object 



# Task 5 : Abstraction (Using Abstract Base Class)
- We use abstraction --> import abc module
- use @abstractmethod to make abstraction method
- Payment is abstract class --> Payment(ABC)
- process_payment() --> structure
- child can override the method
- Create subclass --> CreditCardPayment(Payment) and UPIPayment(Payment)
- define process_payment in its own way
- Create objects and test


# Task 6: Magic Methods & Operator Overloading
- Create a class Product
1. __str__ method ---> comvert to readable form
  - like Product : name , price , category
2. __add__ operator ---> to combine the price and show the total price of products
- Create two objects like as -- laptop and mouse
- test to print objects
- test to combine the total price


# Task 7: Mini Project : Simple Inventory System (OOP Only)
1. Product Class
----> This class is used to store the details of a product.
----> Attributes -> name,price,category
--> Method 
   ---> __str__() --> returns details in readable format
   ---> __add__() --> adds prices of two product objects and returns total price

2. Inventory Class
----> This class is used to manage all products in a list
----> Attributes -> products
----> Methods :
- add_product() -> adds a product object to inventory
- remove_product() -> removes a product by name
- get_total_value() -> calculates total price of all products in inventory
- show_all_product() -> displays all products stored in inventory

3. Store Class
----> This class is represent the store and contains the inventory
----> Attributes --> store_name , inventory
----> Methods : 
- add_new_product() --> creates a new product object and adds it to inventory
- show_summary() --> shows store name , total number of products , total inventory value , and all products

# Learning Objective
- Classes & Obective
- Attributes & Methods
- Constructors (__init__)
- Encapsulation (private / protected attributes)
- Inheritance
- Polymorphism (method overriding)
- Abstraction (simple base class)
- Magic Methods
- Operator overloading


# How to run

Requirements
- Python 
- VS code or other code editor

Steps:
1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and run