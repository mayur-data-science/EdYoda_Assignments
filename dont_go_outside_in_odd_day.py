#---------------------------------#
# Assignment-1: Operators | Loops :
#---------------------------------#

        # Write a Python program to count the number of even and odd numbers from a series of numbers.
        
        # Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

        # Expected Output :

        # Number of even numbers : 4

        # Number of odd numbers : 5

# Approach : 1 (Using for)
sequence_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Declaring the list
odd_counter = 0
even_counter = 0

for x in sequence_list:
    if not x % 2: # 1(True) and 0(False) # not True is False # not False is True
        even_counter+=1	# incrimenting counter variable
    else:
        odd_counter+=1	# incrementing counter variable

print("Number of even numbers : {0}".format(even_counter))
print("Number of odd numbers :{0}".format(odd_counter))

    # o/p : 
        # Number of even numbers : 5
        # Number of odd numbers :5



# Approach : 2(using while)

sequence_tuple = (66, 45, 12, 18, 68, 65, 37, 25, 120, 307)

even_counter = odd_counter = 0
i = 0

while (i < len(sequence_tuple)):
    if(sequence_tuple[i] % 2 == 0):
        even_counter = even_counter + 1
    else:
        odd_counter = odd_counter + 1
    i = i + 1

print("The Count of Even Numbers in sequence_tuple = ", even_counter)
print("The Count of Odd  Numbers in sequence_tuple = ", odd_counter)


    # o/p :
        # The Count of Even Numbers in sequence_tuple =  5
        # The Count of Odd  Numbers in sequence_tuple =  5