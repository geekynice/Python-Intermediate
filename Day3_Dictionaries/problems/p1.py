'''
Problem 1: Find the Key with Maximum Value
Write a function that takes a dictionary of key-value pairs (where the values are integers) 
and returns the key with the largest value. If the dictionary is empty, return None.

Expected Output:
For example, given:
mydict = {'a': 10, 'b': 35, 'c': 25}

The output should be:
'b'
'''



def largest(mydict):
    if not mydict:
        return None
    else:
        maximum = max(mydict, key=mydict.get)
        print(maximum)

mydict = {'a': 10, 'b': 35, 'c': 25}
largest(mydict)