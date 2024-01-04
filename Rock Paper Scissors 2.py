import random
import os

choices = ["Rock", "Paper", "Scissors"]
decisions = [1, 2]
gamedecisions = [1, 2, 3]

def defineWinner(user, comp):
    if (user == 'Rock' and comp == 'Scissors'
    or user == 'Scissors' and comp == 'Paper'
    or user == 'Paper' and comp == 'Rock'):
        return "User"
    elif (user == 'Scissors' and comp == 'Rock'
          or user == 'Paper' and comp == 'Scissors'
          or user == 'Rock' and comp == 'Paper'):
        return "Comp"
    else:
        return "Draw"
    
def validContinueGame(userchoice):
    while userchoice not in decisions:
        print("That is not a valid choice.")
        try:
            userchoice = int(input("Please enter either 1 or 2: "))
        except:
            continue
    return userchoice

def validPlayGame(userchoice):
    while userchoice not in gamedecisions:
        print("That is not a valid choice.")
        try:
            userchoice = int(input("Please enter either 1, 2 or 3: "))
        except:
            continue
    return userchoice

playing = True

while playing:
    os.system('cls')
    print("Hello and thank you for playing 'Rock, Paper, Scissors'!" + "\n")
    print(choices, "\n")
    print("Please select one of the following above choices by number:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    pick = input("Pick: ")
    try:
        pick = int(pick)
    except:
        pick = validPlayGame(pick)
    pick = choices[pick - 1]

    print(" ")
    print(f"Your choice: {pick}")
    programpick = random.choice(choices)
    print(f"The program's choice: {programpick}" + '\n')
    answer = defineWinner(pick, programpick)

    if answer == "User":
        print(f"Congrats! You've won! {pick} beats {programpick}." + '\n')
    elif answer == "Comp":
        print(f"Ha! I've won this round, as {programpick} beats {pick}." + '\n')
    else:
        print(f"Appears to be a draw! We both picked {pick}." + '\n')

    print(f"Play again?")
    print("1. Play Again")
    print("2. Quit program")

    decision = input("Please enter your choice: ")
    try:
        decision = int(decision)
    except:
        decision = validContinueGame(decision)

    if decision == 2:
        print("\n" + "I understand. Thank you for playing! Enjoy your day.")
        playing = False
    elif decision == 1:
        continue