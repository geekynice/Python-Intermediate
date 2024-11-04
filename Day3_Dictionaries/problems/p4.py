'''
Problem 4: Remove Keys with Specific Values
Write a function that takes a dictionary and a list of values. 
The function should remove all the keys from the dictionary whose values are in the given list of values.

Expected Output:
For example, given:
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
values_to_remove = [2, 4]

The output should be:
{'a': 1, 'c': 3}
'''


def removal(mydict, values_to_remove):
    keys_to_remove = []
    for key, value in mydict.items():
        if value in values_to_remove:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del mydict[key]

    print(mydict)

mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
values_to_remove = [2, 4]
removal(mydict, values_to_remove)