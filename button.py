import pygame

class Button:
    def __init__(self, x, y, width, height, text, text_color, color, hover_color, primary_color, font_size) -> None:   
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.hover_color = hover_color
        self.primary_color = primary_color

        self.text_surface = self.font.render(self.text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = self.hover_color
        else:
            self.color = self.primary_color
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("clicked button")
                return True