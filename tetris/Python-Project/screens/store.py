# Group 3
# 03/04/2021
# screens.store.py -  a place to buy things in game

# -- store() -- allows you to buy things with tiles (eventually)

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import sys
import const

pygame.init()  # Initialize pygame


def store():
    """
    -- the store screen currently blank currently does not do anything except show the background and exit
    :return: [void]
    """
    pygame.display.flip()

    click = False
    waiting = True
    while waiting:
        # sets the game_over background
        const.WINDOW.blit(const.STORE_SCREEN, (0, 0))

        # get the mouse cursor position
        x, y = pygame.mouse.get_pos()

        # creates the buttons
        back_button = pygame.Rect(242, 892, 325, 54)  # back to main menu

        # if click on play button, then starts the game
        if back_button.collidepoint((x, y)):
            if click:
                return  # problem: it doesn't restart the game

        # draws the buttons
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, back_button, 1)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        const.CLOCK.tick(30)
