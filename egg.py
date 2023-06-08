# Define player_position
player_position = (0, 0)

# Define the environment elements
environment_elements = {
    "tree": {
        "description": "A tall tree that provides shade and wood.",
        "resource": "wood"
    },
    "river": {
        "description": "A flowing river that provides water and fish.",
        "resource": "water"
    },
    "mountain": {
        "description": "A majestic mountain that provides a high vantage point.",
        "resource": "metal"
    }
}

# Define the pollution types
pollution_types = {
    "plastic": {
        "description": "A type of pollution that is harmful to wildlife and the environment.",
        "tool": "plastic cleaner"
    },
    "oil": {
        "description": "A type of pollution that is harmful to water and marine life.",
        "tool": "oil absorber"
    },
    "air": {
        "description": "A type of pollution that is harmful to air quality and human health.",
        "tool": "air purifier"
    }
}

# Define the defender types
defender_types = {
    "scientist": {
        "description": "A defender who specializes in research and development.",
        "resource": "knowledge"
    },
    "engineer": {
        "description": "A defender who specializes in building and repairing structures.",
        "resource": "tools"
    },
    "activist": {
        "description": "A defender who specializes in negotiation and communication.",
        "resource": "support"
    }
}

# Define the tools
tools = {
    "plastic cleaner": {
        "description": "A tool that can clean up plastic waste from the environment.",
        "resource": "knowledge"
    },
    "oil absorber": {
        "description": "A tool that can absorb oil spills from the water.",
        "resource": "tools"
    },
    "air purifier": {
        "description": "A tool that can purify the air from pollutants.",
        "resource": "support"
    }
}

# Define the resources
resources = {
    "wood": {
        "description": "A resource that can be used to build structures and tools.",
        "quantity": 10
    },
    "water": {
        "description": "A resource that can be used for drinking and cleaning.",
        "quantity": 10
    },
    "metal": {
        "description": "A resource that can be used to build durable structures and tools.",
        "quantity": 10
    },
    "knowledge": {
        "description": "A resource that can be used to research and develop new technologies.",
        "quantity": 10
    },
    "tools": {
        "description": "A resource that can be used to build and repair structures and tools.",
        "quantity": 10
    },
    "support": {
        "description": "A resource that can be used to negotiate and communicate with others.",
        "quantity": 10
    }
}

player_inventory = {
    "recycled paper": 10,
    "reusable water bottle": 1,
    "solar-powered flashlight": 1,
    "organic seeds": 5,
    "compost bin": 1,
    "bicycle": 1
}

# Function to display the game map
def display_map(player_position, environment_elements):
    print("You are currently at position", player_position)
    print("This is the game map:")
    for position, element in environment_elements.items():
        if position == player_position:
            print("*", end="")
        else:
            print("-", end="")
    print()

# Function to move the player on the map

# Function to move the player on the map
def move_player(player_position):
    direction = input("Where do you want to move? (North/South/East/West)").lower()
    if direction == "north":
        player_position[1] += 1
    elif direction == "south":
        player_position[1] -= 1
    elif direction == "east":
        player_position[0] += 1
    elif direction == "west":
        player_position[0] -= 1
    else:
        print("Invalid direction. Please try again.")
    return player_position

# Function to display the player inventory
def display_inventory(player_inventory):
    print("Your inventory:")
    for resource, quantity in player_inventory.items():
        print(f"{resource}: {quantity}")

# Function to collect resources from an environment element
def collect_resource(player_position, environment_elements, player_inventory):
    element = environment_elements.get(player_position)
    if element:
        resource = element.get("resource")
        if resource:
            quantity = element.get("quantity", 1)
            player_inventory[resource] = player_inventory.get(resource, 0) + quantity
            element["quantity"] = max(0, element.get("quantity", 0) - quantity)
            print(f"You collected {quantity} {resource} from {player_position}.")
        else:
            print(f"{player_position} does not contain a collectible resource.")
    else:
        print(f"{player_position} is not a valid environment element.")

# Function to clean up pollution from an environment element
def clean_pollution(player_position, environment_elements, pollution_types, tools, player_inventory):
    element = environment_elements.get(player_position)
    if element:
        pollution = element.get("pollution")
        if pollution:
            pollution_type = pollution_types.get(pollution)
            if pollution_type:
                tool = tools.get(pollution_type.get("tool"))
                if tool:
                    if tool.get("resource") in player_inventory:
                        player_inventory[tool.get("resource")] -= 1
                        element["pollution"] = None
                        print(f"You used {pollution_type.get('tool')} to clean up pollution from {player_position}.")
                    else:
                        print(f"You need {tool.get('resource')} to use {pollution_type.get('tool')}.")
                else:
                    print(f"No tool available to clean up {pollution}.")
            else:
                print(f"No tool available to clean up {pollution}.")
        else:
            print(f"{player_position} does not contain pollution.")
    else:
        print(f"{player_position} is not a valid environment element.")

# Function to display the player inventory
def display_inventory(player_inventory):
    print("Your inventory:")
    for resource, quantity in player_inventory.items():
        print(f"{resource}: {quantity}")

# Function to collect resources from an environment element
def collect_resource(player_position, environment_elements, player_inventory):
    element = environment_elements.get(player_position)
    if element:
        resource = element.get("resource")
        if resource:
            quantity = element.get("quantity", 1)
            player_inventory[resource] = player_inventory.get(resource, 0) + quantity
            element["quantity"] = max(0, element.get("quantity", 0) - quantity)
            print(f"You collected {quantity} {resource} from {player_position}.")
        else:
            print(f"{player_position} does not contain a collectible resource.")
    else:
        print(f"{player_position} is not a valid environment element.")

# Function to clean up pollution from an environment element
def clean_pollution(player_position, environment_elements, pollution_types, tools, player_inventory):
    element = environment_elements.get(player_position)
    if element:
        pollution = element.get("pollution")
        if pollution:
            pollution_type = pollution_types.get(pollution)
            if pollution_type:
                tool = tools.get(pollution_type.get("tool"))
                if tool:
                    if tool.get("resource") in player_inventory:
                        player_inventory[tool.get("resource")] -= 1
                        element["pollution"] = None
                        print(f"You used {pollution_type.get('tool')} to clean up pollution from {player_position}.")
                    else:
                        print(f"You need {tool.get('resource')} to use {pollution_type.get('tool')}.")
                else:
                    print(f"No tool available to clean up {pollution}.")
            else:
                print(f"No tool available to clean up {pollution}.")
        else:
            print(f"{player_position} does not contain pollution.")
    else:
        print(f"{player_position} is not a valid environment element.")

# Utilize the game mechanics functions and game data
while True:
    display_map(player_position, environment_elements)
    action = input("What do you want to do? (Move/Collect/Clean/Inventory/Quit)").lower()
    if action == "move":
        player_position = move_player(player_position)
    elif action == "collect":
        collect_resource(player_position, environment_elements, player_inventory)
    elif action == "clean":
        clean_pollution(player_position, environment_elements, pollution_types, tools, player_inventory)
    elif action == "inventory":
        display_inventory(player_inventory)
    elif action == "quit":
        print("Thanks for playing Eco-Defender!")
        break
    else:
        print("Invalid action. Please try again.")
