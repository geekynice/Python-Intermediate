a = [1, 2, 3, 4, 5]
b = filter(lambda x: x%2 == 0,  a)
print(list(b))
#result: [2, 4]