import pygame
import button

pygame.init()

BACKGROUND_COLOR = (0,0,0)
PRIMARY_COLOR = (255,255,255)
BUTTON_HOVER_COLOR = (225,225,225)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame physics playground test")

spawnButton = button.Button(x=725, y=25, width=50, height=50, text="Spawn", text_color=BACKGROUND_COLOR, color=PRIMARY_COLOR, hover_color=BUTTON_HOVER_COLOR, primary_color=PRIMARY_COLOR, font_size=16)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BACKGROUND_COLOR)

    spawnButton.draw(screen)

    pygame.display.flip()

pygame.quit()