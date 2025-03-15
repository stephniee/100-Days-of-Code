import random
# rand_num = random.randint(1,10)
# print(rand_num)

# random float
# rand_num = random.random()
# print(rand_num)

# rand_num = random.uniform(2,4)
# print(rand_num)

user_input = input("Let's do a coin flip, heads or tails!")
num = random.uniform(2,4)
if num >= 3:
    print("The coin flipped heads")
    if user_input == "heads":
        print("You won!")
    else:
        print("you lost!")
else:
    print("The coin flipped tails")
    if user_input == "tails":
        print("You won!")
    else:
        print("you lost!")