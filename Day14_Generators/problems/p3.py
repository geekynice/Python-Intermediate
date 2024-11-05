'''
Problem 3: Fibonacci Generator
Task: Create a generator function fibonacci(n) that yields the first n numbers in the Fibonacci sequence. Test it by printing the generated numbers.

Expected Output: For example, given:
n = 6

The output should be:
0
1
1
2
3
5
'''

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
        
fb = fibonacci(6)
for i in fb:
    print(i)