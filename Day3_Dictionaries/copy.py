mydict = {'name': 'Nice', 'age': 20, 'city': 'Toronto', 'email': 'nicebanjara@gmail.com'}
mydictcopy = mydict
mydictcopy['address'] = '34. Romulus Drive'
print(mydict)
print(mydictcopy)

#results: {'name': 'Nice', 'age': 20, 'city': 'Toronto', 'email': 'nicebanjara@gmail.com', 'address': '34. Romulus Drive'}
#results: {'name': 'Nice', 'age': 20, 'city': 'Toronto', 'email': 'nicebanjara@gmail.com', 'address': '34. Romulus Drive'}

mydict = {'name': 'Nice', 'age': 20, 'city': 'Toronto', 'email': 'nicebanjara@gmail.com'}
mydictcopy = mydict.copy()
print(mydictcopy)
#results: {'name': 'Nice', 'age': 20, 'city': 'Toronto', 'email': 'nicebanjara@gmail.com'}

mydictcopy = dict(mydict)
print(mydictcopy)
#results: {'name': 'Nice', 'age': 20, 'city': 'Toronto', 'email': 'nicebanjara@gmail.com'}