import os
import sys
import time
from grid import Grid


def grid_size():
    size = int(sys.argv[1])
    return size


def display_title():
    print("----------------------")
    print("|    Brain Buster    |")
    print("----------------------")
    print()


def display_menu():
    print("1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up - reveal the grid")
    print("4. New game")
    print("5. Exit")
    print()


size = grid_size()

if size == 2 or size == 4 or size == 6:
    grid = Grid(size)

else:
    print("Please indicate the correct desired grid size (2 or 4 or 6)")
    exit(0)

if size == 2:
    elements = ['1', '1', '2', '2']
    for element in elements:
        grid.place_elements(element)
elif size == 4:
    elements = ['1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8']
    for element in elements:
        grid.place_elements(element)

elif size == 6:
    elements = ['1', '1', '2', '2','3', '3', '4', '4', '5', '5', '6', '6',
                '7', '7', '8', '8', '9', '9', '10', '10', '11', '11', '12', '12',
                '13', '13', '14', '14', '15', '15', '16', '16', '17', '17', '18', '18']
    for element in elements:
        grid.place_elements(element)
else:
    print("Please submit a correct array size in the command line: python3 game.py [2 or 4 or 6]")

userInput = 0
counter = 0
while True:
    display_title()
    grid.display()
    display_menu()
    userInput = input("Select: ")

    if userInput == "1":
        os.system("clear")

        display_title()
        grid.display()
        display_menu()

        grid.uncover_pair()

    elif userInput == "2":
        cell_coordinate = input("Enter cell coordinates to uncover (e.g., a0) : ")
        os.system("clear")
        grid.uncover(cell_coordinate)

    elif userInput == "3":
        os.system("clear")
        grid.uncover_all()

    elif userInput == "4":
        new_size = int(input("Please enter the size of your new game (e.g. 2, 4, 6): "))
        os.system("clear")
        grid.reset_game(new_size)

    elif userInput == "5":
        print("Thank you for playing.")
        break

    else:
        print("Please input a correct menu option.")
        time.sleep(1.5)
        os.system("clear")