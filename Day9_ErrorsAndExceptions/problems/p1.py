'''
Problem 1: Handle Division by Zero
Write a function that takes two numbers and divides them. 
If a division by zero occurs, handle the exception and return "Cannot divide by zero".

Expected Output:
For example, given:
a = 10
b = 0

The output should be:
"Cannot divide by zero"
'''
a = 10
b = 0
def handleZero(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return f"Cannot divide by zero"

print(handleZero(a, b))