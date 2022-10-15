#---------------------------------#
# Assignment-1: Operators | Loops :
#---------------------------------#

        # Write a Python program that accepts a word from the user and reverse it.

        # Sample Test Case

        # Input : Edyoda

        # output: adoydE


# Approach : 1

while True:
    user_input = input("Enter the word to reverse : ") # Promt to user
    if (user_input.strip().isdigit() or user_input == ""): # validating for empty string and numbers.
        print("You entered Nothing OR number as word mistakenly, please enter word only ")
        continue
    else:
        print("Your word : ", user_input)
        break 

# Logic to reverse the string.
reversed_str = "" # to store charecter from right to left of original string.

for string_chr in user_input: # string is iterable
    reversed_str = string_chr + reversed_str # concatinating charecters.
    
print("Reversed Word : ",reversed_str)  

    # o/p : 
        # Enter the word to reverse : EdYoda
        # Your word :  EdYoda
        # Reversed Word :  adoYdE

