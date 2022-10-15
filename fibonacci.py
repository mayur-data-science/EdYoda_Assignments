#---------------------------------#
# Assignment-1: Operators | Loops :
#---------------------------------#

        # Write a Python program to get the Fibonacci series between 0 to 50

        # Note : The Fibonacci Sequence is the series of numbers :
                                # 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

        # Every next number is found by adding up the two numbers before it.

        # Expected Output : 1 1 2 3 5 8 13 21 34

# Approach : 1 ( pythonic way )

previous_number, next_number  = 0, 1 # initializing first two number of the Sequence.(tuple unpacking)

    # By default, the print function ends with a newline
    # end default parameter end=' ' indicates that the end character has to be identified by whitespace and not a newline.
print("Fibonacci Series Between 0 to 50 : ", previous_number, next_number, end=' ') 

for iteration in range(0,8): # range() generator only used for iteration purpose.
    fib_number = previous_number + next_number # calculating fibonacci number by adding previous number and next number.
    previous_number, next_number = next_number, fib_number # tuple unpacking
    print(fib_number, end=" ") # if we don't use end here only 1st iteration o/p printed in same line, rest every iteration o/p in new line.
print() # ignore, its for 2nd Approach o/p to print in next line.

# o/p : Fibonacci Series Between 0 to 50 :  0 1 1 2 3 5 8 13 21 34





# Approach : 2 (requires more line of code)

previous_number = 0
next_number = 1

print("Fibonacci Series Between 0 to 50 : ", previous_number, next_number, end=' ')

for iteration in range(0,8):
    fib_number = previous_number + next_number
    previous_number = next_number
    next_number = fib_number
    print(fib_number, end=" ")

# o/p : Fibonacci Series Between 0 to 50 :  0 1 1 2 3 5 8 13 21 34


