'''
Problem 5: Filtered Generator for Odd Numbers
Task: Write a generator function odd_filter(numbers) that takes a list of numbers and yields only the 
odd numbers from that list.

Expected Output: For example, given:
numbers = [1, 2, 3, 4, 5, 6]

The output should be:
1
3
5
'''


def odd_filter(numbers):
    for i in numbers:
        if i % 2 != 0:
            yield i

numbers = [1, 2, 3, 4, 5, 6]
odd = odd_filter(numbers)
for i in odd:
    print(i)