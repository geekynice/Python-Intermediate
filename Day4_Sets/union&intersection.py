odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}

union = odds.union(evens)
intersection  = odds.intersection(evens)

print("Union: ", union)
print("Intersection: ", intersection)

'''
result:
Union:  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Intersection:  set(), it is because it didnot found any common number
'''

setA = {1, 2, 3, 4, 5}
setB = {2, 4, 6, 8, 10}

union = setA.union(setB)
intersection  = setA.intersection(setB)

print("Union: ", union)
print("Intersection: ", intersection)

'''
result:
Union:  {1, 2, 3, 4, 5, 6, 8, 10}, see how it doesn't take duplicates
Intersection:  {2, 4}
'''