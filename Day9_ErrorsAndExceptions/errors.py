#1. Syntax Error
# a = 3 b = 3
#SyntaxError: invalid syntax, because i missed a comma in between

#2. Type Error
# a = "12"
# b = 1
# print(a+b)
#TypeError: can only concatenate str (not "int") to str

#3. ModuleNotFound Error:
# from something import something
#ModuleNotFoundError: No module named 'something'

#4. FileNotFound Error:
# f =  open("nice.txt")
#FileNotFoundError: [Errno 2] No such file or directory: 'nice.txt'

#5. Value Error:
# a = [1, 2, 3, 4]
# a.remove(7)
#ValueError: list.remove(x): x not in list

#6. Index Error:
# a = [1, 2, 3, 4]
# a[6]
# IndexError: list index out of range

#7. Indentation Error:
# a = 8
# if a > 6:
# print("Yes")
# IndentationError: expected an indented block after 'if' statement on line 31