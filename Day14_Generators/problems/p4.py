'''
Problem 4: Sum of Squared Numbers using Generator Expression
Task: Using a generator expression, create a generator that yields the squares of numbers from 1 to n. 
Write a function that takes n as input and returns the sum of these squares.

Expected Output: For example, given:
n = 4
The generator should produce 1, 4, 9, 16 and the sum should be 30.
'''
n = 4
squares = [i * i for i in range(1, n + 1)]
for square in squares:
    print(square)

total_sum = sum(squares)
print(total_sum)  

#remember generators are exhausted after one use.