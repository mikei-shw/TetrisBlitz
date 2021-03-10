# Group 3
# 03/04/2021
# screens.main_menu.py - the main menu from which to get to every part of this game

# -- main_menu(click) -- this is the main menu from which you can go pretty much anywhere in the game, from here you
#  |                     from here you can call most of the game screens
#  |____ clicking play brings you to screens.game.py and calls game()
#  |____ clicking leaderboard brings you to screens.leaderboard.py and calls leaderboard()
#  |____ clicking options brings you to screens.options.py and calls options()
#  |____ clicking stats brings you to screens.stats.py and calls stats()
#  |____ clicking store brings you to screens.store.py and calls rename_player()
#  |____ clicking upgrade brings you to screens.upgrade.py and calls upgrade()

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import sys
import const
from screens.game import game
from screens.leaderboard import leaderboard
from screens.new_player import new_player
from screens.options import options
from screens.stats import stats
from screens.store import store
from screens.upgrade import upgrade
from screens.players import players
from save import save
pygame.init()  # Initialize pygame


def main_menu(click):
    """
    -- the main menu of the game from which all screens are accessible
    :param click: [bool]
    :return: [void]
    """
    run = True
    while run:
        for player in const.PLAYERS:
            if player.current_player == 1:
                current_player = player

        const.WINDOW.fill((0, 0, 0))

        # main menu image
        const.WINDOW.blit(const.MAIN_MENU_SCREEN, (0, 0))

        # get the mouse cursor position
        mx, my = pygame.mouse.get_pos()

        # creates the buttons

        play_button = pygame.Rect(0, 609, 477, 66)
        leaderboard_button = pygame.Rect(0, 696, 477, 66)
        options_button = pygame.Rect(0, 786, 477, 66)
        exit_button = pygame.Rect(0, 880, 477, 66)
        stats_button = pygame.Rect(590, 608, 477, 70)
        store_button = pygame.Rect(590, 700, 477, 70)
        upgrade_button = pygame.Rect(590, 788, 477, 70)
        players_button = pygame.Rect(590, 877, 477, 70)

        player_tiles = const.small_font.render("T: " + str(current_player.tiles), True, const.RED)
        player_levels = const.small_font.render("L: " + str(current_player.level), True, const.GREEN)
        player_name = const.small_font.render(str(current_player.name), True, const.BLUE)
        player_points = const.small_font.render("P: " + str(current_player.points_earned), True, const.YELLOW)

        const.WINDOW.blit(player_points, (624, 628))
        const.WINDOW.blit(player_tiles, (624, 719))
        const.WINDOW.blit(player_levels, (624, 807))
        const.WINDOW.blit(player_name, (624, 898))

        # if click on play button, then starts the game
        if play_button.collidepoint((mx, my)):
            if click:
                game()
                click = False
                save()
                pass

        elif leaderboard_button.collidepoint((mx, my)):
            if click:
                leaderboard()
                click = False
                save()
                pass

        elif options_button.collidepoint((mx, my)):
            if click:
                options()
                click = False
                save()
                pass

        elif exit_button.collidepoint((mx, my)):
            if click:
                for event in pygame.event.get():
                    run = False

        elif stats_button.collidepoint((mx, my)):
            if click:
                stats()
                click = False
                save()
                pass

        elif store_button.collidepoint((mx, my)):
            if click:
                store()
                click = False
                save()
                pass

        elif upgrade_button.collidepoint((mx, my)):
            if click:
                upgrade()
                click = False
                save()
                pass

        elif players_button.collidepoint((mx, my)):
            if click:
                players()
                click = False
                save()
                pass

        # draws rectangle shaped buttons
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, play_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, leaderboard_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, options_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, exit_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, stats_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, store_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, upgrade_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, players_button, 1)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        const.CLOCK.tick(30)
    pygame.quit()
