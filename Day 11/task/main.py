from art import logo
import random

#Initialize Parameters

game_over = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random_choice = ["y","n"]

def determine_winner(score_1, score_2):
    if score_1 > 21 and score_2 > 21:
        print("No winners lol")
    elif score_1 > 21:
        print("You went over. You lose 😭")
    elif score_2 > 21:
        print("The computer went over. You win 😎")
    elif score_1 > score_2:
        print("You win 😎")
    elif score_2 > score_1:
        print("You lose 😭")
    else:
        print("Its a tie!")
def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    result = sum(cards)
    return result

def game_logic(first_cards,second_cards,score_1,score_2):
    while score_1 < 21 or score_2 < 21:
        score_1 = calculate_score(first_cards)
        score_2 = calculate_score(second_cards)
        print(f"Your cards: {first_cards}, current score: {score_1}")
        print(f"The computer's first card: {second_cards[0]}")
        another_choice = input("Type 'y' to get another card or type 'n' to pass. ")
        computer_choice = random.choice(random_choice)
        if another_choice == 'y':
            first_cards.append(random.choice(cards))
            score_1 = calculate_score(first_cards)
        if computer_choice == 'y':
            second_cards.append(random.choice(cards))
            score_2 = calculate_score(second_cards)
        elif another_choice == 'n' and computer_choice == 'n':
            break

    print(f"Your final hand: {first_cards}, final score: {score_1}")
    print(f"The computer's final hand: {second_cards}, final score: {score_2}")
    determine_winner(score_1,score_2)

while not game_over:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    computer_score = 0
    user_score = 0
    user_card = []
    computer_card = []
    if choice == 'y':
        print(logo)
        n = 0

        while n < 2:
            user_card.append(random.choice(cards))
            computer_card.append(random.choice(cards))
            n += 1

        game_logic(first_cards=user_card,second_cards=computer_card,score_1=user_score,score_2=computer_score)

    else:
        print("byebye")
        game_over = True



