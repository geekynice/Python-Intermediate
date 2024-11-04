import secrets

#1. secrets.randbelow()
a = secrets.randbelow(10)
print(a)
#result: 4

#2. secrets.randbits()
a = secrets.randbits(4)
print(a)
#result: 7

#3. secrets.choice()
mylist = list("ABCSDBJSDH")
choice = secrets.choice(mylist)
print(choice)
#result: B

'''
*Note: The result could change in each attempt, as it is just a random number.
'''