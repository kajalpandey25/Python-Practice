#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

import random

def get_computer_choice():
    return random.choice(["S", "W", "G"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif player_choice == "S":
        return "Player" if computer_choice == "W" else "Computer"
    elif player_choice == "W":
        return "Player" if computer_choice == "G" else "Computer"
    elif player_choice == "G":
        return "Player" if computer_choice == "S" else "Computer"

def display_result(player_choice, computer_choice, winner):
    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Winner: {winner}")

def snake_water_gun():
    print("Welcome to Snake Water Gun Game!")
    print("Choose one among Snake (S), Water (W), and Gun (G).")
    
    player_choice = input("Your choice: ").upper()
    if player_choice not in ["S", "W", "G"]:
        print("Invalid choice! Please choose S, W, or G.")
        return
    
    computer_choice = get_computer_choice()
    winner = determine_winner(player_choice, computer_choice)
    display_result(player_choice, computer_choice, winner)

snake_water_gun()
