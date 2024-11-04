'''
Problem 3: Custom Exception for Age
Write a custom exception AgeTooLowError and create a function that raises this exception if a user’s age is below 18. 
Catch the exception and print "Age is too low".

Expected Output:
For example, given:
age = 16

The output should be:
"Age is too low"
'''
age = 16
class AgeTooLowError(Exception):
    def __init__(self, message, age):
        self.message = message
        self.age = age

def test_age(age):
    if age < 18:
        raise AgeTooLowError("Age is too low.",  age)
    else:
        pass

try:
    test_age(age)
except AgeTooLowError as e:
    print(f"Age is too low {e.age}")