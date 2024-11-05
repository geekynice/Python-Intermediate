'''
Problem 1: Simple Sequence Generator
Task: Write a generator function simple_sequence(n) that yields numbers from 0 up to but not including n. 
Use this generator in a loop to print the numbers.

Expected Output: For example, given:
n = 5

The output should be:
0
1
2
3
4
'''

def simple_sequence(n):
    initial = 0
    while initial < n:
        yield initial
        initial += 1
ss = simple_sequence(5)

for i in ss:
    print(i)