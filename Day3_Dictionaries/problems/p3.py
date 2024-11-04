'''
Problem 3: Count Occurrences of Values
Write a function that takes a dictionary and counts how many times each value appears. 
Return a new dictionary where the keys are the values from the original dictionary and 
the values are their respective counts.

Expected Output:
For example, given:
mydict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

The output should be:
{1: 2, 2: 2, 3: 1}
'''


def counting(mydict):
    values = mydict.values()
    mytuple = tuple(values)
    dict1 = {}
    for item in mytuple:
        if item in dict1:
            continue
        else:
            count = mytuple.count(item)
            dict1[item] = count
    print(dict1)

mydict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
counting(mydict)