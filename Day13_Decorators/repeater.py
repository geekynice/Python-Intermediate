import functools

def repeater(num_times):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat_decorator

@repeater(num_times=4)
def greet(name):
    print(f'Hi! {name}')

greet('Nice')

'''
result: 
Hi! Nice
Hi! Nice
Hi! Nice
Hi! Nice
'''