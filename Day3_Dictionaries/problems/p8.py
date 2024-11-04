'''
Problem: Filter Dictionary by Value
Write a function that takes a dictionary and a threshold value. 
The function should return a new dictionary that only contains the key-value pairs 
where the value is greater than the given threshold.

Expected Output:
For example, given:
mydict = {'a': 10, 'b': 20, 'c': 30, 'd': 5}
threshold = 15

The output should be:
{'b': 20, 'c': 30}
'''

def filterDict(mydict, thresold):
    new_dict = {}
    for key, value in mydict.items():
        if value > thresold:
            new_dict[key]= value
    return new_dict


mydict = {'a': 10, 'b': 20, 'c': 30, 'd': 5}
threshold = 15

print(filterDict(mydict, threshold))