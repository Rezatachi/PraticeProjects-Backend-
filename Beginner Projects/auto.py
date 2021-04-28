import random
# Use of imports and random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scisscors")

question = input()
user = int(question)
computer_num = random.randint(0,2)


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

if ((user == 1) and (computer_num == 2)):
    print("You Chose:\n " + paper)
    print("Bot Chose:\n" + scissors)
    print("You LOST LOL")

if ((user == 2) and (computer_num == 1)):
    print("You Chose:\n " + scissors)
    print("Bot Chose:\n" + paper)
    print("You won OMG")

if ((user == 0) and (computer_num == 2)):
    print("You Chose:\n " + rock)
    print("Bot Chose:\n" + scissors)
    print("You won OMEGALUL")

if ((user == 2) and (computer_num == 0)):
    print("You Chose:\n " + scissors)
    print("Bot Chose:\n" + rock)
    print("You lost OMEGALUL")
    
if ((user == 1) and (computer_num == 0)):
    print("You Chose:\n " + paper)
    print("Bot Chose:\n" + rock)
    print("You won OMEGALUL")

if ((user == 0) and (computer_num == 1)):
    print("You Chose:\n " + rock)
    print("Bot Chose:\n" + paper)
    print("You lost OMEGALUL")
elif (user == computer_num):
        print("Draw!")
else:
     print("Error, please choose a number between 0 and 2")


