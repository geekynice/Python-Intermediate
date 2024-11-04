setA = {1, 2, 3, 4, 5}
setB = {2, 4, 6, 8, 10}

difference = setA.difference(setB)
symmetric_difference = setA.symmetric_difference(setB)
print("Difference: ", difference)
print("Symmetric Difference: ", symmetric_difference)

'''
result:
Difference:  {1, 3, 5}, this method removes all the elements of setA that is found in setB
Symmetric Difference:  {1, 3, 5, 6, 8, 10}, this method removes all the elements of setA that is found in setB & merges the remaining
'''