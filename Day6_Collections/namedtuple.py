from collections import namedtuple

Point = namedtuple('Point', 'x, y')
point = Point(-1, 4)
print(point)
#result: Point(x=-1, y=4)

print(point.x, point.y)
#result: -1 4
