import random

a = random.random()  # Random float between 0.0 and 1.0
print(a)
#result: 0.42683300532324675

a = random.uniform(1, 10)  # Random float between 1 and 10
print(a)
#result: 4.147935254098172

a = random.randint(1, 10)  # Random integer between 1 and 10 (inclusive)
print(a)
#result: 6

a = random.randrange(1, 10)  # Random integer between 1 and 9 (upper bound is exclusive)
print(a)
#result: 8

a = random.normalvariate(0, 1)  # Random number from a normal distribution with mean=0, stdev=1
print(a)
#result: -1.4433091104342113

mylist = list("ABCDEFGH")
choice = random.choice(mylist)  # Randomly choose one element from the list
print(choice)
#result: G

sample = random.sample(mylist, 3)  # Randomly choose 3 unique elements from the list
print(sample)
#result: ['H', 'A', 'D']

choices = random.choices(mylist, k=3)  # Randomly choose 3 elements from the list (with replacement)
print(choices)
#result: ['E', 'G', 'C']

random.shuffle(mylist)  # Shuffle the list in place
print(mylist)  # Print the shuffled list
#result: ['G', 'H', 'C', 'A', 'F', 'B', 'D', 'E']

random.seed(1)
a = random.random()  # Generate the same random number sequence with seed 1
print(a)
#result: 0.13436424411240122

a = random.randint(1, 10)
print(a)
#result: 2

random.seed(1)
a = random.random()  # Same random sequence as above
print(a)
#result: 0.13436424411240122

a = random.randint(1, 10)
print(a)
#result: 2