mytuple = ("Nice", 20, "Toronto")

name, age, city = mytuple
print(f'Name:  {name}, Age:  {age}, City:  {city}')
#result: Name:  Nice, Age:  20, City:  Toronto

name, age = mytuple
print(f'Name:  {name}, Age:  {age}')
# #result: ValueError: too many values to unpack (expected 2)

name, age, city, what = mytuple
print(f'Name:  {name}, Age:  {age}, City:  {city}')
#result: ValueError: not enough values to unpack (expected 4, got 3)