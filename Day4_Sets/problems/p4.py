'''
Problem 4: Symmetric Difference Between Two Sets
Write a function that takes two sets and returns the symmetric 
difference (elements that are in either of the sets but not in both).

Expected Output:
For example, given:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

The output should be:
{1, 2, 4, 5}
'''

def symmetricDifference(set1, set2):
    return set1.symmetric_difference(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(symmetricDifference(set1, set2))