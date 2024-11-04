import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Nice", 20)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

userJSON = json.dumps(user, default=encode_user, indent=4)
print(userJSON)
'''
result:
{
    "name": "Nice",
    "age": 20,
    "User": true
}
'''

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)

'''
result:
<class '__main__.User'>
Nice
'''