"""
Tic-tac-toe
"""

import numpy as np


class TicTacToe:
    def __init__(self, player1, player2, gridsize=3):
        self.player1 = player1
        self.player2 = player2

        self.gridsize = gridsize
        self.grid = np.full((gridsize, gridsize), " ")

        # start game
        self.currentplayer = True  # boolean to flip between players
        while self.checkstate():
            # get player one's turn
            self.getturn()

            if not self.checkstate():
                break

            # get player two's turn
            self.getturn()

        self.showwinner()

    def drawgrid(self):
        """
        Draw the current state of the grid.
        """

        print("")
        for i, row in enumerate(self.grid):
            rowstr = "|".join([f" {x} " for x in row])
            print(rowstr)
            if i < self.gridsize - 1:
                print("-" * (self.gridsize * 3 + (self.gridsize - 1)))
        print("")

    def getturn(self):
        """
        Ask player for input coordinates and re-draw grid.
        """

        counters = ["x", "o"]
        players = [self.player1, self.player2]
        playeridx = int(self.currentplayer)

        coords = input(
            "{}: input the grid coordinates 'x y' for your move: ".format(players[playeridx])
        )

        x, y = [int(coord.strip()) for coord in coords.split()]

        # fill in grid
        self.grid[self.gridsize - x][self.gridsize - y] = counters[playeridx]

        # draw the grid
        self.drawgrid()

        # flip player
        self.currentplayer = not self.currentplayer

    def checkstate(self):
        """
        Check whether anyone has won.
        """

        # check if any rows are completed
        complete = False
        for row in [np.diag(self.grid), np.diag(np.fliplr(self.grid))] + [r for r in self.grid] + [r for r in np.transpose(grid)]:
            if np.all(row == row[0]):
                complete = True
                break

        return complete
