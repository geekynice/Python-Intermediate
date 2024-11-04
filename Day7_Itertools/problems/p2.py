'''
Problem 2: Find the Cartesian Product of Two Lists
Write a function that takes two lists and returns the cartesian product of those lists using itertools.product().

Expected Output:
For example, given:
a = [1, 2]
b = [3, 4]

The output should be:
[(1, 3), (1, 4), (2, 3), (2, 4)]
'''
from itertools import product
a = [1, 2]
b = [3, 4]

def cartesianProduct(a, b):
    return list(product(a, b))

print(cartesianProduct(a, b))