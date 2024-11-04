'''
Problem 3: Nested Decorators for Logging and Timing
Create two decorators, log_decorator and timing_decorator, and apply both to a function.
log_decorator should log the function name and arguments, 
and timing_decorator should measure the time taken for the function to execute.

Expected Output:
For example:
@log_decorator
@timing_decorator
def greet(name):
    print(f"Hello, {name}!")
greet("John")

The output should include:
Calling greet('John')
Hello, John!
'greet' returned None
Execution time: 0.001 seconds
'''
import functools
import time
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        timing = end-start
        print(f'Execution time: {timing:.3f} seconds')
        return result
    return wrapper

@log_decorator
@timing_decorator
def greet(name):
    print(f"Hello, {name}!")
greet("John")