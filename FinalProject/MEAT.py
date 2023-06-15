import sys
import time
import threading
import tkinter as tk

# brand new game statuses
prestige_reset = 1
currentItem_num = 0
itemBag = ['waffle', 'mushroom', 'rabbit foot', 'lawnmower', 'goat', 'czech republic flag']
advanceReq = (currentItem_num + 1) * 500
price = prestige_reset * 10
balance = 0
speed = prestige_reset * 1
luck = prestige_reset * 2 - 1

# game reset with prestige in mind
def new_game():
    global price, balance, speed, luck
    price = prestige_reset * 10
    balance = 0
    speed = prestige_reset * 1
    luck = prestige_reset * 2 - 1

# play game function
def setting_up():
    new_game()
    while True:
        inputte = input("Play Game? (y/n)")
        if inputte != "n":
            break
        else:
            print()

# update balance
def update_balance():
    global balance, price, speed
    while True:
        time.sleep(speed)
        balance += price

# executes program
def play_game():
    global balance, speed, luck, price
    setting_up()

    # create a separate thread to continuously update the balance
    balance_thread = threading.Thread(target=update_balance)
    balance_thread.daemon = True
    balance_thread.start()

    # create the main game window
    root = tk.Tk()
    root.title("Game Window")

    # displays/returns to main menu
    def switch_to_main():
        main_frame.pack()
        stats_frame.pack_forget()
        research_frame.pack_forget()
        advance_frame.pack_forget()
        prestige_frame.pack_forget()

    # update statuses
    def update_stats_label():
        stats_label.config(text="Balance: {}".format(int(balance)))
        stats_label.after(1000, update_stats_label)

    # stats button
    def switch_to_stats():
        main_frame.pack_forget()
        stats_frame.pack()
        research_frame.pack_forget()
        advance_frame.pack_forget()
        prestige_frame.pack_forget()

    # research button
    def switch_to_research():
        main_frame.pack_forget()
        stats_frame.pack_forget()
        research_frame.pack()
        advance_frame.pack_forget()
        prestige_frame.pack_forget()

    # advance button
    def switch_to_advance():
        main_frame.pack_forget()
        stats_frame.pack_forget()
        research_frame.pack_forget()
        advance_frame.pack()
        prestige_frame.pack_forget()

    # prestige button
    def switch_to_prestige():
        main_frame.pack_forget()
        stats_frame.pack_forget()
        research_frame.pack_forget()
        advance_frame.pack_forget()
        prestige_frame.pack()

    # research price
    def research_price():
        global price
        price *= 1.2
        price = round(price)
        research_label.config(text="Current price: {}\nNext price: {}\nCurrent speed: {}\nNext speed: {}\nCurrent luck: {}\nNext luck: {}".format(
            int(price), int(price * 1.2), int(speed), int(speed * 1.2), int(luck), int(luck * 1.2)))

    # research speed
    def research_speed():
        global speed
        speed *= 1.2
        speed = round(speed)
        research_label.config(text="Current price: {}\nNext price: {}\nCurrent speed: {}\nNext speed: {}\nCurrent luck: {}\nNext luck: {}".format(
            int(price), int(price * 1.2), int(speed), int(speed * 1.2), int(luck), int(luck * 1.2)))

    # research luck
    def research_luck():
        global luck
        luck *= 1.2
        luck = round(luck)
        research_label.config(text="Current price: {}\nNext price: {}\nCurrent speed: {}\nNext speed: {}\nCurrent luck: {}\nNext luck: {}".format(
            int(price), int(price * 1.2), int(speed), int(speed * 1.2), int(luck), int(luck * 1.2)))

    # create the main game frame
    main_frame = tk.Frame(root)

    # create the buttons for each function
    stats_button = tk.Button(main_frame, text="View marketing status", command=switch_to_stats)
    stats_button.pack()

    research_button = tk.Button(main_frame, text="Research", command=switch_to_research)
    research_button.pack()

    advance_button = tk.Button(main_frame, text="Next advancement", command=switch_to_advance)
    advance_button.pack()

    prestige_button = tk.Button(main_frame, text="Prestige", command=switch_to_prestige)
    prestige_button.pack()

    exit_button = tk.Button(main_frame, text="Exit", command=sys.exit)
    exit_button.pack()

    main_frame.pack()

    # create the stats frame
    stats_frame = tk.Frame(root)

    stats_label = tk.Label(stats_frame, text="Balance: {}".format(int(balance)))
    stats_label.pack()

    update_stats_label()

    stats_back_button = tk.Button(stats_frame, text="Back", command=switch_to_main)
    stats_back_button.pack()

    # create the research frame
    research_frame = tk.Frame(root)

    research_label = tk.Label(research_frame, text="Current price: {}\nNext price: {}\nCurrent speed: {}\nNext speed: {}\nCurrent luck: {}\nNext luck: {}".format(
        int(price), int(price * 1.2), int(speed), int(speed * 1.2), int(luck), int(luck * 1.2)))
    research_label.pack()

    research_price_button = tk.Button(research_frame, text="Research price", command=research_price)
    research_price_button.pack()

    research_speed_button = tk.Button(research_frame, text="Research speed", command=research_speed)
    research_speed_button.pack()

    research_luck_button = tk.Button(research_frame, text="Research luck", command=research_luck)
    research_luck_button.pack()

    research_back_button = tk.Button(research_frame, text="Back", command=switch_to_main)
    research_back_button.pack()

    # create the advance frame
    advance_frame = tk.Frame(root)

    advance_label = tk.Label(advance_frame, text="Next item: {}\nRequirements for next advancement: {}".format(itemBag[currentItem_num + 1], advanceReq))
    advance_label.pack()

    advance_back_button = tk.Button(advance_frame, text="Back", command=switch_to_main)
    advance_back_button.pack()

    # create the prestige frame
    prestige_frame = tk.Frame(root)

    prestige_label = tk.Label(prestige_frame, text="Prestige Stats:\nPrestige Multiplier: {}\nBalance: {}".format(prestige_reset, int(balance)))
    prestige_label.pack()

    prestige_back_button = tk.Button(prestige_frame, text="Back", command=switch_to_main)
    prestige_back_button.pack()

    root.mainloop()

# execute game
play_game()
