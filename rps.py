import sys
import random
from enum import Enum

game_count = 0


def play_game():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    playerchoice=input("Enter your choice...\n----------------------------\n1 for  Rock\n2 for Paper\n3 for Scissor\n---------------------------- ")

    if playerchoice not in ["1","2","3"]:
        print("\nYou must enter only 1, 2, 3. Read the Instruction clearly!!!\n")
        return play_game()
    
    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)


    print("\nYou choose "+ str(RPS(player)).replace('RPS.',' ').title() + ".")
    print("Computer choose "+ str(RPS(computer)).replace('RPS',' ').title()+".\n")

    def decide_winner(player,computer):
        if player == 1  and computer == 3:
            return "You Win"
        elif player == 2 and computer == 1:
            return "You Win"
        elif player == 3 and computer == 2:
            return "You Win"
        elif player == computer:
            return "Its Tiee Game!!!"
        else:
            return "Computer win"
    
    game_result = decide_winner(player,computer)

    print(game_result)

    global game_count
    game_count += 1
    print("\nGame count: " + str(game_count))

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