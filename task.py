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
game = [rock, paper, scissors]
import random
computer_choice = random.choice(game)
instruction = int(input("What you want to choose? Type 0 for rock, 1 for paper and 2 for scissors:\n "))
if instruction == 0:
    print("You chose:")
    print(rock)
    print("Computer chose:")
    print(computer_choice)
    if computer_choice == rock:
        print("Match draw")
    elif computer_choice == paper:
        print("Computer won!")
    else:
        print("You won!")
elif instruction == 1:
    print("You chose:")
    print(paper)
    print("Computer chose:")
    print(computer_choice)
    if computer_choice == rock:
        print("You win!")
    elif computer_choice == paper:
        print("Match draw")
    else:
        print("Computer won!")
elif instruction == 2:
    print("You chose:")
    print(scissors)
    print("Computer chose:")
    print(computer_choice)
    if computer_choice == rock:
        print("Computer won!")
    elif computer_choice == paper:
        print("You won!")
    else:
        print("Match draw")
else:
    print("Invalid input")
