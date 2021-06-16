import pygame

class Player:
    """
    Player object for the game.
    The player class is initiated by the KubaGame class.
    It will store player information such as name, color given by the KubaGame class operations.
    It will also store the red marbles count of each player, which will help determine a winner.
    """
    def __init__(self, player):
        """
        Initializing player data using given player data from KubaGame class and
        starting captured red marbles count of 0.
        """
        self._name, self._color = player
        self._red_marbles = 0

    def get_name(self):
        """Return player's name"""
        return self._name

    def get_color(self):
        """Return player's color"""
        return self._color

    def get_red_marbles(self):
        """Return captured red marble count"""
        return self._red_marbles

    def set_red_marbles(self):
        """Increment number of red marbles captured"""
        self._red_marbles += 1