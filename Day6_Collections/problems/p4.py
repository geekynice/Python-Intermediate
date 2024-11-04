'''
Problem 4: Double-Ended Queue Operations
Write a function that takes a list of numbers and performs the following operations using deque:

1. Append all elements to the right.
2. Remove an element from the left.
3. Rotate the deque by 2.

Expected Output:
For example, given:
numbers = [1, 2, 3, 4, 5]

The output should be:
deque([4, 5, 2, 3])
'''
from collections import deque

numbers = [1, 2, 3, 4, 5]

def dequeOperations(numbers):
    d = deque()
    d.extend(numbers)
    d.popleft()
    d.rotate(2)
    return d

print(dequeOperations(numbers))