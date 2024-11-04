from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d)
print(d['a'])
print(d['c'])
#result: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
#result: 1
#result: 0, because it provides default value of int if key is not found