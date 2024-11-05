def myGenerator():
    yield 4
    yield 1
    yield 3

mg = myGenerator()
print(sorted(mg))
#result: [1, 3, 4]

print(sum(mg))
#result: 8

