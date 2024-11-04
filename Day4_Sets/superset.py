setA = {1, 2, 3, 5, 6}
setB = {2, 3, 4, 7, 8}

#to check if it is  a subset
print(setA.issuperset(setB))
#result: False

if setA.issuperset(setB):
    print("Yes")
else:
    print("No")
#result: No

setA = {1, 2, 3, 5, 6}
setB = {1, 2, 3, 5, 6}

#to check if it is  a subset
print(setA.issuperset(setB))
#result: True