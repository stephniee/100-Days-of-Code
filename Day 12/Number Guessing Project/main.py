import random
import art

print(art.logo)
GUESS_NUMBER = random.randrange(1, 101)
lives = 0

print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
else:
    print("That's an invalid input")

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))

    if user_guess < GUESS_NUMBER:
        print("Too low!")
    elif user_guess > GUESS_NUMBER:
        print("Too high!")
    else:
        print(f"You got it! The answer was {GUESS_NUMBER}")
        break  # Exit the loop immediately after a correct guess

    lives -= 1  # Decrease lives only once per iteration

if lives == 0:
    print(f"You lost! The answer was {GUESS_NUMBER}")

