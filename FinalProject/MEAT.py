import sys
import random

# library() - list holding every value/string
def library():
    global egg, yogurt, waffle, sandwick, donut, coffee, noot, fulcrum, holdem
    holdem = [egg, yogurt, waffle, sandwick, donut, coffee, noot, fulcrum]

# new_game() - sets up immediate statuses and values/strings, affected respectful to each by prestige
def new_game():
    global price, balance, currentItem, advanceReq, nextItem, speed, luck, god_waffles, 
    noot = 1
    yogurt = (0.1 * noot) * 20
    egg = yogurt
    waffle = yogurt
    sandwick = yogurt
    fulcrum = (0.2 * noot) * 20
    donut = fulcrum
    coffee = fulcrum

# settingUp() - asks user "Play Game?," closes program if no
def setting_up():
    global egg, yogurt, waffle, sandwick, donut, coffee, noot, fulcrum
    new_game()
    while True:
        inputte = input("Play Game? (y/n)")
        if inputte != "n":
            break
        else:
            print()
    return

# gold() - displays statuses and command options to be responded to in yogurt()
def display_menu():
    print(f"\nCurrent Item: " + currentItem)
    print(f"\nBalance: ", balance)
    print(f"\nRequirements for next advancement: " + advanceReq)
    print("1. View marketing status")
    print("2. Research")
    print("3. Next advancement")
    print("4. Prestige")
    print("5: Exit")

# yogurt() - executes options in gold()
def choose_option():
    print("welcome")
    while True:
        displayMenu()
        chezel = input("Which one: ")
        if chezel == 1:
            display_market()
        elif chezel == 2:
            display_research()
        elif chezel == 3:
            display_advance()
        elif chezel == 4:
            display_prestige()
        elif chezel == 5:
            exit()
        else:
            # ask chezel again
            print()
        
        return

# sandwick() - option 1 of gold() - manage selling of current item
def display_stats():
    print("Balance: ", balance)
    stats_choice = input("press enter to continue")
    if stats_choice == "" or stats_choice >= "":
        print()

# waffle() - option 2 of gold() - research stems for item
def waffle():
    print("Current price: ", price, " | Next price: ", (price*1.2))
    print("Current speed: ", speed, " | Next speed: ", (speed*1.2))
    print("Current luck: ", luck, " | Next luck: ", (luck*1.2))
    print("1. Research price")
    print("2. Research speed")
    print("3. Research luck")
    research_choice = input("Choose one: ")
    if research_choice == "1":
        price = price * 1.2
        pass
    elif research_choice == "2":
        speed = speed * 1.2
        pass
    elif research_choice == "3":
        luck = luck * 1.2
        pass
    else:
        pass
    return

# donut() - option 3 of gold() - advance to next item
def display_advance():
    print("Next item: ", nextItem)
    advance_choice = input("Advance? (y/n) ")
    if advance_choice == "n":
        pass
    elif advance_choice == "y":
        advance()
    else:
        pass
    
    return

 # chezel() - option 4 of gold() - start over with prestige multiplier
def display_prestige():
    pass
    # ~ display prestige stats
    # ~ print option to prestige
    # ~ print option to exit
    # ~ allow input for which option
    # ~ if option 2:
        # ~ return to playGame()
    # ~ if option 1:
        # ~ prestige_reset()
    # ~ else:
        # ~ return to input for which option
    return

def play_game():
    while True:
        display_menu()

play_game()