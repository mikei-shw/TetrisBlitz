# Group 3
# 03/04/2021
# screens.stats.py - shows player statistics

# -- stats() -- allows you to see the current players statistics.

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import sys
import const

pygame.init()  # Initialize pygame


def stats():
    """
    -- displays player statistics
    :return: [void]
    """
    pygame.display.flip()

    current_player = const.PLAYERS[0]
    for player in const.PLAYERS:
        if player.current_player:
            current_player = player

    click = False
    waiting = True
    while waiting:
        # sets the game_over background
        const.WINDOW.blit(const.STATISTICS_SCREEN, (0, 0))

        # get the mouse cursor position
        x, y = pygame.mouse.get_pos()

        stat_name = const.large_font.render(str(current_player.name), True, const.YELLOW)
        stat_lines_cleared = const.sudo_medium_font.render(str(current_player.lines_cleared), True, const.YELLOW)
        stat_points_earned = const.sudo_medium_font.render(str(current_player.points_earned), True, const.YELLOW)
        stat_instant_drops = const.sudo_medium_font.render(str(current_player.instant_drops), True, const.YELLOW)
        stat_rotations = const.sudo_medium_font.render(str(current_player.rotations), True, const.YELLOW)
        fav_rot = "NONE"
        if current_player.up_rotations > current_player.down_rotations:
            fav_rot = "CLOCKWISE"
        elif current_player.up_rotations < current_player.down_rotations:
            fav_rot = "COUNTER-CLOCKWISE"
        stat_favorite_rotation = const.sudo_medium_font.render(fav_rot, True, const.YELLOW)

        current_player.add_score(0)
        top_scores = [0, 0, 0, 0, 0]
        for i in range(5):
            if current_player.scores:
                if current_player.scores[i]:
                    if current_player.scores[i] > 0:
                        top_scores.append(current_player.scores[i])
                        top_scores.sort()
                        top_scores.reverse()
                        top_scores.pop()

        score_1 = const.sudo_medium_font.render("~ " + str(top_scores[0]), True, const.DARK_GREY)
        score_2 = const.sudo_medium_font.render("~ " + str(top_scores[1]), True, const.DARK_GREY)
        score_3 = const.sudo_medium_font.render("~ " + str(top_scores[2]), True, const.DARK_GREY)
        score_4 = const.sudo_medium_font.render("~ " + str(top_scores[3]), True, const.DARK_GREY)
        score_5 = const.sudo_medium_font.render("~ " + str(top_scores[4]), True, const.DARK_GREY)

        player_level = const.small_font.render(str(current_player.level), True, const.LIGHT_GREY)
        const.WINDOW.blit(player_level, (55, 223))

        const.WINDOW.blit(score_1, (500, 339))
        const.WINDOW.blit(score_2, (500, 380))
        const.WINDOW.blit(score_3, (500, 425))
        const.WINDOW.blit(score_4, (500, 472))
        const.WINDOW.blit(score_5, (500, 515))

        const.WINDOW.blit(stat_name, (5, 180))
        const.WINDOW.blit(stat_points_earned, (20, 310))
        const.WINDOW.blit(stat_lines_cleared, (20, 400))
        const.WINDOW.blit(stat_instant_drops, (20, 490))
        const.WINDOW.blit(stat_rotations, (20, 580))
        const.WINDOW.blit(stat_favorite_rotation, (20, 670))

        percentage = current_player.exp/const.level_up(current_player.level)
        update_box = pygame.Rect(5, 243, 482 * percentage, 3)
        pygame.draw.rect(const.WINDOW, const.GREEN, update_box, 0)

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
