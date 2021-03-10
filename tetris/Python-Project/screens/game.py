# Group 3
# 03/04/2021
# screens.edit_player.py - the actual game of tetris. the game screen and all of the games features. basically the
#                          items that happen when you click play

# -- game() -- the game of tetris when X is hit the pause() function is called, when the game is lost the game
#  |           over function is called
#  |____ clicking rename brings you to screens.rename_player.py and calls rename_player()
#
# -- game_over() -- the game is over, you can eiter restart which calls game() or exit which returns to the screen
#  |                that called it. <currently a bug> if you hit restart and you exit it returns you to the last
#  |                game players over screen
#  |____ clicking exit should take you to screens.main_menu.py
#
# -- pause() -- the game is paused and the game window is frozen, yopu are able to resume which resumes the game or
#               exit which returns.

import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_x,
    K_1,
    K_2,
    K_3,
    KEYDOWN,
    QUIT
)
import sys
import random
import block
import const
from save import save

pygame.init()  # Initialize pygame


def game():
    save()
    current_player = const.PLAYERS[0]
    for player in const.PLAYERS:
        if player.current_player:
            current_player = player

    # Game Variables
    score = 0  # Score
    timer = 30  # Countdown Timer used fro game level
    pow_timer = 0  # Used for powerup usage
    dt = 0  # something 1
    tick = 10
    lines_cleared = 0  # number of lines cleared
    tick_multiplier = 0
    game_level = 1
    p1_last_used = 0  # POWERUP 1 time last used (Instant Clear)
    p2_last_used = 0  # POWERUP 2 time last used (Slow Time)
    p3_last_used = 0  # POWERUP 3 time last used (Score Mult)
    score_mult = const.pow_mult_factor[current_player.pow_score_mult_level]
    score_mult_on = False
    p3_multiplier = 1

    click = False  # something 2

    # Set up the placed blocks again. Allows the game to restart
    placed_blocks = [[const.BLACK] * const.GAME_WIDTH for r in range(const.GAME_HEIGHT)]

    # Pick the first block to drop
    rand_arrange_type = random.choice("LOJISTZ")
    next_block = block.Arrangement(rand_arrange_type)

    running = True
    paused = False
    while running:

        # pause the game if necessary
        events = pygame.event.get()
        if K_x in [e.key for e in events if e.type == KEYDOWN]:
            paused = False if paused else True

        if not paused:
            # if there is no active arrangement
            if len(const.ACTIVE_ARRANGEMENTS) == 0:
                # create an arrangement.
                const.ACTIVE_ARRANGEMENTS.append(next_block)

                # choose next arrangement.
                rand_arrange_type = random.choice("LOJISTZ")
                next_block = block.Arrangement(rand_arrange_type)

            # Go through each game event
            for event in events:
                tick_multiplier = int((tick - 5) / 5)
                # Did the user close the game?
                if event.type == pygame.QUIT:
                    # running = False
                    sys.exit()

                # Did the user hit a key?
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_LEFT:
                        const.ACTIVE_ARRANGEMENTS[0].moveLeft(placed_blocks)
                        score += 1 * tick_multiplier * p3_multiplier
                        current_player.add_exp(1 * tick_multiplier * p3_multiplier)
                    elif event.key == K_RIGHT:
                        const.ACTIVE_ARRANGEMENTS[0].moveRight(placed_blocks)
                        score += 1 * tick_multiplier * p3_multiplier
                        current_player.add_exp(1 * tick_multiplier * p3_multiplier)
                    elif event.key == K_UP:
                        const.ACTIVE_ARRANGEMENTS[0].rotate(placed_blocks, clockwise=True)
                        score += 1 * tick_multiplier * p3_multiplier
                        current_player.add_exp(1 * tick_multiplier * p3_multiplier)
                        current_player.up_rotations += 1
                        current_player.rotations += 1
                    elif event.key == K_DOWN:
                        const.ACTIVE_ARRANGEMENTS[0].rotate(placed_blocks, clockwise=False)
                        score += 1 * tick_multiplier * p3_multiplier
                        current_player.add_exp(1 * tick_multiplier * p3_multiplier)
                        current_player.down_rotations += 1
                        current_player.rotations += 1
                    elif event.key == K_SPACE:
                        const.ACTIVE_ARRANGEMENTS[0].instant(placed_blocks)
                        score += 10 * tick_multiplier * p3_multiplier
                        current_player.add_exp(10 * tick_multiplier * p3_multiplier)
                        current_player.instant_drops += 1
                    elif event.key == K_1:
                        if current_player.pow_instant_clear_level and (pow_timer - p1_last_used) >= \
                                const.pow_time_to_refresh[current_player.pow_instant_clear_level]:
                            rows_to_clear = const.pow_rows_deleted[current_player.pow_instant_clear_level]
                            p1_last_used = pow_timer
                            for i in range(rows_to_clear):
                                placed_blocks.pop(19)  # Delete the full row
                                placed_blocks.insert(0, [const.BLACK] * const.GAME_WIDTH)
                                lines_cleared += 1
                                current_player.lines_cleared += 1
                                clear_multiplier = 1 + (lines_cleared * .3)
                                score += (100 * clear_multiplier) * tick_multiplier * p3_multiplier  # Increment Score
                                current_player.add_exp((100 * clear_multiplier) * tick_multiplier * p3_multiplier)
                                current_player.add_tiles(
                                    int(((100 * clear_multiplier) * tick_multiplier * p3_multiplier) / 10))
                    elif event.key == K_2:
                        if current_player.pow_slow_time_level and (pow_timer - p2_last_used) >= const.pow_slow_refresh:
                            slow_factor = const.pow_slow_time_factor[current_player.pow_slow_time_level]
                            if tick - slow_factor > 0:
                                tick -= slow_factor
                            p2_last_used = pow_timer
                    elif event.key == K_3:
                        if current_player.pow_score_mult_level and (pow_timer - p3_last_used) >= const.pow_mult_refresh:
                            p3_last_used = pow_timer
                            score_mult_on = True

            if pow_timer - p3_last_used > const.pow_duration[current_player.pow_score_mult_level]:
                score_mult_on = False

            # If score multiplier is active set score multiplier to
            if score_mult_on:
                p3_multiplier = const.pow_mult_factor[current_player.pow_score_mult_level]
            else:
                p3_multiplier = 1

            # Apply gravity to the active block arrangement
            for a in const.ACTIVE_ARRANGEMENTS:
                # If we can't move down any further
                if not a.moveDown(placed_blocks):

                    # Get the type of arrangement a is to determine the color block
                    color = const.ARR_TYPES[a.arrange_type][1]

                    # Place permanent blocks in the placed_blocks array
                    for b in range(len(a.blocks[0])):
                        # The 3 surrounding blocks
                        x = int(a.pos_x / const.BLOCK_LEN + a.blocks[0][b])
                        y = int(a.pos_y / const.BLOCK_LEN + a.blocks[1][b])
                        # print('(%d, %d)', x, y)
                        placed_blocks[y][x] = color
                        # blocks.append(block.Block(a.pos_x + a.blocks[0][b]*block.BLOCK_LEN, a.pos_y +
                        # a.blocks[1][b]*block.BLOCK_LEN, block.Arrange_types.L))
                        # TODO update this to the correct arrange_type

                    # The center block blocks.append(block.Block(a.pos_x, a.pos_y, block.Arrange_types.L))
                    # TODO update this to the correct arrange_type
                    x = int(a.pos_x / const.BLOCK_LEN)
                    y = int(a.pos_y / const.BLOCK_LEN)
                    placed_blocks[y][x] = color

                    # delete the active arrangement
                    const.ACTIVE_ARRANGEMENTS.pop()

                    # Check to see if the player has lost
                    if placed_blocks[0].count(const.BLACK) != const.GAME_WIDTH:
                        b_game_lost = True
                    else:
                        b_game_lost = False

                    if b_game_lost:
                        current_player.add_score(int(score))
                        current_player.points_earned += int(score)
                        current_player.highest_level_check(int(game_level))
                        game_over()
                        click = False
                        return

            # Check to see if any rows can be deleted
            for i in range(len(placed_blocks) - 1, 1, -1):  # iterate backwards

                if placed_blocks[i].count(const.BLACK) == 0:
                    placed_blocks.pop(i)  # Delete the full row
                    placed_blocks.insert(0, [const.BLACK] * const.GAME_WIDTH)  # add empty space at the top
                    lines_cleared += 1
                    current_player.lines_cleared += 1
                    clear_multiplier = 1 + (lines_cleared * .3)
                    score += (100 * clear_multiplier) * tick_multiplier  # Increment Score
                    current_player.add_exp((100 * clear_multiplier) * tick_multiplier)
                    current_player.add_tiles(int(((100 * clear_multiplier) * tick_multiplier) / 10))

            const.WINDOW.fill((0, 0, 0))
            const.WINDOW.blit(const.GAME_SCREEN, (0, 0))  # game background
            # Draw all placed blocks
            for i in range(len(placed_blocks)):
                for j in range(len(placed_blocks[0])):

                    # if b is not empty
                    color = placed_blocks[i][j]

                    # Paint a black block first for a border
                    # temp_surf = pygame.Surface((BLOCK_LEN, BLOCK_LEN))
                    # temp_surf.fill((0, 0, 0))
                    if color != const.BLACK:
                        temp_surf = pygame.Surface((const.BLOCK_LEN - 1, const.BLOCK_LEN - 1))
                        temp_surf.fill(color)
                        const.WINDOW.blit(temp_surf, (j * const.BLOCK_LEN, i * const.BLOCK_LEN))

            # speed increases every 20 seconds
            # for a in const.ACTIVE_ARRANGEMENTS:
            #   if timer < 20:
            #       a.pos_y += 0.05 * const.BLOCK_LEN
            #   if timer < 40:
            #       a.pos_y += 0.15 * const.BLOCK_LEN

            # Draw all active blocks
            for a in const.ACTIVE_ARRANGEMENTS:
                a.paint(const.WINDOW)

            # Display Player information
            player_tiles = const.sudo_medium_font.render(str(current_player.tiles), True, const.RED)
            player_levels = const.sudo_medium_font.render(str(current_player.level), True, const.GREEN)
            player_name = const.medium_font.render(str(current_player.name), True, const.LIGHT_GREY)

            const.WINDOW.blit(player_tiles, (702, 70))
            const.WINDOW.blit(player_levels, (555, 70))
            const.WINDOW.blit(player_name, (520, 15))

            percentage = current_player.exp / const.level_up(current_player.level)
            update_box = pygame.Rect(509, 53, 300 * percentage, 2)
            pygame.draw.rect(const.WINDOW, const.GREEN, update_box, 0)

            pygame.display.flip()

            # Display next arrangement to drop
            temp_block = block.Arrangement(next_block.arrange_type, 600, 315)
            temp_block.paint(const.WINDOW)

            # Display Score
            score_surface = const.medium_font.render(str(int(score)), 1, (255, 255, 255))
            # score_rec = score_surface.get_rect()
            const.WINDOW.blit(score_surface, (650, 144))

            # Game Level display
            game_level_display = const.sudo_medium_font.render("LEVEL " + str(game_level), True, const.YELLOW)
            const.WINDOW.blit(game_level_display, (520, 530))

            # Game speed display
            game_level_display = const.sudo_small_font.render("GAME SPEED: " + str(tick), True, const.BLUE)
            const.WINDOW.blit(game_level_display, (520, 750))

            # Game mult_display
            game_level_display = const.sudo_small_font.render("ROW CLEAR MULTIPLIER: " + str(1 + (lines_cleared * .3)),
                                                              True, const.BLUE)
            const.WINDOW.blit(game_level_display, (520, 780))

            # Game mult_display
            game_level_display = const.sudo_small_font.render("TICK MULTIPLIER: " + str(tick_multiplier),
                                                              True, const.BLUE)
            const.WINDOW.blit(game_level_display, (520, 810))

            # Game mult_display
            game_level_display = const.sudo_small_font.render("POWER-UP MULTIPLIER: " + str(p3_multiplier),
                                                              True, const.BLUE)
            const.WINDOW.blit(game_level_display, (520, 840))

            # Power-ups Display ---------------------------------------------------------------------------------------
            if (pow_timer - p1_last_used) < const.pow_time_to_refresh[
                current_player.pow_instant_clear_level] and current_player.pow_instant_clear_level:
                percentage = (pow_timer - p1_last_used) / const.pow_time_to_refresh[
                    current_player.pow_instant_clear_level]
                p1_cool_down = pygame.Rect(527, 667, 66, 66 * percentage)
                pygame.draw.rect(const.WINDOW, const.RED, p1_cool_down, 0)
            elif current_player.pow_instant_clear_level:
                p1_ready = pygame.Rect(525, 665, 70, 70)
                pygame.draw.rect(const.WINDOW, const.RED, p1_ready, 0)

            if (pow_timer - p2_last_used) < const.pow_slow_refresh and current_player.pow_slow_time_level:
                percentage = (pow_timer - p2_last_used) / const.pow_slow_refresh
                p2_cool_down = pygame.Rect(627, 667, 66, 66 * percentage)
                pygame.draw.rect(const.WINDOW, const.BLUE, p2_cool_down, 0)
            elif current_player.pow_slow_time_level:
                p2_cool_down = pygame.Rect(625, 665, 70, 70)
                pygame.draw.rect(const.WINDOW, const.BLUE, p2_cool_down, 0)

            if (pow_timer - p3_last_used) < const.pow_mult_refresh and current_player.pow_score_mult_level:
                percentage = (pow_timer - p3_last_used) / const.pow_mult_refresh
                p3_cool_down = pygame.Rect(727, 667, 66, 66 * percentage)
                pygame.draw.rect(const.WINDOW, const.YELLOW, p3_cool_down, 0)
            elif current_player.pow_score_mult_level:
                p3_cool_down = pygame.Rect(725, 665, 70, 70)
                pygame.draw.rect(const.WINDOW, const.YELLOW, p3_cool_down, 0)

            if current_player.pow_instant_clear_level:
                pow_row_clear = pygame.transform.scale(const.POWER_ROW_CLEAR,
                                                       (const.POWERUP_ICON_WIDTH_SMALL, const.POWERUP_ICON_WIDTH_SMALL))
                const.WINDOW.blit(pow_row_clear, (530, 670))

            if current_player.pow_slow_time_level:
                pow_slow_time = pygame.transform.scale(const.POWER_SLOW_TIME,
                                                       (const.POWERUP_ICON_WIDTH_SMALL, const.POWERUP_ICON_WIDTH_SMALL))
                const.WINDOW.blit(pow_slow_time, (630, 670))

            if current_player.pow_slow_time_level:
                pow_score = pygame.transform.scale(const.POWER_SCORE_MULT,
                                                   (const.POWERUP_ICON_WIDTH_SMALL, const.POWERUP_ICON_WIDTH_SMALL))
                const.WINDOW.blit(pow_score, (730, 670))

            if score_mult_on:
                score_mult_display = const.large_font.render(
                    "x: " + str(const.pow_mult_factor[current_player.pow_score_mult_level]), True, const.YELLOW)
                const.WINDOW.blit(score_mult_display, (10, 10))
            # --------------------------------------------------------------------------------------------------------
            # Power-ups incrementing timer
            pow_timer += dt

            # Decrementing Timer
            timer -= dt
            if timer <= 0:
                tick += 5
                timer = 30  # timer will reset when game ends
                game_level += 1

            # Timer display
            timer_back = const.medium_font.render(str(round(timer, 2)), True, (255, 255, 255))
            const.WINDOW.blit(timer_back, (520, 600))
            pygame.display.flip()
            dt = const.CLOCK.tick(tick) / 1000  # convert to seconds

            # Update the display
            pygame.display.flip()

        else:
            # Display a pause screen
            response = pause()
            if response == "main_menu":
                return
            paused = False
            pygame.display.flip()

            if [1 for e in events if e.type == pygame.QUIT]:
                save()
                running = False
                sys.exit()


