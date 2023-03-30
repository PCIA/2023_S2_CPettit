import random
import time


reset = True


while reset == True:
    
    # defines the starting values
    money = 0
    customers = 0
    products = ["apple", "banana", "orange"]
    product_prices = {"apple": 1, "banana": 2, "orange": 3}
    product_inventories = {"apple": 10, "banana": 5, "orange": 3}
    ad_cost = 5
    ad_multiplier = 2
    reputation = 1

    def start_game():
        # a function which allows the user to retry or leave the game
        global reset, money, customers, reputation
        money = 0
        customers = 0
        reputation = 1
        answer = input('Play game? (y/n)')
        if answer == 'y':
            print('Good luck!')
        elif answer == 'n':
            reset = False
        else:
            print('Invalid input')

        return
    
    def print_menu():
        # shows current status and available options
        print(f"\nYour balance: ${money}")
        print(f"Customers: {customers}")
        print(f"Reputation: {reputation}")
        print("1. Sell a product")
        print("2. Buy an ad")
        print("3. Buy more inventory")
        print("4. Exit")

    def sell_product():
        global money, customers, reputation
        available_products = [product for product in products if product_inventories[product] > 0]
        if len(available_products) > 0:
            product = random.choice(available_products)
            customers += 1
            money += product_prices[product]
            product_inventories[product] -= 1
            print(f"Sold a {product} for ${product_prices[product]}")
            if random.random() < 0.1 * (1/reputation):
                print(f"Oh no! A customer complained about the quality of the {product}.")
                reputation -= 1
                start_game()
                if reset == False:
                    print('Goodbye!')
                    break
        else:
            print("Sorry, we're out of stock!")

    def buy_ad():
        global money, customers, ad_multiplier
        if money >= ad_cost:
            money -= ad_cost
            ad_multiplier += 1
            print(f"Bought an ad for ${ad_cost}")
        else:
            print("Sorry, you don't have enough money for an ad.")

    def buy_inventory():
        global money, product_inventories, reputation
        print("What product would you like to buy inventory for?")
        for i, product in enumerate(products):
            print(f"{i+1}. {product} (${product_prices[product]} each, {product_inventories[product]} in stock)")
        choice = input("Enter a number: ")
        if choice.isdigit() and int(choice) in range(1, len(products)+1):
            product = products[int(choice)-1]
            cost = product_prices[product] * (1/reputation)
            print(f"How much {product}s would you like to buy? (${cost} each)")
            amount = input("Enter a number: ")
            if amount.isdigit() and int(amount) > 0:
                total_cost = cost * int(amount)
                if money >= total_cost:
                    money -= total_cost
                    product_inventories[product] += int(amount)
                    print(f"Bought {amount} {product}s for ${total_cost}")
                    if random.random() < 0.1 * (1/reputation):
                        print(f"Oh no! Some of the {product}s we bought were spoiled.")
                        reputation -= 1
                        start_game()
                        if reset == False:
                            print('Goodbye!')
                            break
                else:
                    print("Sorry, you don't have enough money to buy that much inventory.")
            else:
                print("Invalid input.")
        else:
           print("Invalid input.")

    print("Welcome to the shop game!")
    while True:
        print_menu()
        choice = input("Enter a number: ")
        if choice == "1":
            sell_product()
        elif choice == "2":
            buy_ad()
        elif choice == "3":
            buy_inventory()
        elif choice == "4":
            print("Goodbye!")
            reset = False

