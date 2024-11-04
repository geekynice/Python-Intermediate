def my_decorator_function(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@my_decorator_function
def doSomething():
    print('Nice')

doSomething()
'''
result:
Start
Nice
End
'''
# def add_all(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper

# @add_all
# def addNumbers(x):
#     return x + 5

# addNumbers(5)
'''
TypeError: my_decorator_function.<locals>.wrapper() takes 0 positional arguments but 1 was given
# We got the error because our decorator function is not aware about arguments that our addNumber() function takes
'''
def add_all(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@add_all
def addNumbers(x):
    return x + 5

print(addNumbers(5))
'''
result: 
Start
End
10
'''