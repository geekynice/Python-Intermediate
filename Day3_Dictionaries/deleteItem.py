mydict = {'name': 'Nice', 'age': 20, 'city': 'Toronto', 'email': 'nicebanjara@gmail.com'}
del mydict['email']
print(mydict)
#results: {"name": "Nice", "age" : 20, "city" :"Toronto"}

mydict.pop('age')
print(mydict)
#results: {"name": "Nice", "city" :"Toronto"}

mydict.popitem()
print(mydict)
#results: {"name": "Nice"}