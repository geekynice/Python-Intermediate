'''
Problem 1: Generate All Permutations of a List
Write a function that takes a list and generates all possible permutations 
of length n using itertools.permutations().

Expected Output:
For example, given:
a = [1, 2, 3]
n = 2

The output should be:
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
'''
from itertools import permutations
a = [1, 2, 3]
n = 2

def generatePerm(a, n):
    perm = permutations(a, n)
    return list(perm)

print(generatePerm(a, n))