'''
Problem 3: Encode and Decode a Custom Class
Write a function that encodes a custom class Person into JSON format and decodes it back into a Person object. Use custom encode and decode functions for the process.

Expected Output:
For example, for a class like:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

The encoded JSON should look like:
{
  "name": "Alice",
  "age": 25,
  "Person": true
}
'''
import json
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encodeDecode():
    def encode(o):
        if isinstance(o, Person):
            return {'name': o.name, 'age': o.age}
        else:
            raise TypeError
    def decode(dct):
        if Person.__name__ not in dct:
            return Person(name=dct['name'], age=dct['age'])
        return dct
    
    # Create a Person object
    person = Person("Alice", 25)
    
    personJSON = json.dumps(person, default=encode, indent=4)
    print("Encoded JSON:")
    print(personJSON)

    personDecoded = json.loads(personJSON, object_hook=decode)
    print("\nDecoded Person Object:")
    print(f"Name: {personDecoded.name}, Age: {personDecoded.age}")
        
encodeDecode()