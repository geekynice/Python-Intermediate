import json

person = {"name":"Nice",
          "age": 20,
          "unemployed": True,
          "address": "34 Romulus Drive"
          }

personJSON = json.dumps(person, indent=4)
print(personJSON)

'''
result:
{
    "name": "Nice",
    "age": 20,
    "unemployed": true,
    "address": "34 Romulus Drive"
}
'''