'''
Problem: Longest Palindromic Substring
Write a function that takes a string and returns the longest palindromic substring 
(a string that reads the same forward and backward).

Expected Output:
For example, given:
mystring = "babad"

The output could be:
"bab"  # or "aba"

Another example:
mystring = "cbbd"

The output should be:
"bb"
'''
from timeit import default_timer as timer

start = timer()
mystring = "babad"
def palindrome(mystring):
    new_list = []
    longest_palindrome = ''
    for i in range(len(mystring)):
        for x in range(i+1,  len(mystring)+1):
            new_list.append(mystring[i:x])
    for item in new_list:
        if len(item) == 1:
            pass
        else:
            if item == item[::-1] and len(item) > len(longest_palindrome):
                longest_palindrome = item 
    return longest_palindrome
# class Solution(object):
#     def longestPalindrome(self, s):
#         if len(s) == 0:
#             return ''
#         elif len(s) == 1:
#             return s
#         palindrome_list = []
#         longest_palindrome_substring = ""
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 palindrome_list.append(s[i:j])
#             for item in palindrome_list:
#                 if item == item[::-1] and len(item) > len(longest_palindrome_substring):
#                     longest_palindrome_substring = item
#                 else:
#                     pass
            
        # return longest_palindrome_substring
            
print(palindrome(mystring))
stop = timer()
print(stop-start)


