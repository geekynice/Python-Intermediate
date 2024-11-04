'''
Problem 2: Decode a JSON String into a Python Dictionary
Write a function that takes a JSON string and returns the equivalent Python dictionary.

Expected Output:
For example, given:
personJSON = '{"name": "John", "age": 30, "city": "New York"}'

The output should be:
{'name': 'John', 'age': 30, 'city': 'New York'}
'''
import json
personJSON = '{"name": "John", "age": 30, "city": "New York"}'
def decoder(personJSON):
    return json.loads(personJSON)

print(decoder(personJSON))