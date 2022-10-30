# Assignment-3: Functions | Modules

# Calculate the Upper and The lower Case

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.



# Sample String : 'The quick Brow Fox'

# Expected Output :

# No. of Upper case characters : 3

# No. of Lower case Characters : 12


# The code must be implemented using Function - 15

# The function must accept the string - 15

# Count of upper-case characters must be printed - 5

# count of lower case character must be printed - 5

def upper_lower(s):      
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : ",upper)
    print("No. of Lower case characters : ",lower)

upper_lower("The quick Brow Fox")

# o/p : 
# No. of Upper case characters :  3
# No. of Lower case characters :  12