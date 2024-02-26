# Michael Naiss
# IT-140
# Text-Based-Game

import os
import time


# Bold title
class color:
    bold = '\033[1m'
    end = '\033[0m'


# Display starting menu
def show_instructions():
    print(
        color.bold + '\t\t\t\tMISSION MEMORY: Lenita’s quest for the armor pieces\n' + color.end,
        'Objective: Find all 6 armor pieces to restore Lenita’s memory and defeat Franklin Limerick.\n\n'
        'Move commands: go North, go South, go East, go West\n'
        'Adding to Inventory: type get “item name”\n')

    input('Press "ENTER" to continue....')


# Clears screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Calling Intro and clear function
    clear()
    show_instructions()

    # Dictionary of rooms and assigning items where they are present
    rooms = {
        'Entrance tunnel': {'South': 'Technology research', 'North': 'Robotic engineering',
                            'East': 'Communication center'},
        'Technology research': {'North': 'Entrance tunnel', 'East': 'Workshop', 'item': 'Chest'},
        'Workshop': {'West': 'Technology research', 'item': 'Greaves'},
        'Robotic engineering': {'South': 'Entrance tunnel', 'East': 'Laboratory', 'item': 'Helmet'},
        'Laboratory': {'West': 'Robotic engineering', 'item': 'Shoulders'},
        'Armory': {'West': 'Communication Center', 'item': 'Buster', 'North': 'Living Quarters'},
        'Living Quarters': {'South': 'Armory', 'Boss': 'Franklin Limerick'},
        'Communication center': {'West': 'Entrance tunnel', 'East': 'Armory', 'item': 'Pulse'}
    }

    # Creating an empty inventory and defining starting room
    inventory = []
    current_room = 'Entrance tunnel'
    last_move = ''

    # Main game loop
    while True:
        print(f"You are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")
        print(last_move)

        # Item indicator
        if 'item' in rooms[current_room].keys():
            nearby_item = rooms[current_room]['item']
            if nearby_item not in inventory:
                print(f'You see {nearby_item}.')

        # Boss Encounter
        if 'Boss' in rooms[current_room].keys():

            # Lose
            if len(inventory) < 6:
                print(f"You lost the fight with {rooms[current_room]['Boss']}...\n"
                      f"Thank you for playing!")
                time.sleep(5)
                break

            # Win
            else:
                print(f"You have defeated {rooms[current_room]['Boss']} and have regained all of your memories!!\n"
                      f"Thank you for playing!")
                time.sleep(5)
                break

        # Player's move as input
        user_input = input('Enter your move:\n')
        next_move = user_input.split(' ')
        action = next_move[0].title()
        direction = ''

        if len(next_move) > 1:
            item = next_move[1:]
            direction = next_move[1].title()
            item = ' '.join(item).title()
        else:
            item = None

        # Moving between rooms
        if action == 'Go':
            try:
                current_room = rooms[current_room][direction]
                print(f'You travel {direction}.')
            except:
                print("You can't go that way.")

        # Picking up items
        elif action == 'Get':
            try:
                if item is not None and item == rooms[current_room]['item']:
                    if item not in inventory:
                        inventory.append(rooms[current_room]['item'])
                        print(f'{item} retrieved!')
                    else:
                        print(f'You already have the {item}.')
                elif item is not None:
                    print(f"Can't find {item}.")
            except:
                if item is not None:
                    print(f"Can't find {item}.")

        elif action == 'Exit':
            break
        else:
            print('Invalid Command.')


if __name__ == '__main__':
    main()
