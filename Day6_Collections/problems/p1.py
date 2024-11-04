'''
Problem 1: Most Frequent Element Using Counter
Write a function that takes a list of elements and returns the most frequent element 
using the Counter from collections.

Expected Output:
For example, given:
elements = [1, 2, 2, 3, 3, 3, 4]

The output should be:
3
'''
from collections import Counter
elements = [1, 2, 2, 3, 3, 3, 4]

def frequentElement(elements):
    count = Counter(elements)
    return count.most_common(1)[0][0]

print(frequentElement(elements))