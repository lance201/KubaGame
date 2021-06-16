import pygame

class Piece:
    """Loads images of the game pieces"""
    def __init__(self):
        self._red = pygame.image.load('red.png').convert_alpha()
        self._white = pygame.image.load('white.png').convert_alpha()
        self._black = pygame.image.load('black.png').convert_alpha()
        self._x = 0
        self._y = 0

    def calc_pos(self):
        """Calculate positions of the pieces"""
        self._x = SQUARE_SIZE * COLS + SQUARE_SIZE // 2