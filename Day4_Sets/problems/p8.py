'''
Problem 8: Find Common Elements in Multiple Sets
Write a function that takes a list of sets and returns a set of elements that are common across all the sets.

Expected Output:
For example, given:
set_list = [{1, 2, 3, 4}, {2, 3, 4, 5}, {2, 4, 6}]

The output should be:
{2, 4}
'''
set_list = [{1, 2, 3, 4}, {2, 3, 4, 5}, {2, 4, 6}]

def commonElements(set_list):
    common_elements = set_list[0]
    for sets in set_list[1:]:
        common_elements = common_elements.intersection(sets)
    return common_elements
    
print(commonElements(set_list))