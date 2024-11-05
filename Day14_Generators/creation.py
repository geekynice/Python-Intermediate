def myGenerator():
    yield 1

g = myGenerator()
print(g)
#result: <generator object myGenerator at 0x10486b530>

value = next(g)
print(value)
#result: 1

value = next(g)
print(value)
#result: StopIteration error: because the next function only looks for value called after it,
#and in our case, we dont have any more value after 1.