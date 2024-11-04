'''
Problem: Find Common Keys in Two Dictionaries
Write a function that takes two dictionaries and returns a list of keys that are present in both dictionaries.

Expected Output:
For example, given:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

The output should be:
['b', 'c']
'''

def commonFinder(dict1, dict2):
    common_list = []
    for key in dict1:
        if key in dict2:
            common_list.append(key)
    return common_list
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

print(commonFinder(dict1, dict2))