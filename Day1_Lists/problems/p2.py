'''
Problem 2: List Rotation
Write a function that takes a list and an integer n.
Rotate the list to the right by n positions. 
Rotating the list means moving the last n elements to the front.

Expected Output

If you are given:
my_list = [10, 20, 30, 40, 50]
n = 2

The output should look like:
[40, 50, 10, 20, 30]
'''

def rotate(my_list, n):
    n = n % len(my_list)
    a =  my_list[-n:]
    b = my_list[:-n]
    return a+b

my_list = [10, 20, 30, 40, 50]
n = int(input("Enter index: "))
print(rotate(my_list, n))