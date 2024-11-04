mydict = {"name": "Nice", "age" : 20, "city" :"Toronto"}
value = mydict["name"]
print(value)
#result: Nice

for key in mydict:
    print(key)
#result: 
# name
# age
# city

print(mydict.keys())
#result: dict_keys(['name', 'age', 'city'])