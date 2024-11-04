from itertools import accumulate

a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))
#result: [1, 3, 6, 10]