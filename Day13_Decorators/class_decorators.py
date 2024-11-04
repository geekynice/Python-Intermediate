class CountClass:
    def __init__(self, func):
        self.func = func
        self.nums_called = 0

    def __call__(self, *args, **kwargs):
        self.nums_called += 1
        print(f'This function is called {self.nums_called} times.')
        return self.func(*args, **kwargs)
    
@CountClass
def sayhello():
    print("Hi Nice!")

sayhello()
sayhello()
sayhello()
sayhello()

'''
result: 
This function is called 1 times.
Hi Nice!
This function is called 2 times.
Hi Nice!
This function is called 3 times.
Hi Nice!
This function is called 4 times.
Hi Nice!
'''