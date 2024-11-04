'''
Problem 3: Shuffle a List
Write a function that takes a list and shuffles the elements in place. Print the shuffled list.

Expected Output:
For example, given:
mylist = [1, 2, 3, 4, 5]

The shuffled output could be:
[3, 5, 1, 4, 2]
'''
import random
mylist = [1, 2, 3, 4, 5]

def shuffler(mylist):
    random.shuffle(mylist)
    return mylist

print(shuffler(mylist))