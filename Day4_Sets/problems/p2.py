'''
Problem 2: Set Difference
Write a function that takes two sets and returns a new set containing elements that
are present in the first set but not in the second set.

Expected Output:
For example, given:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

The output should be:
{1, 2}
'''

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

def diff(set1, set2):
    new_set = set1.difference(set2)
    return new_set

print(diff(set1, set2))