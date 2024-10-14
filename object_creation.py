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
            self.speed += self.g / 60
        else:
            self.speed = maxFallSpeed
            self.position[1] += self.speed

            # Check for collisions with groundrects
        for groundrect in groundrects:
            if self.rect.colliderect(groundrect):
                self.position[1] = groundrect.top - self.size[1]  # Use groundrect.top
                self.speed = 0

    # Update the rect based on the new position
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

        self.position[1] += self.speed

class stationaryBlock:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)