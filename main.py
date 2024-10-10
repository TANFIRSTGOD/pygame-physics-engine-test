import pygame
import button

pygame.init()

BACKGROUND_COLOR = (0,0,0)
PRIMARY_COLOR = (255,255,255)

DEFAULT_FONT = pygame.font.Font(None, 36)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame physics playground test")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BACKGROUND_COLOR)



    pygame.display.flip()

pygame.quit()