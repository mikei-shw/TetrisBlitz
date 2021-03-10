# Group 3
# 03/04/2021
# const.py - ability to save an load changes

# CONSTANTS FILE -- VARIABLES THAT ARE USED THROUGH OUT THE PROGRAM, MOST UNCHANGED
# -- level_up() -- decides when the threshold for leveling up is, the numbers it returns will never change
# -- PLAYERS[]  -- holds the players in the game.

import pygame

pygame.init()  # Initialize pygame

# Main Constants
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 810
POWERUP_ICON_WIDTH_MEDIUM = 220
POWERUP_ICON_WIDTH_SMALL = 60

# Block Constants
DEV = True
BLOCK_LEN = 50
GAME_WIDTH = 10
GAME_HEIGHT = 20
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 22, 22)
ORANGE = pygame.Color(255, 107, 16)
YELLOW = pygame.Color(255, 204, 0)
GREEN = pygame.Color(50, 212, 41)
FOREST_GREEN = pygame.Color(50, 205, 50)
BLUE = pygame.Color(0, 194, 246)
PURPLE = pygame.Color(165, 0, 212)
INDIGO = pygame.Color(7, 73, 255)
DARK_GREY = pygame.Color(32, 32, 32)
LIGHT_GREY = pygame.Color(217, 217, 217)
WHITE = pygame.Color(255, 255, 255)

w_width = 600
w_height = 600

# loads the file for all backgrounds
MAIN_MENU_SCREEN = pygame.image.load('resources/start_screen.png')
GAME_SCREEN = pygame.image.load('resources/game_screen.png')
GAME_OVER_SCREEN = pygame.image.load('resources/game_over_screen.png')
PAUSE_SCREEN = pygame.image.load('resources/paused_screen.png')
LEADERBOARD_SCREEN = pygame.image.load('resources/leaderboard_screen.png')
OPTIONS_SCREEN = pygame.image.load('resources/options_screen.png')
NEW_PLAYER_SCREEN = pygame.image.load('resources/new_player_screen.png')
STORE_SCREEN = pygame.image.load('resources/store_screen.png')
PLAYERS_SCREEN = pygame.image.load('resources/players_screen.png')
UPGRADE_SCREEN = pygame.image.load('resources/upgrade_screen.png')
STATISTICS_SCREEN = pygame.image.load('resources/statistics_screen.png')
EDIT_PLAYER = pygame.image.load('resources/edit_player_screen.png')

# loads the file for all "sprites"
TILE_ICON = pygame.image.load('resources/tile_icon.png')
POWER_ROW_CLEAR = pygame.image.load('resources/pow_clear_row.png')
POWER_SLOW_TIME = pygame.image.load('resources/pow_slow_time.png')
POWER_SCORE_MULT = pygame.image.load('resources/pow_score_mult.png')
UPGRADE_BUTTON = pygame.image.load('resources/upgrade_button.png')
REQ_NOT_MET_BUTTON = pygame.image.load('resources/req_not_met_button.png')
STORE_TILES_BACKGROUND = pygame.image.load('resources/store_tiles_background.png')
MAX_LEVEL_CARD = pygame.image.load('resources/max_level.png')
MAX_LEVEL_HAZE = pygame.image.load('resources/max_level_haze.png')
NEED_TILES_BACKGROUND = pygame.image.load('resources/need_tiles_background.png')
NEED_LEVELS_BACKGROUND = pygame.image.load('resources/need_levels_background.png')

# FONTS
large_font = pygame.font.SysFont('comicsans', 60)
medium_font = pygame.font.SysFont('comicsans', 35)
sudo_medium_font = pygame.font.SysFont('comicsans', 28)
sudo_small_font = pygame.font.SysFont('comicsans', 24)
small_font = pygame.font.SysFont('comicsans', 20)

# WINDOW
WINDOW = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# PYGAME CLOCK SETUP
CLOCK = pygame.time.Clock()

# 10x20 array keeping track of which blocks have been placed. Initially all blank (B)
# E = empty, R = red, O = orange, Y = yellow, G = green, B = blue, P = purple, Q = gray
placed_blocks = [[BLACK] * GAME_WIDTH for r in range(GAME_HEIGHT)]

# Dict containing info for building pre-set arrangements
ARR_TYPES = {'L': [[[0, 0, 1], [1, 2, 0]], PURPLE],
             'O': [[[0, 1, 1], [1, 0, 1]], GREEN],
             'J': [[[1, 1, 1], [0, 1, 2]], RED],
             'I': [[[0, 0, 0], [-1, 1, 2]], BLUE],
             'S': [[[0, 1, 1], [-1, 0, 1]], YELLOW],
             'T': [[[1, 0, 0], [0, -1, 1]], ORANGE],
             'Z': [[[0, 1, 1], [1, 0, -1]], INDIGO]
             }

# IM NOT SURE
ACTIVE_ARRANGEMENTS = []

# PLAYERS IN THE GAME
PLAYERS = []

# POWER-UPS REQUIREMENTS
REQUIREMENTS = ["LEVEL TOO LOW", "NOT ENOUGH TILES"]

# INSTANT CLEAR LEVEL ARRAYS
pow_rows_deleted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pow_time_to_refresh = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70]

# SLOW TIME LEVEL ARRAYS
pow_slow_time_factor = [0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 10]
pow_slow_refresh = 75
# SCORE MULTIPLIER LEVELS
pow_mult_factor = [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pow_duration = [5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
pow_mult_refresh = 30

def price(pow_level):
    if pow_level == 0:
        return 0
    cost = (300 * pow_level) + price(pow_level - 1)
    return int(cost)


def level_up(current_level):
    """
    -- finds out wht the experience threshold needed to level up. According to the equation [(level x 1000) x 1.25]
    -- for example if you are level 2 the experience you need to get to level 3 is (2 x 1000) x 1.25 = 2500
    :param current_level:
    :return: [int]
    """
    exp_needed = (1000 * current_level) * 1.25
    return exp_needed
