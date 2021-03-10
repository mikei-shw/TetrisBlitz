# Group 3
# 03/04/2021
# screens.upgrade.py -  a place to buy things in game

# -- upgrade() -- allows you to upgrade abilities with tiles (eventually)

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import sys
import const
from save import save

pygame.init()  # Initialize pygame


def upgrade():
    """
    -- the upgrade screen currently blank currently does not do anything except show the background and exit
    :return: [void]
    """
    pygame.display.flip()

    click = False
    waiting = True
    while waiting:
        for player in const.PLAYERS:
            if player.current_player == 1:
                current_player = player

        # sets the upgrade background
        const.WINDOW.blit(const.UPGRADE_SCREEN, (0, 0))

        # get the mouse cursor position
        mx, my = pygame.mouse.get_pos()
        requirements_1_met = False
        requirements_2_met = False
        requirements_3_met = False

        # ----------------------------------------------------------------- #
        # ROW CLEAR POWERUP LOGIC
        instant_clear_button = pygame.Rect(260, 320, 175, 50)
        instant_clear_level = current_player.pow_instant_clear_level
        medium_icon = pygame.transform.scale(const.POWER_ROW_CLEAR,
                                             (const.POWERUP_ICON_WIDTH_MEDIUM, const.POWERUP_ICON_WIDTH_MEDIUM))
        const.WINDOW.blit(medium_icon, (25, 150))
        instant_tiles_needed = const.price(instant_clear_level + 1)

        # Upgrade button
        if instant_clear_level < ((current_player.level - 1) / 2) and current_player.tiles >= instant_tiles_needed \
                and instant_clear_level < 20:
            const.WINDOW.blit(const.UPGRADE_BUTTON, (260, 320))
            const.WINDOW.blit(const.STORE_TILES_BACKGROUND, (430, 320))
            currency_1_display = const.medium_font.render(str(instant_tiles_needed), True, const.LIGHT_GREY)
            const.WINDOW.blit(currency_1_display, (480, 335))
            requirements_1_met = True
        else:
            const.WINDOW.blit(const.REQ_NOT_MET_BUTTON, (260, 320))
            if instant_clear_level >= ((current_player.level - 1) / 2):
                const.WINDOW.blit(const.NEED_LEVELS_BACKGROUND, (430, 320))
            elif current_player.tiles < instant_tiles_needed:
                const.WINDOW.blit(const.NEED_TILES_BACKGROUND, (430, 320))
                currency_1_display = const.medium_font.render(str(instant_tiles_needed), True, const.RED)
                const.WINDOW.blit(currency_1_display, (480, 335))
            else:
                const.WINDOW.blit(const.MAX_LEVEL_CARD, (260, 320))
                const.WINDOW.blit(const.MAX_LEVEL_HAZE, (430, 320))
        pow_name = const.medium_font.render("INSTANT ROW CLEAR", True, const.RED)
        pow_level = const.small_font.render("LEVEL " + str(instant_clear_level), True, const.LIGHT_GREY)
        description_1 = const.sudo_medium_font.render("When activated this power up allows the", True, const.RED)
        description_2 = const.sudo_medium_font.render(
            "player to delete " + str(const.pow_rows_deleted[instant_clear_level]) + " pesky rows from the bottom",
            True, const.RED)
        description_3 = const.sudo_medium_font.render(
            "of the game board every " + str(const.pow_time_to_refresh[instant_clear_level]) + " seconds!", True,
            const.RED)

        const.WINDOW.blit(pow_name, (260, 155))
        const.WINDOW.blit(pow_level, (260, 185))
        const.WINDOW.blit(description_1, (260, 210))
        const.WINDOW.blit(description_2, (260, 235))
        const.WINDOW.blit(description_3, (260, 260))

        if instant_clear_button.collidepoint((mx, my)):
            if click and requirements_1_met:
                current_player.pow_instant_clear_level += 1
                current_player.tiles -= instant_tiles_needed
                click = False
                save()
                pass

        # ----------------------------------------------------------------- #
        # SLOW TIME POWERUP LOGIC
        slow_time_button = pygame.Rect(260, 570, 175, 50)
        slow_time_level = current_player.pow_slow_time_level
        medium_icon = pygame.transform.scale(const.POWER_SLOW_TIME,
                                             (const.POWERUP_ICON_WIDTH_MEDIUM, const.POWERUP_ICON_WIDTH_MEDIUM))
        const.WINDOW.blit(medium_icon, (25, 400))
        slow_tiles_needed = const.price(slow_time_level + 1)

        # Upgrade button
        if slow_time_level < ((current_player.level - 2) / 2) and current_player.tiles >= slow_tiles_needed \
                and slow_time_level < 20:
            const.WINDOW.blit(const.UPGRADE_BUTTON, (260, 570))
            const.WINDOW.blit(const.STORE_TILES_BACKGROUND, (430, 570))
            currency_2_display = const.medium_font.render(str(slow_tiles_needed), True, const.LIGHT_GREY)
            const.WINDOW.blit(currency_2_display, (480, 585))
            requirements_2_met = True
        else:
            const.WINDOW.blit(const.REQ_NOT_MET_BUTTON, (260, 570))
            if slow_time_level >= ((current_player.level - 2) / 2):
                const.WINDOW.blit(const.NEED_LEVELS_BACKGROUND, (430, 570))
            elif current_player.tiles < slow_tiles_needed:
                const.WINDOW.blit(const.NEED_TILES_BACKGROUND, (430, 570))
                currency_2_display = const.medium_font.render(str(slow_tiles_needed), True, const.RED)
                const.WINDOW.blit(currency_2_display, (480, 585))
            else:
                const.WINDOW.blit(const.MAX_LEVEL_CARD, (260, 570))
                const.WINDOW.blit(const.MAX_LEVEL_HAZE, (430, 570))

        pow_name = const.medium_font.render("SLOW TIME", True, const.BLUE)
        pow_level = const.small_font.render("LEVEL " + str(slow_time_level), True, const.LIGHT_GREY)
        description_1 = const.sudo_medium_font.render("When activated this power up allows the", True, const.BLUE)
        description_2 = const.sudo_medium_font.render("player slow the speed of the game by a", True, const.BLUE)
        description_3 = const.sudo_medium_font.render(
            "factor of " + str(const.pow_slow_time_factor[slow_time_level]) + " permanently every "
            + str(const.pow_slow_refresh) + " seconds!", True,const.BLUE)

        const.WINDOW.blit(pow_name, (260, 405))
        const.WINDOW.blit(pow_level, (260, 435))
        const.WINDOW.blit(description_1, (260, 460))
        const.WINDOW.blit(description_2, (260, 485))
        const.WINDOW.blit(description_3, (260, 510))

        if slow_time_button.collidepoint((mx, my)):
            if click and requirements_2_met:
                current_player.pow_slow_time_level += 1
                current_player.tiles -= slow_tiles_needed
                click = False
                save()
                pass

        # ----------------------------------------------------------------- #
        # SCORE POWERUP LOGIC
        score_button = pygame.Rect(260, 820, 175, 50)
        score_level = current_player.pow_score_mult_level
        medium_icon = pygame.transform.scale(const.POWER_SCORE_MULT,
                                             (const.POWERUP_ICON_WIDTH_MEDIUM, const.POWERUP_ICON_WIDTH_MEDIUM))
        const.WINDOW.blit(medium_icon, (25, 650))
        score_tiles_needed = const.price(score_level + 1)
        # Upgrade button
        if score_level < ((current_player.level - 3) / 2) and current_player.tiles >= score_tiles_needed \
                and score_level < 20:
            const.WINDOW.blit(const.UPGRADE_BUTTON, (260, 820))
            const.WINDOW.blit(const.STORE_TILES_BACKGROUND, (430, 820))
            currency_3_display = const.medium_font.render(str(score_tiles_needed), True, const.LIGHT_GREY)
            const.WINDOW.blit(currency_3_display, (480, 830))
            requirements_3_met = True
        else:
            const.WINDOW.blit(const.REQ_NOT_MET_BUTTON, (260, 820))
            if score_level >= ((current_player.level - 3) / 2):
                const.WINDOW.blit(const.NEED_LEVELS_BACKGROUND, (430, 820))
            elif current_player.tiles < score_tiles_needed:
                const.WINDOW.blit(const.NEED_TILES_BACKGROUND, (430, 820))
                currency_3_display = const.medium_font.render(str(score_tiles_needed), True, const.RED)
                const.WINDOW.blit(currency_3_display, (480, 830))
            else:
                const.WINDOW.blit(const.MAX_LEVEL_CARD, (260, 820))
                const.WINDOW.blit(const.MAX_LEVEL_HAZE, (430, 820))

        pow_name = const.medium_font.render("SCORE MULTIPLIER", True, const.YELLOW)
        pow_level = const.small_font.render("LEVEL " + str(score_level), True, const.LIGHT_GREY)
        description_1 = const.sudo_medium_font.render("When activated this power up allows the", True, const.YELLOW)
        description_2 = const.sudo_medium_font.render("player multiply any score, exp, and tiles", True, const.YELLOW)
        description_3 = const.sudo_medium_font.render("by " + str(const.pow_mult_factor[score_level] * 100) + "% for " + str(
            const.pow_duration[score_level]) + " seconds every " + str(const.pow_mult_refresh) + " seconds!", True, const.YELLOW)

        const.WINDOW.blit(pow_name, (260, 655))
        const.WINDOW.blit(pow_level, (260, 685))
        const.WINDOW.blit(description_1, (260, 710))
        const.WINDOW.blit(description_2, (260, 735))
        const.WINDOW.blit(description_3, (260, 760))

        if score_button.collidepoint((mx, my)):
            if click and requirements_3_met:
                current_player.pow_score_mult_level += 1
                current_player.tiles -= score_tiles_needed
                click = False
                save()
                pass

        # ----------------------------------------------------------------- #
        # creates the buttons
        back_button = pygame.Rect(242, 892, 325, 54)  # back to main menu

        # if click on play button, then starts the game
        if back_button.collidepoint((mx, my)):
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
