'''
Problem 5: Random 2D Array using NumPy
Write a function that generates a 2D array (4x4) of random integers between 0 and 9 using numpy.

Expected Output:
The output should be a 4x4 array, for example:
[[2 5 6 3]
 [9 1 8 0]
 [7 4 6 2]
 [1 3 5 4]]
'''
import numpy as np

def randomArray():
    return np.random.randint(0, 9, (4, 4))

print(randomArray())