import sys
import time

# Global variables
current_item = "normal waffle"
money = 0
advance_req = 0
noot = 1
god_waffles = 0
god_waffles_in_use = 0

# Initialize game values
def new_game():
    global current_item, money, egg, advance_req, noot, god_waffles, god_waffles_in_use
    noot = 1
    money = 0
    egg = 10
    advance_req = 0
    current_item = "normal waffle"
    god_waffles = 0
    god_waffles_in_use = 0

# Display the main menu
def display_menu():
    print("\n=== Main Menu ===")
    print("1. View Marketing Stats")
    print("2. Research")
    print("3. Next Advancement")
    print("4. Prestige")
    print("5. Exit")

# Handle user's menu choice
def handle_choice(choice):
    global current_item, money, advance_req, noot, god_waffles, god_waffles_in_use
    
    if choice == "1":
        display_stats()
    elif choice == "2":
        research()
    elif choice == "3":
        next_advancement()
    elif choice == "4":
        prestige()
    elif choice == "5":
        sys.exit()
    else:
        print("Invalid choice. Please try again.")

# Display marketing stats for the current item
def display_stats():
    print("\n=== Marketing Stats ===")
    print("Current Item:", current_item)
    print("Money:", money)
    print("Requirements for Next Advancement:", advance_req)
    input("Press Enter to continue...")

# Perform research for the current item
def display_research():
    global money
    print("\n=== Research ===")
    print("1. Research Value")
    print("2. Research Speed")
    print("3. Research Luck")
    print("4. Exit")

# Perform research for value
def research_value():
    global money, egg
    research_cost = 100  # Example cost for value research
    if money >= research_cost:
        money -= research_cost
        egg = egg * 1.2
        print("Value research performed successfully!")
    else:
        print("Insufficient funds to perform value research.")

# Perform research for speed
def research_speed():
    global money
    research_cost = 200  # Example cost for speed research
    if money >= research_cost:
        money -= research_cost
        # Update speed research progress and its effects
        print("Speed research performed successfully!")
    else:
        print("Insufficient funds to perform speed research.")

# Perform research for luck
def research_luck():
    global money
    research_cost = 300  # Example cost for luck research
    if money >= research_cost:
        money -= research_cost
        # Update luck research progress and its effects
        print("Luck research performed successfully!")
    else:
        print("Insufficient funds to perform luck research.")

# Perform research for the current item
def research():
    global money
    print("\n=== Research ===")
    print("1. Research Value")
    print("2. Research Speed")
    print("3. Research Luck")
    print("4. Exit")

    research_choice = input("Choose an option: ")
    if research_choice == "1":
        research_value()
    elif research_choice == "2":
        research_speed()
    elif research_choice == "3":
        research_luck()
    elif research_choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")


# Advance to the next item
def next_advancement():
    global current_item, money, advance_req
    print("\n=== Next Advancement ===")
    print("Are you sure you want to advance to the next item?")
    print("1. Yes")
    print("2. No")

    advancement_choice = input("Choose an option: ")
    if advancement_choice == "1":
        # Check if the user has enough money to advance
        if money >= advance_req:
            money -= advance_req
            # Update current_item, money, and advance_req accordingly
            current_item = "Next Item"
            advance_req += 100  # Example increment for the next advancement
            print("Advanced to the next item!")
        else:
            print("Insufficient funds to advance.")
    elif advancement_choice == "2":
        return
    else:
        print("Invalid choice. Please try again.")

# Perform prestige
def prestige():
    global money, noot, god_waffles, god_waffles_in_use
    print("\n=== Prestige ===")
    print("God Waffles (Unused):", god_waffles)
    print("Are you sure you want to prestige?")
    print("1. Yes")
    print("2. No")

    prestige_choice = input("Choose an option: ")
    if prestige_choice == "1":
        # Update money and noot based on the prestige logic
        money += god_waffles_in_use * 100  # Example calculation based on god waffles in use
        noot = 1
        god_waffles += god_waffles_in_use
        god_waffles_in_use = 0
        print("Prestige successful!")
    elif prestige_choice == "2":
        return
    else:
        print("Invalid choice. Please try again.")

# Main game loop
def play_game():
    setting_up()
    start_time = time.time()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        handle_choice(choice)
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1:
            start_time = time.time()
            sell_item()

# Sell one item
def sell_item():
    global money, egg
    money += egg
    print("Item sold! Money +$10")

# Ask the user if they want to play the game
def setting_up():
    new_game()
    while True:
        inputte = input("Play Game? (y/n) ")
        if inputte != "n":
            break
        else:
            sys.exit()

# Start the game
play_game()
