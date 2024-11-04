'''
Problem 5: Find the Missing Numbers
Write a function that takes two sets: one representing a full set of numbers and 
the other representing a subset of it with some numbers missing. Your task is to return 
a new set containing the numbers that are missing from the second set.

Expected Output:
For example, given:
full_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
subset = {1, 2, 3, 5, 7}

The output should be:
{4, 6, 8, 9}
'''

full_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
subset = {1, 2, 3, 5, 7}

def missing_number(full_set, subset):
    missing_number = full_set.difference(subset)
    return missing_number

print(missing_number(full_set, subset))