import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# Defines the player class
class Player(Sprite):
# Initialize the player sprite with an image, position, velocity, etc.
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'theBigBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.score = 0
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        # CHECKING FOR COLLISION WITH MOBS HERE>>>>>
        hits = pg.sprite.spritecollide(self, self.game.all_mobs, False)
        if hits:
            print ("i hit a mob")
            # player.hitpoints -= 10
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
       

# Defines the platforms class
class Platform(Sprite):
# Initialize platform attributes like position, movement, etc.
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
# Update platform position - allows for movement
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed

# Defines the jumpPlatform class
class jumpPlatform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
     
# Defines the enemy mob class
class Mob(Sprite):
# Initialize the enemy mob attributes like the image, position, etc.
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'enemy.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving vertically" or "moving horizontally":
            self.speed = 8
# Update the mob position - allowing for movement
    def update(self):
        if self.category == "moving horizontally":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
        if self.category == "moving vertically":
            self.rect.y += self.speed
            if self.rect.y + self.rect.h > HEIGHT or self.rect.y < 0:
                self.speed = -self.speed

# Defines the coin class
class Coin(Sprite):
# Initialize the coin attributes like the image, position, etc.
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'coin.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect.center)
        self.category = category
        self.speed = 5  
        if self.category == "moving":
                self.rect.y += self.speed
                if self.rect.y > HEIGHT/2 or self.rect.y < 0:
                    self.speed = -self.speed
                    self.rect.y += 25

# Update the coin position and movement
    def update(self):
        pass
