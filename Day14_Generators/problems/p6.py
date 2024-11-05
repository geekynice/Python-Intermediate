'''
Problem 6: Chunked Data Generator
Task: Write a generator function chunked(data, size) that takes a list data and an integer size, 
yielding chunks of size elements at a time from data.

Expected Output: For example, given:
data = [1, 2, 3, 4, 5, 6, 7, 8]
size = 3

The output should be:
[1, 2, 3]
[4, 5, 6]
[7, 8]
'''

def chunked(data, size):
    for i in range(0,  len(data), size):
        yield data[i:i+size]

data = [1, 2, 3, 4, 5, 6, 7, 8]
size = 3
for chunk in chunked(data, size):
    print(chunk)