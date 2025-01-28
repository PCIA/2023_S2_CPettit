# Testing!

import sys

# playGame() - allows useer to execute all functions, otherwise known as play the game
def playGame():
    a = input("play game (y/n) ")
    if a == "n":
        print("goodbye")
        exit()
    elif a == "y":
        fullReset()
        while True:
            displayMenu()
            b = input("what would you like to do ")
            if b == "1":
                displayStats()
            elif b == "2":
                displayResearch()
            elif b == "3":
                displayAdvance()
            elif b == "4":
                displayPrestige()
            elif b == "5":
                print("goodbye")
                exit()
            else:
                # ask b again
    else:
        print("invalid")
    return

# no definitions beyond this point | gameplay section

playGame()