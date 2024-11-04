'''
Problem 1: Random Float and Integer
Write a function that generates and returns a random float between 1 and 10, and a random integer between 1 and 100.

Expected Output:
For example:
Random float: 7.54
Random integer: 54
'''
import random

def randomNumberGenerator():
    return f'Random float: {random.uniform(1, 10)}\nRandom integer: {random.randint(1, 100)}'

print(randomNumberGenerator())