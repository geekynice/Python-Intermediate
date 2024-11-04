'''
Problem 1: Encode a Dictionary to JSON
Write a function that takes a dictionary and returns its JSON representation, formatted with an indentation of 2 spaces.

Expected Output:
For example, given:
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

The output should be:
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
'''
import json
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
def jsonify(person):
    return json.dumps(person,  indent=2)

print(jsonify(person))