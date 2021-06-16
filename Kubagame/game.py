import pygame
from .board import Board
from .player import Player
import copy

class KubaGame:
    """
    KubaGame object that moderates the game with the given rules and requirements,
    meaning it will determine whose turn it is, if a move is valid, if a player has won.
    It will also return states of the game such as number of marbles captured by the players,
    marble counts of each color on the board, and checking what is in a particular location.
    It will need to interact with the Board class to identify conditions of the board and
    to check if the player's move is legal. The KubaGame class will also initiates the Player
    class and creates two Player objects to store each player's information.
    """
    def __init__(self, player1, player2):
        """
        Initializing the game with players, turn and game state.
        It takes player1 and player2 parameters and use them to create Player objects.
        It initializes the current turn as None and winner as none.
        """
        self._players = [Player(player1), Player(player2)]
        self._current_turn = None
        self._winner = None
        self._game_board = Board()

    def get_current_turn(self):
        """
        Returns the player name whose turn it is to play the game.
        Returns None if no player has made the first move.
        """
        if self._current_turn == None:
            return None
        else:
            return self._current_turn.get_name()

    def set_current_turn(self, player):
        """Takes a player parameter and set the player whose turn it is to play the game"""
        self._current_turn = player

    def make_move(self, playername, coordinates, direction):
        """
        Takes playername, coordinates and direction for the player to make a move.
        It checks if a move is valid, make the move if it is valid.
        The method returns True if the move is valid, False if invalid.
        """

        # Get player object and color
        playercolor = None
        current_player = None
        for player in self._players:
            if player.get_name() == playername:
                current_player = player
                playercolor = player.get_color()

        # check if it is player's turn
        current_turn = self.get_current_turn()
        if self.get_current_turn() is not None:
            if current_turn != playername:
                return False

        # check if the coordinates given contains player's marble
        if playercolor != self._game_board.get_board_item(coordinates):
            return False

        # check if the game has been won
        if self._winner is not None:
            return False

        # check valid direction entry
        direction_check = ["L", "R", "F", "B"]
        if direction not in direction_check:
            return False

        # check if coordinates provided is within range of 0-6
        row, column = coordinates
        if row not in range(7):
            return False
        if column not in range(7):
            return False

        # create a board
        current_board = copy.deepcopy(self._game_board.get_board())

        # saves board into previous state of board
        self._game_board.set_before_previous(copy.deepcopy(self._game_board.get_previous()))
        self._game_board.set_previous(copy.deepcopy(current_board))

        # Making a move for direction "L"
        if direction == "L":
            # validate direction "L"
            if column + 1 <= 6:
                if current_board[row][column + 1] != "X":
                    return False
            column_ct = column
            while column_ct > 0:
                if current_board[row][column_ct - 1] != "X":
                    column_ct -= 1
                else:
                    difference = column - column_ct
                    current = column_ct
                    while difference >= 0:
                        current_board[row][current - 1] = current_board[row][current]
                        difference -= 1
                        current += 1
                    current_board[row][column] = "X"
                    break
            if column_ct == 0:
                column_ct2 = column
                current2 = 0
                if current_board[row][0] == playercolor:
                    return False
                elif current_board[row][0] == "R":
                    current_player.set_red_marbles()
                    while column_ct2 > 0:
                        current_board[row][current2] = current_board[row][current2 + 1]
                        column_ct2 -= 1
                        current2 += 1
                    current_board[row][column] = "X"
                else:
                    while column_ct2 > 0:
                        current_board[row][current2] = current_board[row][current2 + 1]
                        column_ct2 -= 1
                        current2 += 1
                    current_board[row][column] = "X"

            # check if move undo a move that opponent just made by checking if the
            # move is the same as previous board state
            if current_board == self._game_board.get_before_previous():
                return False
            else:
                for player in self._players:
                    if player.get_name() != playername:
                        self.set_current_turn(player)
                self._game_board.set_board(current_board)

        # Making a move for direction "R"
        if direction == "R":
            # validate direction "R"
            if column - 1 >= 0:
                if current_board[row][column - 1] != "X":
                    return False
            column_ct = column
            while column_ct < 6:
                if current_board[row][column_ct + 1] != "X":
                    column_ct += 1
                else:
                    difference = column_ct - column
                    current = column_ct
                    while difference >= 0:
                        current_board[row][current + 1] = current_board[row][current]
                        difference -= 1
                        current -= 1
                    current_board[row][column] = "X"
                    break
            if column_ct == 6:
                column_ct2 = column
                current2 = 6
                if current_board[row][6] == playercolor:
                    return False
                elif current_board[row][6] == "R":
                    current_player.set_red_marbles()
                    while column_ct2 < 6:
                        current_board[row][current2] = current_board[row][current2 - 1]
                        column_ct2 += 1
                        current2 -= 1
                    current_board[row][column] = "X"
                else:
                    while column_ct2 < 6:
                        current_board[row][current2] = current_board[row][current2 - 1]
                        column_ct2 += 1
                        current2 -= 1
                    current_board[row][column] = "X"

            # check if move undo a move that opponent just made by checking if the
            # move is the same as previous board state
            if current_board == self._game_board.get_before_previous():
                return False
            else:
                for player in self._players:
                    if player.get_name() != playername:
                        self.set_current_turn(player)
                self._game_board.set_board(current_board)

        # Making a move for direction "F"
        if direction == "F":
            # validate direction "F"
            if row + 1 <= 6:
                if current_board[row + 1][column] != "X":
                    return False
            row_ct = row
            while row_ct > 0:
                if current_board[row_ct - 1][column] != "X":
                    row_ct -= 1
                else:
                    difference = row - row_ct
                    current = row_ct
                    while difference >= 0:
                        current_board[current - 1][column] = current_board[current][column]
                        difference -= 1
                        current += 1
                    current_board[row][column] = "X"
                    break
            if row_ct == 0:
                row_ct2 = row
                current2 = 0
                if current_board[0][column] == playercolor:
                    return False
                elif current_board[0][column] == "R":
                    current_player.set_red_marbles()
                    while row_ct2 > 0:
                        current_board[current2][column] = current_board[current2 + 1][column]
                        row_ct2 -= 1
                        current2 += 1
                    current_board[row][column] = "X"
                else:
                    while row_ct2 > 0:
                        current_board[current2][column] = current_board[current2 + 1][column]
                        row_ct2 -= 1
                        current2 += 1
                    current_board[row][column] = "X"

            # check if move undo a move that opponent just made by checking if the
            # move is the same as previous board state
            if current_board == self._game_board.get_before_previous():
                return False
            else:
                for player in self._players:
                    if player.get_name() != playername:
                        self.set_current_turn(player)
                self._game_board.set_board(current_board)

        # Making a move for direction "B"
        if direction == "B":
            # validate direction "B"
            if row - 1 >= 0:
                if current_board[row - 1][column] != "X":
                    return False
            row_ct = row
            while row_ct < 6:
                if current_board[row_ct + 1][column] != "X":
                    row_ct += 1
                else:
                    difference = row_ct - row
                    current = row_ct
                    while difference >= 0:
                        current_board[current + 1][column] = current_board[current][column]
                        difference -= 1
                        current -= 1
                    current_board[row][column] = "X"
                    break
            if row_ct == 6:
                row_ct2 = row
                current2 = 6
                if current_board[6][column] == playercolor:
                    return False
                elif current_board[6][column] == "R":
                    current_player.set_red_marbles()
                    while row_ct2 < 6:
                        current_board[current2][column] = current_board[current2 - 1][column]
                        row_ct2 += 1
                        current2 -= 1
                    current_board[row][column] = "X"
                else:
                    while row_ct2 < 6:
                        current_board[current2][column] = current_board[current2 - 1][column]
                        row_ct2 += 1
                        current2 -= 1
                    current_board[row][column] = "X"

            # check if move undo a move that opponent just made by checking if the
            # move is the same as previous board state
            if current_board == self._game_board.get_before_previous():
                return False
            else:
                for player in self._players:
                    if player.get_name() != playername:
                        self.set_current_turn(player)
                self._game_board.set_board(current_board)


        # Check for winner with 7 red marbles after move
        for player in self._players:
            if player.get_red_marbles() == 7:
                self.set_winner(player)

        # Check for winner with opposing player with 0 marbles
        white, black, red = self.get_marble_count()
        if white == 0:
            for player in self._players:
                if player.get_color() == "B":
                    self.set_winner(player)
        if black == 0:
            for player in self._players:
                if player.get_color() == "W":
                    self.set_winner(player)
        return True

    def get_winner(self):
        """
        Returns the name of the winning player.
        If no player has won yet, it returns None.
        """
        if self._winner == None:
            return None
        else:
            return self._winner.get_name()

    def set_winner(self, player):
        """Takes a player parameter and set the player if it satisfied winning conditions"""
        self._winner = player

    def get_captured(self, playername):
        """
        Takes player's name and return number of red marble captured.
        It will communicate with the Player class object to obtain this information.
        """
        for player in self._players:
            if player.get_name() == playername:
                return player.get_red_marbles()

    def get_marble(self, coordinates):
        """
        Takes coordinates and returns marble present in the location (W, B or R).
        If no marble is present, returns 'X'.
        It will check the board condition in Board class to get this information.
        """
        return self._game_board.get_board_item(coordinates)

    def get_marble_count(self):
        """
        Returns marble counts in order of (White, Black, Red).
        It will check the board condition in Board class to get this information.
        """
        wcount = 0
        bcount = 0
        rcount = 0
        for rows in self._game_board.get_board():
            for columns in rows:
                if columns == "W":
                    wcount += 1
                elif columns == "B":
                    bcount += 1
                elif columns == "R":
                    rcount += 1

        return (wcount, bcount, rcount)