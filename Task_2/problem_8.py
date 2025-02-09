'''
    Implement a guessing number game where the computer generates
    a random number between 1 and 100, and the user must guess the number,
    the user has 5 tries and the game can tell if the number is lower or higher .
'''

import random

computer = random.randint(1, 100)
print("Enter a number between 1 and 100, you have 5 tries.")

tries = 5

while tries > 0:
    user = int(input())
    if user == computer:
        print("You win!")
        break
    elif user < computer:
        print("Too low!")
    elif user > computer:
        print("Too high!")
    tries -= 1

if tries == 0:  
    print("You lose!")