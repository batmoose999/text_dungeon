#Alex Cummins
#Text Dungeon Alpha
#Dungeon Main Menu

import sys
from colors import *
from dungeon_help import dungeon_help_menu
from new_player_menu import new_player_function

def mainMenu():
    sys.stdout.write(CYAN)
    print("")
    print(">>>Text Dungeon<<<\n>Options<\n>Play a Dungeon Quest(p)<\n>Help(h)<\n>Quit(q)<")
    print("")

    selection = input(">Choice: ").lower()
    if selection == "p":
        new_player_function()
    elif selection == "h":
        dungeon_help_menu()
        mainMenu()
    elif selection == "q":
        quit()
    else:
        sys.stdout.write(RED)
        print("\n>That seems to be an invalid input...try again!")
        mainMenu()

mainMenu()