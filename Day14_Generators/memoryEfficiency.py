import sys
import time

start = time.time()
def firstN(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
end = time.time()
print(f'The time taken by 1st function is: {end-start}')

start = time.time()
def firstN_with_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
end = time.time()
print(f'The time taken by 2nd function is: {end-start}')

print(f'Memory Occupied: {sys.getsizeof(firstN(10000000))}')
print(f'Memory Occupied: {sys.getsizeof(firstN_with_generator(10000000))}')

'''
The time taken by 1st function is: 0.0
The time taken by 2nd function is: 7.152557373046875e-07
Memory Occupied: 89095160
Memory Occupied: 192
'''