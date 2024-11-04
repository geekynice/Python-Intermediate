'''
Problem 3: Find the First Non-Repeating Character
Write a function that takes a string and returns the first non-repeating character. 
If all characters repeat, return None.

Expected Output:
For example, given:
mystring = "aabbcdd"

The output should be:
"c"
'''
mystring = "aabbcdd"

def repeatChecker(mystring):
    for i in mystring:
        if mystring.count(i) == 1:
            return i
    return None
        
print(repeatChecker(mystring))