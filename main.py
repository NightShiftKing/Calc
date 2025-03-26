import pygame
from cartesian import CartesianPlane
from plane import CoordinatePlane
from constants import DEFAULT_SCREEN_SIZE, FPS, Colors

pygame.init()

screen: pygame.Surface = pygame.display.set_mode(DEFAULT_SCREEN_SIZE, pygame.RESIZABLE)
pygame.display.set_caption('Calculus demonstration')

is_closing: bool = False
clock: pygame.time.Clock = pygame.time.Clock()

coord_plane: CoordinatePlane = CartesianPlane()

while not is_closing:
    ticks: int = clock.get_time()
    clock.tick(FPS)
    gameEvents: list[pygame.event.Event] = pygame.event.get()

    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            is_closing = True

        if event.type == pygame.MOUSEWHEEL:
            coord_plane.increments += event.y

    # Keyboard Input ----------------------------------------------------------

    # Logic & Updates ---------------------------------------------------------
    coord_plane.update()

    # Render Section -----------------------------------------------------------
    screen.fill(Colors.MEDIUM_GRAY)
    coord_plane.draw(screen)
    pygame.display.flip() # Updates graphics each game loop.

    # Application Terminated --------------------------------------------------
else:
    pygame.quit()