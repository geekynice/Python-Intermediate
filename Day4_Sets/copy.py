setA = {1, 2, 3, 4, 5,  6}
setB = setA
print(setB)
#result : {1, 2, 3, 4, 5, 6}

#for actual copy
setB = setA.copy()
print(setB)
#result : {1, 2, 3, 4, 5, 6}

setB = set(setA)
print(setB)
#result : {1, 2, 3, 4, 5, 6}
