"""
WORKFLOW OF PROJECT:
1. Input from user (Rock, Paper, Scissor)
2. Computer Choice (Computer will choose randomly not conditionally)
3. Result print

Cases:
A. Rock
Rock - Rock = Tie
Rock - Paper = Paper Wins
Rock - Scissor = Rock Wins

B. Paper
Paper - Paper = Tie
Paper - Rock = Paper Wins
Paper - Scissor = Scissor Wins

C. Scissor
Scissor - Scissor = Tie
Scissor - Rock = Rock Wins
Scissor - Paper = Scissor Wins

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock, Computer Win")
    else:
        print("Rock smashes Scissor, You Win")
   
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper, Computer Win")
    else:
        print("Paper covers Rock, You Win")
        
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper, You Win")
    else:
        print("Rock smashes Scissor, Computer Win")
        
        