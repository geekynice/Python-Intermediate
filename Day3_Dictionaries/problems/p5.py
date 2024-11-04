'''
Problem 5: Invert a Dictionary
Write a function that takes a dictionary where keys are unique, 
but values might not be. The function should return a new dictionary 
where the keys are the original values, and the values are lists of 
keys from the original dictionary that had that value.

Expected Output:
For example, given:
mydict = {'a': 1, 'b': 2, 'c': 1, 'd': 2}

The output should be:
{1: ['a', 'c'], 2: ['b', 'd']}
'''

def grouping(mydict):
    inverted_dict = {}
    for key, value in mydict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key] 
    return inverted_dict

mydict = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
print(grouping(mydict))