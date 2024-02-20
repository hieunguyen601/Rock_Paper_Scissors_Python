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

game_images = [rock, paper, scissors]

user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

if user_choice in ["rock", "paper", "scissors"]:
    print("You chose:")
    print(game_images[["rock", "paper", "scissors"].index(user_choice)])
    print(f"\nComputer chose {computer_choice}:")
    print(game_images[["rock", "paper", "scissors"].index(computer_choice)])

    if computer_choice ==    user_choice:
        print("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You won!")
    else:
        print("Computer won!")
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")


