'''
Problem 2: Double the Elements of a List
Write a function that takes a list of numbers and doubles each element using lambda and map().

Expected Output:
For example, given:
a = [1, 2, 3, 4, 5]

The output should be:
[2, 4, 6, 8, 10]
'''
a = [1, 2, 3, 4, 5]
def doubleIt(a):
    return list(map(lambda x:x*2, a))

print(doubleIt(a))