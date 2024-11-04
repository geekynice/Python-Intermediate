'''
Problem 7: Find Elements Present in Exactly One List
Write a function that takes two lists and returns a set of elements that are 
present in exactly one of the two lists (i.e., elements that are unique to each list and not present in both).

Expected Output:
For example, given:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

The output should be:
{1, 2, 3, 6, 7, 8}
'''
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

def setConverter(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.symmetric_difference(set2)

print(setConverter(list1, list2))