'''
Problem 1: Decorator for Timing a Function
Write a decorator called timing_decorator that measures and prints the time taken for a function to execute.

Expected Output:
For example, if you have:
@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function complete")

slow_function()

The output should be:
Function complete
Execution time: 2.002 seconds
'''
import time
def timing_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        timing = end-start
        print(f'Execution time: {timing} seconds')
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function complete")

slow_function()