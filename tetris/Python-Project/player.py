# Group 3
# 03/04/2021
# player.py - defines the player class (the object which plays the game)

# -- get_name(self) -- returns name
# -- get_score(self) -- returns scores arr
# -- get_tiles(self) -- returns tiles
# -- get_level(self) -- returns player level
# -- add_score(self, scores) -- adds score to scores arr
# -- set_current_player(self, is_current) -- sets the current player
# -- highest_level_check(self, level) -- checks and sets the highest game level achieved
# -- add_exp(self, score) -- adds experience, levels up, and resets experience

import const


class Player:
    def __init__(self, name):
        """
        -- basic constructor fo a player. Makes a blank user profile
        :param name: [str]
        """
        self.name = name
        self.scores = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.tiles = 0  # currency
        self.level = 0  # player_level
        self.current_player = 0

        self.lines_cleared = 0
        self.points_earned = 0
        self.instant_drops = 0
        self.rotations = 0
        self.up_rotations = 0
        self.down_rotations = 0
        self.highest_game_level = 0
        self.exp = 0
        self.pow_instant_clear_level = 0
        self.pow_slow_time_level = 0
        self.pow_score_mult_level = 0

    def __str__(self):
        """
        -- ability to print the player in string form. Used to save the player information. If you want to save player
        -- data add it to this string
        :return: [srt]
        """
        save_scores = ""
        current_player = ""
        if self.scores:
            for score in self.scores:
                save_scores += str(score)
                save_scores += " "
        if self.current_player:
            current_player = "1"
        else:
            current_player = "0"

        player_info = str(self.name) + "\n" + save_scores + "\n" + str(self.tiles) + "\n" \
                      + str(self.level) + "\n" + current_player + "\n" + str(self.lines_cleared) + "\n" \
                      + str(self.points_earned) + "\n" + str(self.instant_drops) + "\n" + str(self.rotations) + "\n" \
                      + str(self.up_rotations) + "\n" + str(self.down_rotations) + "\n" \
                      + str(self.highest_game_level) + "\n" + str(self.exp) + "\n" \
                      + str(self.pow_instant_clear_level) + "\n" + str(self.pow_slow_time_level) + "\n" \
                      + str(self.pow_score_mult_level) + "\n"
        return player_info

    def get_name(self):
        """
        -- returns the name of the player
        :return: [str]
        """
        return self.name

    def get_score(self):
        """
        -- returns the score of the player
        :return: list[int]
        """
        return self.scores

    def get_tiles(self):
        """
        --returns the amount of currency the player has
        :return: [int]
        """
        return self.tiles

    def get_level(self):
        """
        -- returns the level of the player
        :return: [int]
        """
        return self.level

    def add_score(self, score):
        """
        -- adds the score given to the list of scores the player has obtained, because we only want to keep
        -- the highest 10 scores we then sort the array and pop off the last entry. Also used for saving to\
        -- make sure that no scores array gets longer than 10.
        :param score: [int]
        :return: [void]
        """
        self.scores.append(int(score))
        self.scores.sort()
        self.scores.reverse()
        while len(self.scores) > 10:
            self.scores.pop()

    def add_tiles(self, tiles):
        """
        -- adds the number of tiles specified to the amount of tiles (currency) the player has
        :param tiles: [int]
        :return: [void]
        """
        self.tiles += tiles

    def set_current_player(self, is_current):
        """
        -- function that sets the status of current player.
        -- <False> makes the player not the current player
        -- <True> makes the player the current player
        :param is_current: [bool]
        :return: [void]
        """
        self.current_player = is_current

    def highest_level_check(self, level):
        """
        -- checks if the given level is the highest level achieved and if so,
        -- makes that the new highest level obtained
        :param level: [int]
        :return: [void]
        """
        if level > self.highest_game_level:
            self.highest_game_level = level

    def add_exp(self, score):
        """
        -- adds experience to the player and if that experience reaches the specified threshold
        -- (determined by const.level_up()) increases the level the player is, and resets the exp counter.
        :param score: [int]
        :return: [void]
        """
        self.exp += int(score)
        if self.exp >= const.level_up(self.level):
            self.level += 1
            self.exp = 0


