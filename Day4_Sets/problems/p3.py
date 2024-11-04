'''
Problem 3: Check for Subset
Write a function that takes two sets and returns True if the first set is a subset of the second, 
and False otherwise.

Expected Output:
For example, given:
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

The output should be:
True
'''

def checkSubset(set1,  set2):
    return set1.issubset(set2)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(checkSubset(set1,  set2))