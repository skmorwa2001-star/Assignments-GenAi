# Task 4: File Reader with Exception Handling

## Ask user to enter the filename
filename=input("Enter the filename: ")

try:
    ## Open the file and read data
    with open(filename,'r') as file:
        ## Print the first 3 lines of the file
        for i in range(3):
            line=file.readline()
            if line=="":
                break
            print(line.strip())

## It is used if the file is not found
except FileNotFoundError:
    print("Error: File is Not Found")

## It is used if the the file permission denied
except PermissionError:
    print("Error: Permission Denied")

finally:
    print("File operation attempted")    
