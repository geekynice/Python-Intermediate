'''
Problem 4: Class Decorator for Counting Function Calls
Write a class decorator CountCalls that counts how many times a decorated function is called 
and prints the count each time the function is executed.

Expected Output:
Given:
@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()

The output should be:
This function is called 1 times.
Hello!
This function is called 2 times.
Hello!
'''
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.occourence = 0

    def __call__(self, *args, **kwargs):
        self.occourence += 1
        print(f'This function is called {self.occourence} times.')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
