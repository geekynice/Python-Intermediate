'''
Problem 2: Check for Anagram
Write a function that takes two strings and checks if they are anagrams 
(contain the same letters with the same frequency, but possibly in a different order).

Expected Output:
For example, given:
str1 = "listen"
str2 = "silent"

The output should be:
True
'''

str1 = "listen"
str2 = "silent"

def checker(str1, str2):
    return sorted(str1) == sorted(str2)

print(checker(str1, str2))