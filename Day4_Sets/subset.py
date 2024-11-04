setA = {1, 2, 3, 5, 6}
setB = {2, 3, 4, 7, 8}

#to check if it is  a subset
print(setA.issubset(setB))
#result: False

if setA.issubset(setB):
    print("Yes")
else:
    print("No")
#result: No

setA = {1, 2, 3, 5, 6}
setB = {1, 2, 3, 5, 6, 7}

#to check if it is  a subset
print(setA.issubset(setB))
#result: True