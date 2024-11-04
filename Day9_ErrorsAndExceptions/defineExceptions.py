class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self,message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value Too High")
    elif x < 5:
        raise ValueTooLowError("Value too low", x)
    
try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(f"Message: {e.message} and value is {e.value}")