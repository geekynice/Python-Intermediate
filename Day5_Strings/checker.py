mystring = "hello"
print(mystring.startswith('h'))
print(mystring.startswith('hel'))
print(mystring.startswith('el'))
#result: True
#result: True
#result: False

print(mystring.endswith('o'))
print(mystring.endswith('llo'))
print(mystring.endswith('el'))
#result: True
#result: True
#result: False