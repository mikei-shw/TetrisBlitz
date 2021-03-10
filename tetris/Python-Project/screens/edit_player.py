# Group 3
# 03/04/2021
# screens.edit_player.py - the ability to edit a specified player, accessed through the players screen and is run when
#                          the wrench is clicked on next to a profile.

# -- edit_player() -- ability to rename and delete the player
#  |____ clicking rename brings you to screens.rename_player.py and calls rename_player()

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import sys
import const
from save import save
from screens.new_player import new_player
from screens.rename_player import rename_player
from player import Player
pygame.init()  # Initialize pygame


def edit_player(player):
    """
    -- Allows you to rename or delete a palyer from the game.
    :param player:
    :return:
    """
    pygame.display.flip()

    click = False
    waiting = True
    while waiting:
        # sets the game_over background
        const.WINDOW.blit(const.EDIT_PLAYER, (0, 0))

        # get the mouse cursor position
        x, y = pygame.mouse.get_pos()

        player_tiles = const.sudo_medium_font.render(str(player.tiles), True, const.RED)
        player_levels = const.sudo_medium_font.render(str(player.level), True, const.GREEN)
        player_name = const.sudo_medium_font.render(str(player.name), True, const.BLUE)

        const.WINDOW.blit(player_name, (75, 170))
        const.WINDOW.blit(player_tiles, (80, 235))
        const.WINDOW.blit(player_levels, (80, 305))


        # creates the buttons
        back_button = pygame.Rect(242, 892, 325, 54)  # back to main menu
        rename_button = pygame.Rect(30, 371, 158, 45)  # back to main menu
        delete_button = pygame.Rect(30, 439, 158, 45)  # back to main menu

        # if click on play button, then starts the game
        if back_button.collidepoint((x, y)):
            if click:
                return
        if rename_button.collidepoint((x, y)):
            if click:
                rename_player(player)
                save()
        if delete_button.collidepoint((x, y)):
            if click:
                player_to_remove = 0
                for i in range(len(const.PLAYERS)):
                    if const.PLAYERS[i] == player:
                        player_to_remove = i
                const.PLAYERS.append(Player("Empty"))
                const.PLAYERS.pop(player_to_remove)
                save()
                current_player_exist = False
                for player in const.PLAYERS:
                    if player.current_player:
                        current_player_exist = True
                if (const.PLAYERS[0].level != 0) and (not current_player_exist):
                    const.PLAYERS[0].set_current_player(True)
                elif (const.PLAYERS[0].level == 0) and (not current_player_exist):
                    new_player()
                    save()
                return

        # draws the buttons
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, back_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, rename_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, delete_button, 1)

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
