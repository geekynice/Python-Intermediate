'''
Problem 2: Handle File Not Found Error
Write a function that tries to open a file and reads its contents. 
If the file does not exist, catch the FileNotFoundError and return "File not found".

Expected Output:
For example, given:
filename = "nonexistent.txt"

The output should be:
"File not found"
'''
filename = "nonexistent.txt"
def handleFile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"
    
print(handleFile(filename))