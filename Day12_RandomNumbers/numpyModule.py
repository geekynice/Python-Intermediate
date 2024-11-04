import numpy as np  # Importing the numpy library to generate random numbers and manipulate arrays

# Generate a 1D array with 3 random floats between 0.0 and 1.0
a = np.random.rand(3)
print(a)  # Example output: [0.5488135  0.71518937 0.60276338]

# Generate a 3x3 array with random floats between 0.0 and 1.0
a = np.random.rand(3, 3)
print(a)  
# Example output:
# [[0.54488318 0.4236548  0.64589411]
#  [0.43758721 0.891773   0.96366276]
#  [0.38344152 0.79172504 0.52889492]]

# Generate a random integer between 0 and 9 (inclusive)
a = np.random.randint(0, 10)
print(a)  # Example output: 4

# Generate a 1D array with 3 random integers between 0 and 9 (inclusive)
a = np.random.randint(0, 10, 3)
print(a)  # Example output: [1 8 3]

# Generate a 3x4 array with random integers between 0 and 9 (inclusive)
a = np.random.randint(0, 10, (3, 4))
print(a)
# Example output:
# [[4 9 2 6]
#  [1 3 8 9]
#  [7 2 0 5]]

# Create a 3x3 array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Shuffle the rows of the array in place
np.random.shuffle(arr)
print(arr)  # Example output (rows are shuffled):
# [[4 5 6]
#  [7 8 9]
#  [1 2 3]]
