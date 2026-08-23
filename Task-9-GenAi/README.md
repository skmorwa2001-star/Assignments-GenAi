##### ----- Assignment 9 ------ ######

# Task 1: Creating Numpy Arrays
- import numpy as np
- Create arrays
- 1D Array with the help of --> arange() --> in which direct provides range
- 2D Array : 
   - Use arange() --> for integers range
   - reshape() ---> It helps us out to changing the shape of array as per needs
- Numpy array 
   - Use arange() --> by the help of arange we also give gap between the integers as per needs   



# Task 2: Important Mathematical Operations
- Create two Arrays
  -- A = np.array([10,20,30,40])
  -- B = np.array([1,2,3,4])
- Apply Mathematical operations
 -- Additon (A+B)
 -- Subtraction (A-B)
 -- Multiplication (A*B)
 -- Division (A/B)
 -- Power (A**2)


# Task 3: Important Numpy Mathematical Formulas
- Given array
   -- values=np.array([2,4,6,8,10])
- Calculate:
1. Square root ---> np.sqrt()
2. Exponential  ---> np.exp()
3. Logarithm  ---> np.log()
4. Sum ---> np.sum()
5. Cumulative sum ---> np.cum() ---> in given array ---> Output: [2 6 12 20 30]  ---> (2, 2+4, 2+4+6, 2+4+6+8, 2+4+6+8+10)
- print all the operation by the helps of print funnction   


# Task 4: Aggregation Operations
- Given 2D array 
   - data= np.array([[10,20,30],[40,50,60],[70,80,90]])
- find :
  -- row wise sum ---> np.sum(data,axis=1)   axis=1 for row wise
  -- column wise sum --> np.sum(data,axis=0)  axis=0 for column wise
  -- Minimum Value --> np.min(data)
  -- Maximum Vakue --> np.max(data)
  -- Mean Value --> np.mean(data)


# Task 5: Statistical Operations
- Given 
  - marks=np.array([78,85,90,66,72,88,95,60])
- Calculate:
  1. Mean ---> np.mean()
  2. Median ---> np.median()
  3. Variance ----> np.var()
  4. Standard Deviation ----> np.std()
  5. Mini & maxi marks ----> np.min()   | np.max()
  6. Range(max-min)  ---> max_mark - min_mark  
- print all operations



# Task 6: Percentiles & Sorting
- Given marks array
- Sort ---> np.sort() --> it used to arrange the array in descending order
- for percentile --> np.percentile() --> finds the required percentile values (25th percentile, 50th percentile, 75th percentile)
- Average of marks --> np.mean()
- for count be apply the condtion ---> np.sum(marks>averge)
- print all operation


# Task 7: Mini Use Case : Sales Analysis
- Given daily sales data
   - sales=np.array([1200,1500,900,2000,1800,1700,1600])
- Perform:
  - Total weekly sales ---> np.sum()
  - Average Sales ---> np.mean()
  - Highest & Lowest sales ---> np.min() | np.max()
  - Standard Deviation ---> np.std()
  - Days with above average sales ---> np.where(sales>average_sales)[0]+1  # where +1 mean days starts from 1
- Print all operation


## Learning Objective
- Creating Numpy arrays

- Mathematical operations
  - Addition --> np.sum()
  - Subtact --> np.subtract()
  - Multiple --> np.multiply()
  - Division --> np.divide()
  - Power --> np.power()
  - Square root --> np.sqrt()

- Important Numpy formulas
  - np.array() --> create a array
  - np.linesapce() ---> creates evenly spaced values
  - np.arange() --> creates an array 
  - np.shape() --> Returns dimension of array
  - np.reshape() --> changes the shape of an array
  - np.ones() / np.zeros() --> creates an array filled with ones / zeros
  - np.random.random()  -> creates a random arrays
  - .ravel() --> convert ndim array into 1D array
  - .transpose() / .T  --> convert rows into columns

- Statistical operations
  - Mean --> np.mean()
  - Median --> np.median()
  - Variance --> np.var()
  - Standard Deviation --> np.std()


## How to run
- Requirements

1. Python
2. VS code or other code editor

- Steps:

1. Open the folder in VS code
2. Open the required file
3. Click the run button or open the terminal and run
  