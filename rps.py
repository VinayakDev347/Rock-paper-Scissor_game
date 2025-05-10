import sys
import random
from enum import Enum

def rock_papper_scissor():
    game_count = 0
    player_wins = 0
    computer_wins = 0


    def play_game():
        nonlocal player_wins
        nonlocal computer_wins

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
        print("Computer choose "+ str(RPS(computer)).replace('RPS.',' ').title()+".\n")

        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal computer_wins

            if player == 1  and computer == 3:
                player_wins += 1
                return "You Win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You Win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You Win"
            elif player == computer:
                return "Its Tiee Game!!!"
            else:
                computer_wins += 1
                return "Computer win"
        
        game_result = decide_winner(player,computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("\nPlayer Wins: " + str(player_wins))
        print("\nComputer Wins: " + str(computer_wins))

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

    return play_game

play = rock_papper_scissor()

play()