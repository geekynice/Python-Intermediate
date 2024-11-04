setA = {1, 2, 3, 5, 6}
setB = {7, 8, 9, 10}

#to check if it is  a subset
print(setA.isdisjoint(setB))
#result: True

if setA.isdisjoint(setB):
    print("Yes")
else:
    print("No")
#result: No

setA = {1, 2, 3, 5, 6}
setB = {1, 2, 3, 5, 6, 8}

#to check if it is  a subset
print(setA.isdisjoint(setB))
#result: False 