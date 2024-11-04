'''
Problem 4: Generate Secure Random Number
Write a function that generates and returns a secure random integer between 1 and 50 using the secrets module.

Expected Output:
The output will be a secure random integer between 1 and 50.
'''
import secrets

def secureNumber():
    return secrets.randbelow(50) + 1

print(secureNumber())