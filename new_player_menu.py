#Alex Cummins
#Text Dungeon Alpha
#Dungeon New Player Menu

import sys
from colors import *
from knight_stat_page import knight_stat_function
from mage_stat_page import mage_stat_function
from mercenary_stat_page import mercenary_stat_function
from stage_files.stage_one import stage_one_function

def new_player_function():
    sys.stdout.write(BLUE)
    print("\nPick a class below to start the game!\n")
    print(">>>Select a Class<<<\n>Knight(a)\n>Mage(b)\n>Mercenary(c)")
    class_selection = input(">Choice: ").lower()
    if class_selection == "a":
        knight_stat_function()
    elif class_selection == "b":
        mage_stat_function()
    elif class_selection == "c":
        mercenary_stat_function()
    else:
        sys.stdout.write(RED)
        print("\n>That seems to be an invalid input...try again!")
        new_player_function()
    sys.stdout.write(BLUE)
    class_confirmation = input("Confirm Class Selection? (y or n)").lower()
    if class_confirmation == "y":
        print("\nProceed Ahead!")
        stage_one_function()
    elif class_confirmation == "n":
        new_player_function()
    else:
        sys.stdout.write(RED)
        print("\n>That seems to be an invalid input...try again!")
        new_player_function()