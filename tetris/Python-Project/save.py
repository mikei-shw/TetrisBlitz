# Group 3
# 03/04/2021
# save.py - ability to save an load changes

# -- save() -- saves the state of the players in game_save.txt
# -- load() -- loads the game to its previous state (puts players bak in)

import const


def save():
    """
    -- opens game_save.txt and writes over the old file. writes each players values to the document inorder
    -- to save them which will bve read when loading. (tries to adda score to the player inorder to make sure that there
    -- are no more than 10 elements in each score array, if array is full the pointless value will be removed)
    :return: [void]
    """
    with open("game_save.txt", "w") as save_file:
        for player in const.PLAYERS:
            player.add_score(-1)
            save_file.write(str(player))


def load():
    """
    -- reads in game_save.txt and adds each of the values to each blank player
    -- in the const.PLAYERS array.
    :return:
    """
    with open("game_save.txt", "a") as save_file:
        pass
    with open("game_save.txt", "r") as save_file:
        information = save_file.readlines()
        if information:
            for player in const.PLAYERS:

                # NAME
                player.name = str(information.pop(0).strip())

                # SCORES
                scores = information.pop(0).strip()
                str_scores = scores.split()
                for score in str_scores:
                    player.scores.append(int(score))

                # TILES
                player.tiles = int(information.pop(0).strip())

                # LEVEL
                player.level = int(information.pop(0).strip())

                # CURRENT PLAYER
                player.current_player = int(information.pop(0).strip())

                # LINES CLEARED
                player.lines_cleared = int(information.pop(0).strip())

                # POINTS EARNED
                player.points_earned = int(information.pop(0).strip())

                # INSTANT DROPS
                player.instant_drops = int(information.pop(0).strip())

                # ROTATIONS
                player.rotations = int(information.pop(0).strip())
                player.up_rotations = int(information.pop(0).strip())
                player.down_rotations = int(information.pop(0).strip())

                # HIGEST GAME LEVEL
                player.highest_game_level = int(information.pop(0).strip())

                # PLAYER EXP
                player.exp = int(information.pop(0).strip())

                # INSTANT CLEAR LEVEL
                player.pow_instant_clear_level = int(information.pop(0).strip())
                # SLOW DOWN LEVEL
                player.pow_slow_time_level = int(information.pop(0).strip())
                # SCORE MULTIPLIER LEVEL
                player.pow_score_mult_level = int(information.pop(0).strip())
