# Group 3
# 03/04/2021
# screens.players.py - managing players

# -- players() -- this is where you see and edit players, by clicking on a player you are able to switch to that player,
#  |              if the player does not exist it prompts you to create a new one. If you click the wrench on the
#  |              side of a player it will send you to edit the player.
#  |____ clicking any player information selects it. If the player DNE it brings you to screens.new_player.py
#  |     and calls new_player()
#  |____ clicking the wrench brings you to screens.edit_player.py and call edit_players()

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import sys
import const
from save import save
from screens.edit_player import edit_player
from screens.new_player import new_player
pygame.init()  # Initialize pygame


def players():
    """
    -- allows you to edit modify create and delete players from the game.
    :return: [void]
    """
    pygame.display.flip()

    click = False
    waiting = True
    while waiting:
        # sets the game_over background
        const.WINDOW.blit(const.PLAYERS_SCREEN, (0, 0))

        # get the mouse cursor position
        mx, my = pygame.mouse.get_pos()

        # creates the buttons
        new_player_button = pygame.Rect(175, 817, 440, 55)  # back to main menu
        back_button = pygame.Rect(242, 892, 320, 54)  # back to main menu

        # if click on new player button to try and make a new player
        actual_players = 0
        for player in const.PLAYERS:
            if player.level > 0:
                actual_players += 1
        if new_player_button.collidepoint((mx, my)):
            if click and actual_players < 10:
                new_player()  # problem: it doesn't restart the game

        # if click on play button, then starts the game
        if back_button.collidepoint((mx, my)):
            if click:
                return  # problem: it doesn't restart the game

        # draws the buttons
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, new_player_button, 1)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, back_button, 1)

        for player in const.PLAYERS:
            if player.current_player:
                current_player = player
        if current_player is None:
            new_player()

        # PLAYER 0
        player0_name = const.medium_font.render(str(const.PLAYERS[0].name), True, const.BLUE)
        player0_tiles = const.medium_font.render(str(const.PLAYERS[0].tiles), True, const.RED)
        player0_level = const.medium_font.render(str(const.PLAYERS[0].level), True, const.GREEN)

        # PLAYER 1
        player1_name = const.medium_font.render(str(const.PLAYERS[1].name), True, const.BLUE)
        player1_tiles = const.medium_font.render(str(const.PLAYERS[1].tiles), True, const.RED)
        player1_level = const.medium_font.render(str(const.PLAYERS[1].level), True, const.GREEN)

        # PLAYER 2
        player2_name = const.medium_font.render(str(const.PLAYERS[2].name), True, const.BLUE)
        player2_tiles = const.medium_font.render(str(const.PLAYERS[2].tiles), True, const.RED)
        player2_level = const.medium_font.render(str(const.PLAYERS[2].level), True, const.GREEN)

        # PLAYER 3
        player3_name = const.medium_font.render(str(const.PLAYERS[3].name), True, const.BLUE)
        player3_tiles = const.medium_font.render(str(const.PLAYERS[3].tiles), True, const.RED)
        player3_level = const.medium_font.render(str(const.PLAYERS[3].level), True, const.GREEN)

        # PLAYER 4
        player4_name = const.medium_font.render(str(const.PLAYERS[4].name), True, const.BLUE)
        player4_tiles = const.medium_font.render(str(const.PLAYERS[4].tiles), True, const.RED)
        player4_level = const.medium_font.render(str(const.PLAYERS[4].level), True, const.GREEN)

        # PLAYER 5
        player5_name = const.medium_font.render(str(const.PLAYERS[5].name), True, const.BLUE)
        player5_tiles = const.medium_font.render(str(const.PLAYERS[5].tiles), True, const.RED)
        player5_level = const.medium_font.render(str(const.PLAYERS[5].level), True, const.GREEN)

        # PLAYER 6
        player6_name = const.medium_font.render(str(const.PLAYERS[6].name), True, const.BLUE)
        player6_tiles = const.medium_font.render(str(const.PLAYERS[6].tiles), True, const.RED)
        player6_level = const.medium_font.render(str(const.PLAYERS[6].level), True, const.GREEN)

        # PLAYER 7
        player7_name = const.medium_font.render(str(const.PLAYERS[7].name), True, const.BLUE)
        player7_tiles = const.medium_font.render(str(const.PLAYERS[7].tiles), True, const.RED)
        player7_level = const.medium_font.render(str(const.PLAYERS[7].level), True, const.GREEN)

        # PLAYER 8
        player8_name = const.medium_font.render(str(const.PLAYERS[8].name), True, const.BLUE)
        player8_tiles = const.medium_font.render(str(const.PLAYERS[8].tiles), True, const.RED)
        player8_level = const.medium_font.render(str(const.PLAYERS[8].level), True, const.GREEN)

        # PLAYER 9
        player9_name = const.medium_font.render(str(const.PLAYERS[9].name), True, const.BLUE)
        player9_tiles = const.medium_font.render(str(const.PLAYERS[9].tiles), True, const.RED)
        player9_level = const.medium_font.render(str(const.PLAYERS[9].level), True, const.GREEN)

        # PLAYER 0
        const.WINDOW.blit(player0_name, (105, 205))
        const.WINDOW.blit(player0_tiles, (438, 205))
        const.WINDOW.blit(player0_level, (602, 205))

        # PLAYER 1
        const.WINDOW.blit(player1_name, (105, 261))
        const.WINDOW.blit(player1_tiles, (438, 261))
        const.WINDOW.blit(player1_level, (602, 261))

        # PLAYER 2
        const.WINDOW.blit(player2_name, (105, 318))
        const.WINDOW.blit(player2_tiles, (438, 318))
        const.WINDOW.blit(player2_level, (602, 318))

        # PLAYER 3
        const.WINDOW.blit(player3_name, (105, 375))
        const.WINDOW.blit(player3_tiles, (438, 375))
        const.WINDOW.blit(player3_level, (602, 375))

        # PLAYER 4
        const.WINDOW.blit(player4_name, (105, 433))
        const.WINDOW.blit(player4_tiles, (438, 433))
        const.WINDOW.blit(player4_level, (602, 433))

        # PLAYER 5
        const.WINDOW.blit(player5_name, (105, 489))
        const.WINDOW.blit(player5_tiles, (438, 489))
        const.WINDOW.blit(player5_level, (602, 489))

        # PLAYER 6
        const.WINDOW.blit(player6_name, (105, 545))
        const.WINDOW.blit(player6_tiles, (438, 545))
        const.WINDOW.blit(player6_level, (602, 545))

        # PLAYER 7
        const.WINDOW.blit(player7_name, (105, 603))
        const.WINDOW.blit(player7_tiles, (438, 603))
        const.WINDOW.blit(player7_level, (602, 603))

        # PLAYER 8
        const.WINDOW.blit(player8_name, (105, 660))
        const.WINDOW.blit(player8_tiles, (438, 660))
        const.WINDOW.blit(player8_level, (602, 660))

        # PLAYER 9
        const.WINDOW.blit(player9_name, (105, 718))
        const.WINDOW.blit(player9_tiles, (438, 718))
        const.WINDOW.blit(player9_level, (602, 718))

        # PLAYER SELECT MENU
        player0_select = pygame.Rect(64, 190, 610, 50)
        player1_select = pygame.Rect(64, 247, 610, 50)
        player2_select = pygame.Rect(64, 305, 610, 50)
        player3_select = pygame.Rect(64, 360, 610, 50)
        player4_select = pygame.Rect(64, 420, 610, 50)
        player5_select = pygame.Rect(64, 480, 610, 50)
        player6_select = pygame.Rect(64, 535, 610, 50)
        player7_select = pygame.Rect(64, 590, 610, 50)
        player8_select = pygame.Rect(64, 645, 610, 50)
        player9_select = pygame.Rect(64, 708, 610, 50)

        # PLAYER EDIT MENU
        player0_edit = pygame.Rect(680, 190, 50, 50)
        player1_edit = pygame.Rect(680, 250, 50, 50)
        player2_edit = pygame.Rect(680, 305, 50, 50)
        player3_edit = pygame.Rect(680, 360, 50, 50)
        player4_edit = pygame.Rect(680, 420, 50, 50)
        player5_edit = pygame.Rect(680, 480, 50, 50)
        player6_edit = pygame.Rect(680, 535, 50, 50)
        player7_edit = pygame.Rect(680, 590, 50, 50)
        player8_edit = pygame.Rect(680, 645, 50, 50)
        player9_edit = pygame.Rect(680, 710, 50, 50)

        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player0_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player1_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player2_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player3_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player4_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player5_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player6_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player7_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player8_edit, 2)
        pygame.draw.rect(const.WINDOW, const.DARK_GREY, player9_edit, 2)


        # PLAYER 0 SELECTED
        if const.PLAYERS[0].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player0_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player0_select, 1)

        # PLAYER 1 SELECTED
        if const.PLAYERS[1].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player1_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player1_select, 1)

        # PLAYER 2 SELECTED
        if const.PLAYERS[2].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player2_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player2_select, 1)

        # PLAYER 3 SELECTED
        if const.PLAYERS[3].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player3_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player3_select, 1)

        # PLAYER 4 SELECTED
        if const.PLAYERS[4].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player4_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player4_select, 1)

        # PLAYER 5 SELECTED
        if const.PLAYERS[5].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player5_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player5_select, 1)

        # PLAYER 6 SELECTED
        if const.PLAYERS[6].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player6_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player6_select, 1)

        # PLAYER 7 SELECTED
        if const.PLAYERS[7].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player7_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player7_select, 1)

        # PLAYER 8 SELECTED
        if const.PLAYERS[8].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player8_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player8_select, 1)

        # PLAYER 9 SELECTED
        if const.PLAYERS[9].current_player:
            pygame.draw.rect(const.WINDOW, const.BLUE, player9_select, 2)
        else:
            pygame.draw.rect(const.WINDOW, const.DARK_GREY, player9_select, 1)

        if player0_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[0].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[0].set_current_player(True)
                pygame.draw.rect(const.WINDOW, const.WHITE, player0_select, 1)
                click = False
                pass
        elif player1_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[1].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[1].set_current_player(True)
                click = False
                pass
        elif player2_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[2].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[2].set_current_player(True)
                click = False
                pass
        elif player3_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[3].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[3].set_current_player(True)
                click = False
                pass
        elif player4_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[4].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[4].set_current_player(True)
                click = False
                pass
        elif player5_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[5].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[5].set_current_player(True)
                click = False
                pass
        elif player6_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[6].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[6].set_current_player(True)
                click = False
                pass
        elif player7_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[7].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[7].set_current_player(True)
                click = False
                pass
        elif player8_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[8].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[8].set_current_player(True)
                click = False
                pass
        elif player9_select.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[9].level == 0:
                    new_player()
                for player in const.PLAYERS:
                    player.set_current_player(False)
                const.PLAYERS[9].set_current_player(True)
                click = False
                pass

        # PLAYER EDIT CLICKED
        if player0_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[0].level == 0:
                    return
                else:
                    edit_player(const.PLAYERS[0])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player1_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[1].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[1])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player2_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[2].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[2])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player3_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[3].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[3])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player4_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[4].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[4])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player5_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[5].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[5])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player6_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[6].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[6])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player7_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[7].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[7])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player8_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[8].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[8])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        elif player9_edit.collidepoint((mx, my)):
            if click:
                if const.PLAYERS[9].level == 0:
                    click = False
                else:
                    edit_player(const.PLAYERS[9])
                    pygame.draw.rect(const.WINDOW, const.RED, player0_edit, 1)
                click = False
                pass
        save()
        pygame.display.flip()

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
