"""
Problem 1: Merge and Sort Lists

You are given two lists of integers. Your task is to merge the two lists into one
list and sort the merged list in ascending order. 
The output should be a single sorted list.

Expected Output
If you are given:
list1 = [5, 8, 2]
list2 = [1, 9, 3]

The output should look like:
[1, 2, 3, 5, 8, 9]
"""

list1 = [5, 8, 2]
list2 = [1, 9, 3]

new_list = list1 + list2
new_list.sort()
print(new_list)