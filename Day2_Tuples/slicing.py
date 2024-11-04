mytuple = ("Nice", 20, "Nice", "Toronto")
print(mytuple[1:3])
#result: (20, "Nice")

print(mytuple[:3])
#result: ("Nice", 20, "Nice")

print(mytuple[3:])
#result: ('Toronto',)

print(mytuple[1::])
#result: (20, "Nice", "Toronto")  

print(mytuple[::-1])
#result: ('Toronto', 'Nice', 20, 'Nice')