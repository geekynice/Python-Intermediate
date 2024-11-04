myset = {1, 4, 5, 7, 8}
print(myset)
#result: {1, 4, 5, 7, 8}

myset.add(9)
print(myset)
#result: {1, 4, 5, 7, 8, 9}

myset.add(8)
print(myset)
#result: {1, 4, 5, 7, 8, 9}, it didn't change because 6 is already present in previous set and set doesn't allow duplicates