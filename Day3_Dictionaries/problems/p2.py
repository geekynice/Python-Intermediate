'''
Problem 2: Merge Two Dictionaries
Write a function that takes two dictionaries and merges them. 
If both dictionaries have the same key, the value in the second dictionary should 
overwrite the value from the first dictionary.

Expected Output:
For example, given:
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'age': 30, 'city': 'New York'}

The output should be:
{'name': 'Alice', 'age': 30, 'city': 'New York'}
'''

dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'age': 30, 'city': 'New York'}

dict1.update(dict2)
print(dict1)