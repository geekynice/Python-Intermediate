'''
Problem 3: Find Accumulated Sums
Write a function that takes a list of numbers and returns the accumulated sum of elements using itertools.accumulate().

Expected Output:
For example, given:
a = [1, 2, 3, 4]

The output should be:
[1, 3, 6, 10]
'''
from itertools import accumulate
a = [1, 2, 3, 4]
def accumulateSums(a):
    return list(accumulate(a))

print(accumulateSums(a))