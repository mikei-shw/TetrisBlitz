# Group 3
# 03/04/2021
# block.py - defines the class that creates the blocks and the block arrangements

# -- willCollide(self, x_to_add, y_to_add, placed_blocks)
# -- rotate(self, placed_blocks, clockwise=False)
# -- moveLeft(self, placed_blocks)
# -- moveRight(self, placed_blocks)
# -- moveDown(self, placed_blocks)
# -- instant(self, placed_blocks)
# -- paint(self, window)

import pygame
import const
from enum import Enum
from pygame.locals import RLEACCEL
import numpy as np


# Arrangement class that acts as a container for multiple blocks
class Arrangement:

    # This struct considers only the position of a "center" block
    # other connected blocks are described in self.blocks relative to the center
    def __init__(self, arrang_type, pos_x=(const.GAME_WIDTH / 2 - 1) * const.BLOCK_LEN, pos_y=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.arrange_type = arrang_type
        self.surf = pygame.Surface((const.BLOCK_LEN - 1, const.BLOCK_LEN - 1))

        self.blocks = np.array(const.ARR_TYPES[arrang_type][0])
        self.surf.fill(const.ARR_TYPES[arrang_type][1])

    # example self.blocks:
    # [[0,-1,1],[1,0,0]]
    # these correspond to the vectors (0,1) ^ (-1,0) <- and (1,0) -> respectively
    # the example arrangement can thus be visualized as the "T" block
    #
    #                      #
    #                     ###
    #
    # note that it is implied there is a block in the "center" (0,0)

    def willCollide(self, x_to_add, y_to_add, placed_blocks):
        bWillCollide = False

        # Check outer blocks
        for b in range(len(self.blocks[0])):
            x = int(self.pos_x / const.BLOCK_LEN + x_to_add / const.BLOCK_LEN + self.blocks[0][b])
            y = int(self.pos_y / const.BLOCK_LEN + y_to_add / const.BLOCK_LEN + self.blocks[1][b])
            if x < 0 or x >= const.GAME_WIDTH or y < 0 or y >= const.GAME_HEIGHT:
                bWillCollide = True
            elif (placed_blocks[y][x] != const.BLACK):
                bWillCollide = True

        # Check center block
        x = int(self.pos_x / const.BLOCK_LEN + x_to_add / const.BLOCK_LEN)
        y = int(self.pos_y / const.BLOCK_LEN + y_to_add / const.BLOCK_LEN)
        if (x < 0 or x >= const.GAME_WIDTH or y < 0 or y >= const.GAME_HEIGHT):
            bWillCollide = True
        elif (placed_blocks[y][x] != const.BLACK):
            bWillCollide = True

        return bWillCollide

    def rotate(self, placed_blocks, clockwise=False):

        # if this is an o piece, don't continue any further
        if self.arrange_type == 'O':
            return

        # this matrix corresponds to a 90 degree rotation about the origin (center piece)
        # clockwise when true reverses the direction of the rotation
        rotationMatrix = np.array([[0, -1 * ((-1) ** clockwise)], [1 * ((-1) ** clockwise), 0]])

        # matrix multiplication
        rotatedPositions = rotationMatrix @ self.blocks
        bWillCollide = False

        # Check the 3 outer blocks
        for b in range(len(rotatedPositions)):
            x = int(self.pos_x / const.BLOCK_LEN + rotatedPositions[0][b])
            y = int(self.pos_y / const.BLOCK_LEN + rotatedPositions[1][b])
            if (x < 0 or x >= const.GAME_WIDTH or y < 0 or y >= const.GAME_HEIGHT):
                bWillCollide = True
            elif (placed_blocks[y][x] != const.BLACK):
                bWillCollide = True

        # Check the center block
        x = int(self.pos_x / const.BLOCK_LEN)
        y = int(self.pos_y / const.BLOCK_LEN)
        if (x <= 0 or x >= const.GAME_WIDTH or y <= 0 or y >= const.GAME_HEIGHT):
            bWillCollide = True
        elif (placed_blocks[y][x] != const.BLACK):
            bWillCollide = True

        # If no collisions will occur
        if not bWillCollide:
            self.blocks = rotationMatrix @ self.blocks

    def moveLeft(self, placed_blocks):
        # Check window bounds first
        if (not self.willCollide((-1 * const.BLOCK_LEN), 0, placed_blocks)):  # not colliding(perm_blocks, next_pos) and
            self.pos_x -= 1 * const.BLOCK_LEN

    def moveRight(self, placed_blocks):
        # Check window bounds first
        if (not self.willCollide(const.BLOCK_LEN, 0, placed_blocks)):  # not colliding(perm_blocks, next_pos) and
            self.pos_x += 1 * const.BLOCK_LEN

    def moveDown(self, placed_blocks):

        if (not self.willCollide(0, const.BLOCK_LEN, placed_blocks)):
            self.pos_y += 0.25 * const.BLOCK_LEN

        # if the arrangement cannot move down any further, signal to place this
        # arrangement and make a new one fall
        else:
            return False

        return True

    def instant(self, placed_blocks):
        if not self.willCollide(0, const.BLOCK_LEN, placed_blocks):
            while self.moveDown(placed_blocks):
                pass
        else:
            return False

    def paint(self, window):
        temp_surf = pygame.Surface((const.BLOCK_LEN, const.BLOCK_LEN))
        temp_surf.fill((0, 0, 0))
        # window.blit(temp_surf, (self.pos_x, self.pos_y)) # Paint black block first for a border
        window.blit(self.surf, (self.pos_x, self.pos_y))  # show center block

        for b in range(len(self.blocks[0])):
            # window.blit(temp_surf, (self.pos_x + self.blocks[0][b]*BLOCK_LEN, self.pos_y + self.blocks[1][b]*BLOCK_LEN)) # Show border block
            window.blit(self.surf, (self.pos_x + self.blocks[0][b] * const.BLOCK_LEN,
                                    self.pos_y + self.blocks[1][b] * const.BLOCK_LEN))  # show connected blocks
