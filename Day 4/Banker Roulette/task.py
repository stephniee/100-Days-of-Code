import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print("Who is going to pay the bill?")
rand_num = random.choice(friends)
print(f"{rand_num} is going to pay the bill! Hehe")

# another way
random_num = random.randint(0,4)
print(f"{friends[random_num]} is going to pay the bill! Hehe")