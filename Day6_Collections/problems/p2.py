'''
Problem 2: Store and Retrieve Points Using NamedTuple
Write a function that takes a list of tuples representing (x, y) coordinates and 
returns a list of namedtuple objects for those points. 
Also, return the coordinates of the point with the highest y-value.

Expected Output:
For example, given:
points = [(1, 2), (-1, 5), (3, 4)]

The output should be:
[Point(x=1, y=2), Point(x=-1, y=5), Point(x=3, y=4)]
Point with the highest y-value: (-1, 5)
'''
from collections import namedtuple

points = [(1, 2), (-1, 5), (3, 4)]

def highest(points):
    Point = namedtuple('Point', 'x, y')
    mylist = []
    highest_y_value = Point(points[0][0],  points[0][1])
    for (x, y) in points:
        pt = Point(x, y)
        mylist.append(pt)
        if pt.y  > highest_y_value.y:
            highest_y_value = pt
    
    print(f"Point with the highest y-value: {highest_y_value}")
    return mylist

print(highest(points))