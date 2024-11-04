'''
Problem 3: Find the Largest and Smallest Element in a Tuple
Write a function that takes a tuple of integers and returns the largest and smallest elements in the tuple.

Expected Output
If you are given:
mytuple = (8, 2, 5, 1, 10)

The output should look like:
Largest: 10
Smallest: 1
'''
def finders(mytuple):
    maximum = max(mytuple)
    minimum = min(mytuple)
    print(f'Largest: {maximum}, Smallest: {minimum}')

mytuple = (8, 2, 5, 1, 10)
finders(mytuple)