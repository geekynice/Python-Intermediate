'''
Problem 3: Default Dictionary for Counting Words
Write a function that takes a string and returns a defaultdict where the 
keys are words and the values are the counts of how many times each word appears.

Expected Output:
For example, given:
sentence = "this is a test this is only a test"

The output should be:
{'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
'''
from collections import Counter
sentence = "this is a test this is only a test"

def counterDict(sentence):
    mylist = []
    for words in sentence.split():
        mylist.append(words)

    mycounter = Counter(mylist)
    return mycounter 

print(counterDict(sentence))