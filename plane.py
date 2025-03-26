import pygame
from constants import (
    MIN_INCREMENT,
    MAX_INCREMENT,
    Colors
)


class CoordinatePlane:
    def __init__(self):
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.increments = 10

    def draw(self, screen):
        pygame.draw.line(screen, Colors.BLACK, self.screen_rect.midtop, self.screen_rect.midbottom)
        pygame.draw.line(screen, Colors.BLACK, self.screen_rect.midleft, self.screen_rect.midright)

        self.increments = int(pygame.math.clamp(self.increments, MIN_INCREMENT, MAX_INCREMENT))


    def update(self):
        self.screen_rect.size = pygame.display.get_surface().get_size()
        self.increments = self.increments