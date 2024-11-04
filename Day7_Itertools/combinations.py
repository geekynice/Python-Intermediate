from itertools import combinations

a = [1, 2, 3, 4]
cmb = combinations(a, 2)
print(list(cmb))
#result: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

cmb = combinations(a, 3)
print(list(cmb))
#result: [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

cmb = combinations(a, 4)
print(list(cmb))
#result: [(1, 2, 3, 4)]