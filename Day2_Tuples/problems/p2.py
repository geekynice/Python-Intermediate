'''
Problem 2: Count Occurrences of All Elements in a Tuple
Write a function that takes a tuple of integers and returns a dictionary 
where the keys are the elements from the tuple and the values are the 
number of times each element appears in the tuple.

Expected Output
If you are given:
mytuple = (3, 5, 6, 3, 5, 5, 9)

The output should look like:
{3: 2, 5: 3, 6: 1, 9: 1}
'''

mytuple = (3, 5, 6, 3, 5, 5, 9)

for item in mytuple:
    count = mytuple.count(item)
    print(f'{item}: {count}')