from itertools import groupby

a = [1, 2, 3, 4]
group_obj = groupby(a)
for key, value in group_obj:
	print(key, list(value)) 
	
'''
result: 
1 [1]
2 [2]
3 [3]
4 [4]
'''