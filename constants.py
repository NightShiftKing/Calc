from enum import Enum

MIN_INCREMENT: int = 6
MAX_INCREMENT: int = 90
DEFAULT_SCREEN_SIZE: tuple[int, int] = (700, 700)
FPS: int = 60


class Colors(tuple[int, int, int], Enum):
    BLACK = (0, 0, 0)
    MEDIUM_GRAY = (150, 150, 150)
