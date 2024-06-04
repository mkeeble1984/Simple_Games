import random
import time
import os
import sys

def roll():
    min_roll = 1
    max_roll = 6
    roll = random.randint(min_roll, max_roll)
    return roll

os.system("cls")
print("""In this game, players take it in turns to roll a dice as many times as they choose. 
The score of each roll is added together as they try to reach the target score. 
Players can stop rolling at any time and save their current score, however, 
if they roll a 1 their current score is lost!""")

players = 0
max_score = 0
player_scores = 0
while True:
    players = input("\nPlease enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break;
        else:
            print("\nPlease enter a number between 2 and 4.")
            time.sleep(4)
            os.system("cls")
    else:
        print("\nPlease enter a valid number.")
        time.sleep(4)
        os.system("cls")

while True:
    max_score = input("\nWhat is the winning score would you like to set? ")
    if max_score.isdigit():
        max_score = int(max_score)
        os.system("cls")
        break;
    else:
        print("\nPlease enter a valid number.")
        time.sleep(4)
        os.system("cls")

player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_index in range(players):
        current_score = 0
        
        while True:
            print(f"Target score is: {max_score}")
            print(f"Player 1 score = {player_scores[0]}")
            print(f"Player 2 score = {player_scores[1]}")
                
            if players == 3:
                print(f"Player 3 score = {player_scores[2]}")
            elif players == 4:
                print(f"Player 3 score = {player_scores[2]}")
                print(f"Player 4 score = {player_scores[3]}")
                                
            should_roll = input(f"\nPlayer {player_index + 1}, your current score is {current_score}. Would you like to roll? (Y / N): ").lower()
                
            if should_roll == "y":
                value = roll()
                
                if value == 1:
                    print("\nYou rolled a 1! You lost all your points, your turn is over.")
                    current_score = 0
                    break;
                else:
                    current_score += value
                    print(f"\nYou rolled a {value}, your current score is {current_score}.")

                    if player_scores[player_index] + current_score >= max_score:
                        time.sleep(4)
                        os.system("cls")
                        print(f"Player {player_index + 1}, you have reched the target score!!!!\nWell done, you win!!!!!")
                        time.sleep(5)
                        sys.exit(0)

                    time.sleep(4)
                    os.system("cls")
            
            elif should_roll == "n":
                break;
                
            else:
                print("\nPlease eneter a valid choice. (Y / N)")
                time.sleep(4)
                os.system("cls")
                
        player_scores[player_index] += current_score
        print(f"\nYour total score is {player_scores[player_index]}")
        time.sleep(4)
        os.system("cls")

