'''
Problem 1: Reverse Words in a Sentence
Write a function that takes a string representing a sentence and returns the 
sentence with the words reversed, but the word order intact.

Expected Output:
For example, given:
sentence = "Hello world from Python"

The output should be:
"olleH dlrow morf nohtyP"
'''

sentence = "Hello world from Python"

def reverse(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

print(reverse(sentence))