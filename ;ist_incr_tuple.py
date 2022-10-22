# Assignment-2: List | Tuples | Dictionaries

    # Write a Python program to get a list, sorted in increasing order by the
    # last element in each tuple from a given list of non-empty tuples

    # Print the expected output - 50

    # Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

tuple1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list1 = len(tuple1)

for i in range(0, list1):
	for j in range(0, list1-i-1):
		if (tuple1[j][-1] > tuple1[j + 1][-1]):
			temp = tuple1[j]
			tuple1[j]= tuple1[j + 1]
			tuple1[j + 1]= temp

print(tuple1)

# o/p : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]