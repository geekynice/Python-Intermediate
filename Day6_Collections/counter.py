from collections import Counter

string = "aaaabbbcc"
my_counter = Counter(string)
print(my_counter)
#result: Counter({'a': 4, 'b': 3, 'c': 2})

print(my_counter.elements())
#result: <itertools.chain object at 0x100c67ee0>, it returns an itertools which can further be used as iterable.

print(my_counter.most_common())
#result: [('a', 4), ('b', 3), ('c', 2)], it returns the most common

print(my_counter.most_common(1))
#result: [('a', 4)]

print(my_counter.most_common(1)[0][0])
#result: a

print(my_counter.values())
#result: dict_values([4, 3, 2])