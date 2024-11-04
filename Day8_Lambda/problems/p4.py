'''
Problem 4: Find the Product of a List of Numbers
Write a function that takes a list of numbers and returns the product of all the elements using lambda and reduce().

Expected Output:
For example, given:
a = [1, 2, 3, 4]

The output should be:
24
'''
from functools import reduce
a = [1, 2, 3, 4]
def product(a):
    return reduce(lambda x,y:x*y, a)

print(product(a)) 