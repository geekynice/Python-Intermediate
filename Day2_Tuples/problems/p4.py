'''
Problem 4: Concatenation and Repetition of Tuples
Write a function that concatenates two tuples and repeats the resulting tuple n times.

Expected Output
If you are given:
tuple1 = (1, 2)
tuple2 = (3, 4)
n = 2

The output should look like:
(1, 2, 3, 4, 1, 2, 3, 4)
'''


def connect(tuple1, tuple2, n):
    new_tuple = tuple1 + tuple2
    final_tuple = new_tuple * n
    print(final_tuple)


tuple1 = (1, 2)
tuple2 = (3, 4)
n = 2

connect(tuple1, tuple2, n)