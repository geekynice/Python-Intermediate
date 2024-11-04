'''
Problem 1: Swapping Variables Using Tuples
Write a Python function that takes two variables and swaps their values using tuples. 
You should not use any extra variables, just tuple packing and unpacking.

Expected Output
If you are given:
a = 5
b = 10

The output should look like:
a = 10
b = 5
'''

def swapper(a, b):
    a, b =  b,  a
    print(a,  b)

swapper(5, 10)