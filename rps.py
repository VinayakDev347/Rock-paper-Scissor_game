import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

playagain = True

while playagain:

    print("")
    playerchoice=input("Enter your choice...\n----------------------------\n1 for  Rock\n2 for Paper\n3 for Scissor\n---------------------------- ")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter only 1, 2, 3. Read the Instruction clearly!!!")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You choose"+playerchoice+".")
    print("")

    if player == 1  and computer == 3:
        print("You Win")
    elif player == 2 and computer == 1:
        print("You Win")
    elif player == 3 and computer == 2:
        print("You Win")
    elif player == computer:
        print("Its Tiee Game!!!")
    else:
        print("Computer win")
    