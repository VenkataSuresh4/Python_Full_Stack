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

items = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("Your Choice")
print(items[choice])

print("Computer Choice : ")
computer_choice = random.randint(0, 2)
print(items[computer_choice])

print(choice)
print(computer_choice)

if choice == computer_choice:
    print("Match is a Draw")
elif choice == 0 and computer_choice == 2:
    print("You won the match")
elif choice == 1 and computer_choice == 0:
    print("You won the match")
elif choice == 2 and computer_choice == 1:
    print("You won the match")
else:
    print("Computer Wins")
