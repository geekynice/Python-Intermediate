points2D = [(1, 2), (15, 1), (5, -1)]
points2D_sorted = sorted(points2D, key=lambda x:x[1])
print(points2D_sorted)
#result: [(5, -1), (15, 1), (1, 2)]