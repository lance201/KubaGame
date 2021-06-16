import pygame

WIDTH, HEIGHT = 700, 900
ROWS, COLS = 7, 7
SQUARE_SIZE = WIDTH//COLS
WIN_WIDTH, WIN_HEIGHT = WIDTH + 200, HEIGHT + 200
LINE_WIDTH = 2

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)

RED_P = pygame.image.load('red.png').convert_alpha()
WHITE_P = pygame.image.load('white.png').convert_alpha()
BLACK_P = pygame.image.load('black.png').convert_alpha()