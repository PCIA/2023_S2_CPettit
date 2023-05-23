# playGame() - allows useer to execute all functions, otherwise known as play the game
def playGame():
    a = input("play game (y/n) ")
    if a == "n":
        print("goodbye")
    elif a == "y":
        reset()
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
                prestige()
            elif b == "5":
                exit()
            else:
                print("goodbye")
                break
    else:
        ("invalid")
    return

playGame()