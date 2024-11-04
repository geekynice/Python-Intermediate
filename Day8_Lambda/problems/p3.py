'''
Problem 3: Filter Even Numbers from a List
Write a function that takes a list of numbers and filters out the even numbers using lambda and filter().

Expected Output:
For example, given:
a = [1, 2, 3, 4, 5, 6]

The output should be:
[2, 4, 6]
'''
a = [1, 2, 3, 4, 5, 6]
def filterEven(a):
    return list(filter(lambda x:x%2==0, a))

print(filterEven(a))