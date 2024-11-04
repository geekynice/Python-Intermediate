'''
Problem 1: Sort a List of Tuples by the Second Element
Write a function that takes a list of tuples and sorts them by the second element using lambda and sorted().

Expected Output:
For example, given:
points = [(1, 2), (3, 1), (5, 0)]

The output should be:
[(5, 0), (3, 1), (1, 2)]
'''
points = [(1, 2), (3, 1), (5, 0)]
def sortIt(points):
    points = sorted(points, key=lambda x:x[1])
    return points

print(sortIt(points))