def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fb = fibonacci(20)
for i in fb:
    print(i)

'''
result:
0
1
1
2
3
5
8
13
'''