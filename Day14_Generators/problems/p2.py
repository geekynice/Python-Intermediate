'''
Problem 2: Infinite Even Number Generator
Task: Write a generator function even_numbers() that generates even numbers indefinitely, starting from 0.
Use next() to print the first 5 even numbers.

Expected Output:
0
2
4
6
8
'''

def even_numbers():
    i = 0
    while True:
        yield i
        i += 2

even = even_numbers()

value = next(even)
print(value)
value = next(even)
print(value)
value = next(even)
print(value)
value = next(even)
print(value)
value = next(even)
print(value)