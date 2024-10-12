import pygame
import button
import object_creation
import random

pygame.init()

g = 9.807

BACKGROUND_COLOR = (0,0,0)
PRIMARY_COLOR = (255,255,255)
BUTTON_HOVER_COLOR = (225,225,225)
BUTTON_CLICK_COLOR = (180,180,180)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame physics playground test")

spawnButton = button.Button(x=725, y=25, width=50, height=50, text="Spawn", text_color=BACKGROUND_COLOR, color=PRIMARY_COLOR, hover_color=BUTTON_HOVER_COLOR, primary_color=PRIMARY_COLOR, font_size=16)
resetButton = button.Button(x=725, y=85, width=50, height=50, text="Reset", text_color=BACKGROUND_COLOR, color=PRIMARY_COLOR, hover_color=BUTTON_HOVER_COLOR, primary_color=PRIMARY_COLOR, font_size=16)

testBlock = object_creation.Block([255,255], [50,50], 1, 10, PRIMARY_COLOR, g)

blocks = []

clock = pygame.time.Clock()
fps = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if spawnButton.handle_event(event):
           newBlock = object_creation.Block([255,255], [50,50], 1, 10, (random.randint(0, 255), random.randint(0,255), random.randint(0,255)), g)
           blocks.append(newBlock)

    for currentBlock in blocks:
        if currentBlock.position[1] >= SCREEN_HEIGHT:
            blocks.pop(blocks.index(currentBlock))
        currentBlock.update()

    testBlock.update()

    screen.fill(BACKGROUND_COLOR)

    testBlock.draw(screen)

    for currentBlock in blocks:
        currentBlock.draw(screen)

    spawnButton.draw(screen)
    resetButton.draw(screen)

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()