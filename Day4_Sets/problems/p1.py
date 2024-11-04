'''
Problem 1: Find Common Elements Between Two Sets
Write a function that takes two sets and returns a new set containing only the elements that are present in both sets.

Expected Output:
For example, given:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

The output should be:
{3, 4}
'''

def intersection(set1, set2):
    return  set1.intersection(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(intersection(set1, set2))