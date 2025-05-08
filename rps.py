import sys
import random
from enum import Enum


def play_game():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    playerchoice=input("Enter your choice...\n----------------------------\n1 for  Rock\n2 for Paper\n3 for Scissor\n---------------------------- ")

    if playerchoice not in ["1","2","3"]:
        print("You must enter only 1, 2, 3. Read the Instruction clearly!!!")
        return play_game()
    
    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)


    print("\nYou choose "+ str(RPS(player)).replace('RPS.',' ').title() + ".")
    print("Computer choose "+ str(RPS(computer)).replace('RPS',' ').title()+".\n")

    if player == 1  and computer == 3:
        print("\nYou Win")
    elif player == 2 and computer == 1:
        print("\nYou Win")
    elif player == 3 and computer == 2:
        print("\nYou Win")
    elif player == computer:
        print("\nIts Tiee Game!!!")
    else:
        print("\nComputer win")

    print("\nPlay again?")
    while True:
        playagain = input("\nY for Yes or\nQ for Quit \n\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_game()
    else:
        print("ThankYou for playing!!!")
        sys.exit("Bye...")



play_game()