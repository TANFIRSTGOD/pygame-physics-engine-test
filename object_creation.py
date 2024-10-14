import pygame

class Block:
    def __init__(self, position, size, mass, volume, color, g):
        self.position = position
        self.size = size
        self.mass = mass
        self.volume = volume
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.color = color
        self.g = g*mass #finding the gravity for this object

        self.speed = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, groundrects):
        maxFallSpeed = 80.5556
        if self.speed < maxFallSpeed:
            self.speed += self.g/60 #speed += gravity / frame rate
        else:
            self.speed += 0

        for i in groundrects:
            if self.rect.colliderect(i):
                self.speed = 0

        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

        self.position[1] += self.speed