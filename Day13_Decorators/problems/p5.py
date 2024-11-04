'''
Problem 5: Decorator with Arguments
Create a decorator repeat_decorator that takes an argument n and repeats the execution of the function n times.

Expected Output:
For example:
@repeat_decorator(n=3)
def say_hi():
    print("Hi!")

say_hi()

The output should be:
Hi!
Hi!
Hi!
'''
import functools

def repeat_decorator(n):
    def repeater(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeater

@repeat_decorator(n=3)
def say_hi():
    print("Hi!")

say_hi()