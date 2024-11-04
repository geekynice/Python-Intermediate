myset = {1, 4, 5, 7, 8}
print(myset)
#result: {1, 4, 5, 7, 8}

myset.remove(1)
print(myset)
#result: {4, 5, 7, 8}, removes the desired item

myset.discard(8)
print(myset)
#result: {4, 5, 7}, removes the desired item

myset.pop()
print(myset)
#result: {5, 7}, removes the first item

myset.clear()
print(myset)
#result: set(), clears the set