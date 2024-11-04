import json

person = {"name":"Nice",
          "age": 20,
          "unemployed": True,
          "address": "34 Romulus Drive"
          }

personJSON = json.dumps(person, indent=4)
person = json.loads(personJSON)
print(person)
print(type(person))

'''
result:
{'name': 'Nice', 'age': 20, 'unemployed': True, 'address': '34 Romulus Drive'}
<class 'dict'>
'''