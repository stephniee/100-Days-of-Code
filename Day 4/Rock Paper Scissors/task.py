import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock,paper,scissors]
choice = int(input("What do you choose? Rock, Paper, or Scissors, Rock - 0, Paper - 1, Scissors - 2 "))
choices = ["rock", "paper", "scissors"]
print(f"Your choice is: {choices[choice]}" )
print(rock_paper_scissors[choice])

computer_choice = random.randint(0,2)
print(f"The computer chose: {choices[computer_choice]}")
print(rock_paper_scissors[computer_choice])

if choice == computer_choice:
    print("Its a tie!")
if choice == 0 and computer_choice == 2 or choice == 1 and computer_choice == 0 or choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lost")



