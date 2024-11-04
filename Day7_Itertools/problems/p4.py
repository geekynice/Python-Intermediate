'''
Problem 4: Group Elements by Parity
Write a function that takes a list of numbers and groups them by whether they are even or odd using itertools.groupby().

Expected Output:
For example, given:
a = [1, 2, 2, 3, 4, 4, 5]

The output should be:
1 [1]
2 [2, 2]
3 [3]
4 [4, 4]
5 [5]
'''
from itertools import groupby
a = [1, 2, 2, 3, 4, 4, 5]
def parity(a):
    group_obj = groupby(a)
    for key, value in group_obj:
        print(key, list(value))

(parity(a))