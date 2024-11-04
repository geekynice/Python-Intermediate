'''
Problem 2: Random Element from a List
Write a function that takes a list of items and returns a 
random element from that list using the random.choice() method.

Expected Output:
For example, given:
mylist = ['apple', 'banana', 'cherry', 'date']
'''
import random
mylist = ['apple', 'banana', 'cherry', 'date']
def randomElement(mylist):
    return random.choice(mylist)

print(randomElement(mylist))