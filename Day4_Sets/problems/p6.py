'''
Problem 6: Count Unique Elements in a List Using Sets
Write a function that takes a list and returns the number of unique elements in the list using sets. 
Your task is to convert the list to a set and count the number of elements.

Expected Output:
For example, given:
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]

The output should be:
7
'''

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]

def counter(my_list):
    my_list = set(my_list)
    return len(my_list)

print(counter(my_list))