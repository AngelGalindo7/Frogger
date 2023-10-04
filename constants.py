from enum import Enum, auto
import pygame

SQUARE_SIZE = 40
GAME_SQUARE_WIDTH = 16
GAME_SQUARE_HEIGHT = 20
WIDTH = 600
HEIGHT = 800

WATER_COLOR = (0, 0, 100)  # Water color
WATER_X = 0
WATER_Y = 0
WATER_WIDTH = WIDTH
WATER_HEIGHT = HEIGHT - SQUARE_SIZE * 10

LEFT, RIGHT = False, True

# Just gotta find the bounds rq
WATER_ZONE_X = 0
WATER_ZONE_Y = (40, 320)

FPS = 60

DEBUG_TOGGLE = False
"""
Quick explination for the Enum class.

Enum classes are basically easily adjustable lists that use objects to hold a value that is easily added
to and taken away as it auto iterates on runtime. Think of it like a dictionary that requires less work but
can't hold any serious values.

In most causes, such as this, its used to add clarification onto code and avoid magic numbers. It can be used
in dictionaries to help readability for keys. 
- Moth
"""


class LOG_SKINS(Enum):
    BASIC = auto()


class VECHILE_SKINS(Enum):
    BASIC_1 = auto()
    BASIC_2 = auto()
    TRACTOR = auto()
    SPACESHIP = auto()
    WHITE = auto()
    PINK = auto()


# Sprite dictionaries
LOG_SKIN_SPRITES = {
    LOG_SKINS.BASIC: pygame.image.load("Log/Log_sample.png"),
}

VECHILE_SKIN_SPRITES = {
    VECHILE_SKINS.BASIC_1: pygame.image.load("Vehicle_skin/Car_basic.png"),
    VECHILE_SKINS.BASIC_2: pygame.image.load("Vehicle_skin/Car_2.png"),
    VECHILE_SKINS.TRACTOR: pygame.image.load("Vehicle_skin/Tractor_main.png"),
    VECHILE_SKINS.SPACESHIP:
    pygame.image.load("Vehicle_skin/Spaceship_blue.png"),
    VECHILE_SKINS.WHITE: pygame.image.load("Vehicle_skin/Car_3white.png"),
    VECHILE_SKINS.PINK: pygame.image.load("Vehicle_skin/Car_pin1.png"),
}

END_GRASS_SKIN_SPRITE = pygame.image.load("Grass/EndGrass_Sample2.png")
