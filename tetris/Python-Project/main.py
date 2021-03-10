# Group 3
# 03/04/2021
# main.py -- Start file

# -- main() -- pretty self explanatory (where the program starts)

import const
import pygame

from save import load
from screens.main_menu import main_menu
from player import Player
from screens.new_player import new_player
pygame.init()  # Initialize pygame


def main():
    """
    -- Main function of the program which loads the save data from game_save.txt, initializes the players, and
    -- then calls the main menu (screen) to start the bulk of the program.
    :return: [void]
    """
    for i in range(10):
        const.PLAYERS.append(Player("Empty"))
    load()
    if const.PLAYERS[0].level == 0:
        new_player()
        const.PLAYERS[0].current_player = True
    click = False
    main_menu(click)


if __name__ == "__main__":
    main()
