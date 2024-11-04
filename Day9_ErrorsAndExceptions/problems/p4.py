'''
Problem 4: Handle List Index Out of Range
Write a function that takes a list and an index as input. 
If the index is out of range, catch the IndexError and return "Index out of range".

Expected Output:
For example, given:
a = [1, 2, 3]
index = 5

The output should be:
"Index out of range"
'''
a = [1, 2, 3]
index = 5

def handleList(a, index):
    try:
        return a[index]
    except IndexError:
        return "Index out of range"
    
print(handleList(a, index))