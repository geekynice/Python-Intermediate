setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.update(setB)
print("Update: ", setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.intersection_update(setB)
print("Intersection Update: ", setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.difference_update(setB)
print("Difference Update: ", setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.symmetric_difference_update(setB)
print("Symmetric Difference Update: ", setA)

'''
result:
Update:  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, joins all and removes duplicates
Intersection Update:  {1, 2, 3}, returns the same elements only
Difference Update:  {4, 5, 6, 7, 8, 9}, removes the same elements and returns  remaining of setA
Symmetric Difference Update:  {4, 5, 6, 7, 8, 9, 10, 11, 12}, removes similar elements from both sets and merges the remaining.
'''