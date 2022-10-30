# Assignment-3: Functions | Modules

# Game of "Functions"

# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20

# Explanation:

# Summation should like 8+2+3+0+7 = 20

# Should have used function to implement the code - 15

# Must print the Expected output - 15


def sum(list):
    sum1= 0

    for i in list:
        sum1+= i
    return sum1

list=[8, 2, 3, 0, 7]
print(sum(list))

# o/p : 20