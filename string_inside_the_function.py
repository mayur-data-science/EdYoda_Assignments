# Assignment-3: Functions | Modules

# Write a Python program to reverse a string.

# Sample String : "1234abcd"

# Expected Output : "dcba4321"

# Should have used the function in the code - 15

# Must get the expected output - 15

def reverse(str):    
    string = " "    
    for i in str:        
        string = i + string    
    return string
str = "1234abcd"
print("The original string is:",str)
print("The reverse string is:", reverse(str)) 

# o/p :
    # The original string is: 1234abcd
    # The reverse string is: dcba4321 