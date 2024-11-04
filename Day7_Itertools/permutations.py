from itertools import permutations

a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))
#result: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

perm = permutations(a, 3)
print(list(perm))
#result: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations(a)
print(list(perm))
#result: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]