'''
Problem 4: Count Vowels in a String
Write a function that takes a string and returns the count of vowels (a, e, i, o, u) in the string, 
both uppercase and lowercase.

Expected Output:
For example, given:
mystring = "Hello World"

The output should be:
3
'''
mystring = "Hello World"
def counter(mystring):
    vowels = "aeiouAEIOU"
    new_list = []
    for i in vowels:
        for j in mystring:
            if i == j:
                new_list.append(i)
    return len(new_list)           

print(counter(mystring))