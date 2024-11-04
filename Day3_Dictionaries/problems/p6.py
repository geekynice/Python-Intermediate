'''
Problem 6: Find the Most Frequent Value
Write a function that takes a dictionary and returns the value that appears the most frequently. 
If multiple values have the same frequency, return any one of them.

Expected Output:
For example, given:
mydict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 2}

The output could be:
2
'''

def frequency(mydict):
    new_dict = {}
    for key, value in mydict.items():
        if value in new_dict:
            new_dict[value] +=1
        else:
            new_dict[value] = 1
    max_freq = max(new_dict, key=new_dict.get)
    return max_freq


mydict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 2}
print(frequency(mydict))