dict1 = {"name": "Nice", "age": 28, "city": "Toronto"}
dict2 = dict(name="New Name", age=28, email='nicebanjara@gmail.com')

dict1.update(dict2)
print(dict1)
#result: {'name': 'New Name', 'age': 28, 'city': 'Toronto', 'email': 'nicebanjara@gmail.com'}

'''So what happend here is previous values which matches will be replacedd and overwritten by the 
new dictionary and the new pairs from the new dictionary will be added'''

mytuple  = (3, 2)
mydict = {mytuple: 13}
print(mydict)
#result: {(3, 2): 13}