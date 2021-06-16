import pygame

from .constants import WHITE, GREY, ROWS, COLS, LINE_WIDTH

class Board:
    """
    Board object for the game.
    The board class initializes the game board with the starting conditions.
    It will record all the moves made on the board for the KubaGame class
    to access this record to determine game states.
    It will also record the previous game board state after a move for
    comparison.
    """
    def __init__(self):
        """
        Setting up the initial state of the board using a list.
        It initializes the previous state of the board as None and
        it will update as a move is made.
        """
        self._board = [["W", "W", "X", "X", "X", "B", "B"],
                      ["W", "W", "X", "R", "X", "B", "B"],
                      ["X", "X", "R", "R", "R", "X", "X"],
                      ["X", "R", "R", "R", "R", "R", "X"],
                      ["X", "X", "R", "R", "R", "X", "X"],
                      ["B", "B", "X", "R", "X", "W", "W"],
                      ["B", "B", "X", "X", "X", "W", "W"]]
        self._before_previous = None
        self._previous = None

    def draw_grid(self, win):
        """Draw out the gameboard grid"""
        win.fill(WHITE)
        for row in range(ROWS):
            pygame.draw.line(win, GREY, (row * 100, 0), (row * 100, ROWS * 100), LINE_WIDTH)
        for col in range(COLS + 1):
            pygame.draw.line(win, GREY, (0, col * 100), (COLS * 100, col * 100), LINE_WIDTH)

    def draw_pieces(self):
        """Draw game pieces"""

        display_board = self.get_board()
        for row in display_board:
            for index, piece in enumerate(row):
                if piece == "W":
                    row[index] = white
                if piece == "R":
                    row[index] = red
                if piece == "B":
                    row[index] = black

    def get_board(self):
        """Returns the game board"""
        return self._board

    def set_board(self, board):
        """Set the game board after a move has been made"""
        self._board = board

    def get_previous(self):
        """Returns the previous state of the game board"""
        return self._previous

    def set_previous(self, board):
        """Takes a board parameter and sets the previous state of the board"""
        self._previous = board

    def get_before_previous(self):
        """Returns the previous state of the game board"""
        return self._before_previous

    def set_before_previous(self, board):
        """Takes a board parameter and sets the previous state of the board"""
        self._before_previous = board

    def get_board_item(self, coordinates):
        """Takes a coordinate paramater and return item in given location"""
        row, column = coordinates
        return self._board[row][column]