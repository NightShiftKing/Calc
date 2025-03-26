import pygame
from plane import CoordinatePlane
from constants import Colors


class CartesianPlane(CoordinatePlane):
    def __init__(self ):
        super().__init__()

    def draw(self, screen):
        super().draw(screen)
        x_spacing = self.screen_rect.width / self.increments
        y_spacing = self.screen_rect.height / self.increments
        x_center_offset = (self.increments / 2) * x_spacing - (self.screen_rect.width / 2)
        y_center_offset = (self.increments / 2) * y_spacing - (self.screen_rect.height / 2)

        for i in range(self.increments):
            x_pos = (i * x_spacing) - x_center_offset
            y_pos = (i * y_spacing) - y_center_offset

            pygame.draw.line(screen,
                             Colors.BLACK,
                             (x_pos, self.screen_rect.centery + 5),
                             (x_pos, self.screen_rect.centery - 5))

            pygame.draw.line(screen,
                             Colors.BLACK,
                             (self.screen_rect.centerx + 5, y_pos),
                             (self.screen_rect.centerx - 5, y_pos))

    def update(self):
        super().update()