# Shows the game over screen
def game_over():
    pygame.display.flip()

    click = False
    waiting = True
    while waiting:
        # sets the game_over background
        const.WINDOW.blit(const.GAME_OVER_SCREEN, (0, 0))

        # get the mouse cursor position
        x, y = pygame.mouse.get_pos()

        # creates the buttons
        restart_button = pygame.Rect(130, 441, 530, 64)  # Restart
        exit_button = pygame.Rect(203, 526, 387, 64)  # Exit

        # if click on play button, then starts the game
        if restart_button.collidepoint((x, y)):
            if click:
                score = 0
                timer = 60  # Count Down Timer
                dt = 0
                # active_arrangements = []
                game()

        # if exit button is pressed, then exits the game
        if exit_button.collidepoint((x, y)):
            if click:
                return "main_menu"
        # draws the buttons
        pygame.draw.rect(const.WINDOW, const.BLACK, restart_button, 1)
        pygame.draw.rect(const.WINDOW, const.BLACK, exit_button, 1)

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


def pause():
    pygame.display.flip()

    click = False
    waiting = True
    while waiting:
        # sets the game_over background
        const.WINDOW.blit(const.PAUSE_SCREEN, (0, 0))

        # get the mouse cursor position
        x, y = pygame.mouse.get_pos()

        # creates the buttons
        resume_button = pygame.Rect(130, 441, 530, 64)  # Restart
        exit_button = pygame.Rect(203, 526, 387, 64)  # Exit

        # if click on play button, then starts the game
        if resume_button.collidepoint((x, y)):
            if click:
                return

        # if exit button is pressed, then exits the game
        if exit_button.collidepoint((x, y)):
            if click:
                return "main_menu"
        # draws the buttons
        pygame.draw.rect(const.WINDOW, const.BLACK, resume_button, 1)
        pygame.draw.rect(const.WINDOW, const.BLACK, exit_button, 1)

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
