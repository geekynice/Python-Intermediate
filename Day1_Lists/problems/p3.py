'''
Problem 3: Find the Second Largest Element
Write a function that finds and returns the second largest element in a given list of numbers.
If the list has fewer than two distinct numbers, return None.

Expected Output
If you are given:
my_list = [12, 35, 1, 10, 34, 1]

The output should look like:
34
'''
my_list = [12, 35, 1, 10, 34, 34, 1]
max_num = max(my_list)
my_list.remove(max_num)
second_max_num = max(my_list)
print(second_max_num)





