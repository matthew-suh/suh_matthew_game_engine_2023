# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 1024
HEIGHT = 768
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# List of platform tuples (includes x, y, width, height, etc.)
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "normal"),
                 (500, 250, 100, 20, "normal"),
                 (750, 200, 50, 20, "normal")]

JUMPPLATFORM_LIST = [(512, 384, 100, 30, "normal")]

# List of the moving enemy mobs
MOB_LIST = [(700, 500, 25, 25, "moving vertically"),
            (300, 400, 25, 25, "moving vertically"),
            (100, 300, 25, 25, "moving vertically"),
            (800, 600, 25, 25, "moving vertically"),
            (800, 200, 25, 25, "moving horizontally"),
            (500, 400, 25, 25, "moving horizontally"),
            (300, 600, 25, 25, "moving horizontally"),
            (100, 800, 25, 25, "moving horizontally")]

# List of coins
COIN_LIST = [(750, 150, 50, 20, "moving"),
             (150, 370, 50, 20, "moving"),
             (500, 655, 50, 20, "moving"),
             (100, 655, 50, 20, "moving"),
             (520, 200, 100, 20, "moving")]

