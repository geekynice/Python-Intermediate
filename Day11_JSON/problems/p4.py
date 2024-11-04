'''
Problem 4: Parse JSON with a List of Dictionaries
Write a function that parses a JSON string containing a list of dictionaries. 
Each dictionary represents a person's details.

Expected Output:
For example, given:
'[{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]'

The function should return:
[{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
'''
import json
myjson = '[{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]'

def parser(myjson):
    return json.loads(myjson)

print(parser(myjson))