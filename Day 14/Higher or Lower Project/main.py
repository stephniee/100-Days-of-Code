# Higher or Lower Game
# Import Statements
import os

from art import logo, vs
from game_data import data
import random



# method to clear console
def clear_console():
    print("\n" * 20)

def format_comparison(label, contestant):
    return f"{label}: {contestant['name']}, a {contestant['description']}, from {contestant['country']}."

# method to compare user guess
def check_guess(guess, a, b):
    a_followers = a['follower_count']
    b_followers = b['follower_count']

    if (a_followers > b_followers and guess == 'A') or (a_followers < b_followers and guess == 'B'):
        return 1
    else:
        return 0

def get_user_guess():
    guess= ""
    while True:
        try:
            guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
            # Check if input is valid
            if guess not in ["A", "B"]:
                print("Oopsie, input only A or B please!")
                continue
            else:
                return guess
        except Exception as e:
            print(f"An error occurred: {e}")

def play_game():
    # Initialize variables to score user's score.
    user_score = 0
    game_over = False
    # Randomize participants
    compare_A = random.choice(data)
    compare_B = random.choice(data)
    while compare_B == compare_A:  # checkers
        compare_B = random.choice(data)
    while not game_over:
        print(logo)
        if user_score > 0:
            print(f"You're right! Current score = {user_score}")


        print(format_comparison("Compare A: ", compare_A))
        print(vs)
        print(format_comparison("Against B: ",compare_B))
        user_guess = get_user_guess()
        result = check_guess(user_guess,compare_A,compare_B)

        if result == 1:
            user_score += 1
            if user_guess == 'B':
                compare_A = compare_B
            compare_B = random.choice(data)
        else:
            clear_console()
            print(logo)
            print(f"Sorry that's wrong. Final score = {user_score}")
            break

play_game()




