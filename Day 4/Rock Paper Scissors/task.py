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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

c_choice = random.randint(1,3)
print(f"Computer chose {c_choice}")
if user_choice ==0 and c_choice ==2:
    print("You  wins")
elif c_choice > user_choice:
    print("computer ")
elif c_choice ==
