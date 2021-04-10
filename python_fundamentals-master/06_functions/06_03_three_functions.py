'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
# I made three functions but I couldn't think of a meaningful program where each function calls another function

import random

def player_hand():
    player_item = input("\nSelect Rock, Paper, or Scissors:\n").capitalize()
    for value in rps_dict.values():
        if player_item == value:
            print(f"You chose: {player_item}")
    return player_item

def comp_hand():
    comp_item = random.choice(list(rps_dict.values()))
    for value in rps_dict.values():
        if comp_item == value:
            print(f"Computer chose: {comp_item}")
    return comp_item

def winner(player_item, comp_item):
    if player_item == comp_item:
        print(f"You both selected the same item! You: {player_item}, Computer: {comp_item}\n")
    elif player_item == "Rock":
        if comp_item == "Scissors":
            print(f"{player_item} smashes {comp_item}. You Win!\n")
        elif comp_item == "Paper":
            print(f"{player_item} is covered by {comp_item}. You lose :(\n")
    elif player_item == "Paper":
        if comp_item == "Rock":
            print(f"{player_item} is covered by {comp_item}. You Win!\n")
        elif comp_item == "Scissors":
            print(f"{player_item} is cut by {comp_item}. You lose :(\n")
    elif player_item == "Scissors":
        if comp_item == "Paper":
            print(f"{player_item} cuts {comp_item}. You win!\n")
        elif comp_item == "Rock":
            print(f"{player_item} is smashed by {comp_item}. You lose :(\n")
    return

rps_dict = {
    0: "Scissors",
    1: "Rock",
    2: "Paper"
    }

playing = True
while playing:
    player_item = player_hand()
    comp_item = comp_hand()
    winner(player_item, comp_item)
    keep_playing = input("Play again? Yes or No?\n").capitalize()
    if keep_playing == "Yes":
        playing = True
    elif keep_playing == "No":
        playing = False