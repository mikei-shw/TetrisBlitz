# Group 3
# 03/04/2021
# screens.edit_player.py - the actual game of tetris. the game screen and all of the games features. basically the
#                          items that happen when you click play

# -- leaderboard() -- the leaderboard screen with all of the scores on it ad the players who made those scores, you can
#                     only exit this screen which returns to screens.main_menu.py

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import sys
import const

pygame.init()  # Initialize pygame


# Shows the leaderboard
def leaderboard():
    pygame.display.flip()

    click = False
    waiting = True
    while waiting:
        # sets the game_over background
        const.WINDOW.blit(const.LEADERBOARD_SCREEN, (0, 0))

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

        high_scores = [[0, "None"], [0, "None"], [0, "None"], [0, "None"], [0, "None"], [0, "None"],
                       [0, "None"], [0, "None"], [0, "None"], [0, "None"]]

        for player in const.PLAYERS:
            for score in player.scores:
                high_scores.append([score, str(player.name)])
                high_scores.sort(key=lambda h_score: int(h_score[0]))
                high_scores.reverse()
                high_scores.pop()

        high_score_0 = const.medium_font.render(str(high_scores[0][0]) + " ~ " + high_scores[0][1], True, const.YELLOW)
        high_score_1 = const.medium_font.render(str(high_scores[1][0]) + " ~ " + high_scores[1][1], True,
                                               const.LIGHT_GREY)
        high_score_2 = const.medium_font.render(str(high_scores[2][0]) + " ~ " + high_scores[2][1], True, const.ORANGE)
        high_score_3 = const.medium_font.render(str(high_scores[3][0]) + " ~ " + high_scores[3][1], True, const.PURPLE)
        high_score_4 = const.medium_font.render(str(high_scores[4][0]) + " ~ " + high_scores[4][1], True, const.PURPLE)
        high_score_5 = const.medium_font.render(str(high_scores[5][0]) + " ~ " + high_scores[5][1], True, const.PURPLE)
        high_score_6 = const.medium_font.render(str(high_scores[6][0]) + " ~ " + high_scores[6][1], True, const.PURPLE)
        high_score_7 = const.medium_font.render(str(high_scores[7][0]) + " ~ " + high_scores[7][1], True, const.PURPLE)
        high_score_8 = const.medium_font.render(str(high_scores[8][0]) + " ~ " + high_scores[8][1], True, const.PURPLE)
        high_score_9 = const.medium_font.render(str(high_scores[9][0]) + " ~ " + high_scores[9][1], True, const.PURPLE)

        const.WINDOW.blit(high_score_0, (135, 205))
        const.WINDOW.blit(high_score_1, (135, 264))
        const.WINDOW.blit(high_score_2, (135, 327))
        const.WINDOW.blit(high_score_3, (135, 395))
        const.WINDOW.blit(high_score_4, (135, 454))
        const.WINDOW.blit(high_score_5, (135, 516))
        const.WINDOW.blit(high_score_6, (135, 578))
        const.WINDOW.blit(high_score_7, (135, 640))
        const.WINDOW.blit(high_score_8, (135, 704))
        const.WINDOW.blit(high_score_9, (135, 762))

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
