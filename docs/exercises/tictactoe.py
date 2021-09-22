#!/usr/bin/env python

"""
A class to create a tic-tac-toe game. The class can either be imported and run
in a Python terminal, or the script can be run from the command line.
"""

import sys
import numpy as np


class TicTacToe:
    def __init__(self):
        """
        A tic-tac-toe game. After creating the object, the game can be played
        by calling it, e.g.

        >>> game = TicTacToe()
        >>> game()
        """
        
        player1 = input("Input the name of the first player: ")
        player2 = input("Input the name of the second player: ")
        self.players = [player1, player2]

        try:
            self.gridsize = int(input("Set the grid size (integer): "))
        except ValueError:
            raise ValueError("Grid size must be an integer")

        # initialise grid as empty single space strings
        self.grid = np.full((self.gridsize, self.gridsize), " ")
        self.linecount = 3  # number of lines to rewind by

    def __call__(self):
        # start game
        self.drawgrid()

        self.currentplayer = False  # boolean to flip between players
        while not self.checkstate():
            # get player one's turn
            self.getturn()

            # check if game has been completed
            if self.checkstate():
                break

            # get player two's turn
            self.getturn()

        self.showwinner()

    play = __call__

    def drawgrid(self):
        """
        Draw the current state of the grid.
        """

        # rewind to overwrite previous grid (see, e.g., https://stackoverflow.com/a/59147732/1862861)
        for _ in range(self.linecount):
            sys.stdout.write("\x1b[1A\x1b[2K")

        print("")
        for i, row in enumerate(self.grid):
            rowstr = "|".join([f" {x} " for x in row])
            print(rowstr)
            if i < self.gridsize - 1:
                print("-" * (self.gridsize * 3 + (self.gridsize - 1)))
        print("")

        self.linecount = 2 * self.gridsize + 1

    def getturn(self):
        """
        Ask player for input coordinates and re-draw grid.
        """

        counters = ["✕", "○"]
        playeridx = int(self.currentplayer)

        # make sure coordinates are valid
        while 1:
            coords = input(
                f"{self.players[playeridx]}: Input the grid coordinates 'x y' (between 1 and {self.gridsize}) for your move: "
            )
            self.linecount += 1

            x, y = [int(coord.strip()) for coord in coords.split()]

            # check grid coordinates are valid
            if not (1 <= x <= self.gridsize) or not (1 <= y <= self.gridsize):
                print(f"x and y coordinates must be between 1 and {self.gridsize}")
                self.linecount += 1
                continue

            # check grid cooridate has not already been used
            if self.grid[self.gridsize - y][x - 1] != " ":
                print("That grid point has already be used. Try again.")
                self.linecount += 1
                continue

            break

        # fill in grid
        self.grid[self.gridsize - y][x - 1] = counters[playeridx]

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
        for row in (
            [np.diag(self.grid), np.diag(np.fliplr(self.grid))]
            + [r for r in self.grid]
            + [r for r in np.transpose(self.grid)]
        ):
            # ignore "empty" rows
            if not np.all(row == " "):
                # check if all values in row are the same
                if np.all(row == row[0]):
                    complete = True
                    break

        return complete

    def showwinner(self):
        """
        Show the winner.
        """

        playeridx = int(not self.currentplayer)
        print("The winner is {}!".format(self.players[playeridx]))


# run the game if calling the code directly
if __name__ == "__main__":
    game = TicTacToe()
    game()
