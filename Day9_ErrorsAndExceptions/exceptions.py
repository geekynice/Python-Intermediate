try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(e)
else:
    print("It will run if no exception occoured")
finally:
    print("It will run no matter what")
