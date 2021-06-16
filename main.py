import pygame
from Kubagame.constants import WIDTH, HEIGHT
from Kubagame.game import KubaGame

pygame.init()
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kuba Game')

def main():
    run = True
    clock = pygame.time.Clock()
    game = KubaGame()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_grid(WIN)
        pygame.display.update()

    pygame.quit()

main()