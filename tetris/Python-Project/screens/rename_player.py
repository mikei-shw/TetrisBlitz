# Group 3
# 03/04/2021
# screens.rename_player.py - renaming a player

# -- rename_player() -- this screen allows you to rename a player (only letters) (all caps) (max 8 char)

import pygame
import const
from player import Player

pygame.init()  # Initialize pygame


def rename_player(player):
    """
    -- allows you top rename the specified player
    :param player: [Player]
    :return: [void]
    """
    click = False
    screen = pygame.display.set_mode((810, 1000))
    const.WINDOW.blit(const.NEW_PLAYER_SCREEN, (0, 0))
    font = const.large_font
    clock = const.CLOCK
    input_box = pygame.Rect(220, 380, 375, 64)
    color_inactive = const.DARK_GREY
    color_active = const.BLUE
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        player.name = text.upper()
                        text = ''
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        txt_surface = font.render(text.upper(), True, color)
                        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))
                    elif event.unicode.isalpha():
                        if len(text) < 8:
                            if event.unicode == 8:
                                text += 0
                            else:
                                text += event.unicode
                                text.upper()

        update_box = pygame.Rect(220, 380, 375, 64)
        pygame.draw.rect(const.WINDOW, const.LIGHT_GREY, update_box, 0)
        pygame.display.flip()
        # Render the current text.
        txt_surface = font.render(text.upper(), True, color)
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 10))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
