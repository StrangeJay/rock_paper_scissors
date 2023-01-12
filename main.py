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

#Write your code below this line 👇
choice = int(input("what do you choose? Type 0 for Rock, 1 for paper and 2 for scissors "))
CPU = random.randint(0, 2)

# Possible choices for me
if choice == 0:
    print(f"you choose {rock}")
elif choice == 1:
    print(f"you choose {paper}")
elif choice == 2:
    print(f"you choose {scissors}")
else:
    print("Incorrect selection")

# Choices for CPU
if CPU == 0:
    print(f"CPU chooses {rock}")
elif CPU == 1:
    print(f"CPU chooses {paper}")
elif CPU == 2:
    print(f"CPU chooses {scissors}")
else:
    print("Incorrect selection")

# Rules to determine who wins
if choice == 0 and CPU == 2:
    print("rock breaks scissors, you Win!!!")
elif choice == 1 and CPU == 0:
    print("paper covers rock, you win!!!")
elif choice == 2 and CPU == 1:
    print("Scissors cuts paper, you win")
elif choice == 0 and CPU == 0:
    print("Draw, play again!!!")
elif choice == 1 and CPU == 1:
    print("Draw, play again!!!")
elif choice == 2 and CPU == 2:
    print("Draw, play again!!!")
else:
    print("you lose")
