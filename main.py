# This file was created by Matthew Suh 
# Content from Chris Bradfield's Kids Can Code: http://kidscancode.org/blog/
# Collaborated with my table mates to come up with certain blocks of code when problems arised or when we got stumped

# Game Design:
# Goals: avoid the red enemy mobs, avoid falling off of the platforms, try to collect all of the coins
# Rules: jump and run, do not fall off the platforms, do not get less than zero health 
# Feedback: Total score at the top of the screen, player collision animation
# Freedom: Run side to side, jump up/down

# Feature Goals:
# When the sprite collides with a coin, the total score increases and the coin disappears from the screen
# When the sprite collides with an enemy mob, the total health decreases and the sprite (Big Bell Image) gets sent to the bottom


# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math


vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# Creates a new game class to manage the game
class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # create a group for all sprites
        self.score = 10
        self.coins = 0
        # Create sprite groups for different game elements
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_jumpPlatforms = pg.sprite.Group()
        self.all_Coins = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)

        # Create and add platforms - jump platforms, mobs, and coins
        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)
        
        for j in JUMPPLATFORM_LIST:
            jump = jumpPlatform(*j)
            self.all_sprites.add(jump)
            self.all_jumpPlatforms.add(jump)

        for m in MOB_LIST:
            mobs = Mob(*m)
            self.all_sprites.add(mobs)
            self.all_mobs.add(mobs)

        for c in COIN_LIST: 
            coin = Coin(*c)
            self.all_sprites.add(coin)
            self.all_Coins.add(coin)
            
        # for m in range(0,10):
        #     m = Mob(randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 20, 20, "normal")
        #     self.all_sprites.add(m)
        #     self.all_mobs.add(m)

        self.run()
    
    def run(self):
        # Main game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Update all sprites
        self.all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y >= 0:
            phits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if phits:
                self.player.pos.y = phits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = phits[0].speed*1.5

                    
         # this prevents the player from jumping up through a platform
        elif self.player.vel.y <= 0:
            mhits = pg.sprite.spritecollide(self.player, self.all_mobs, False)
            if mhits:
                self.player.acc.y = 5
                self.player.vel.y = 0
                print("ouch")
                self.score -= 1
                
                if self.player.rect.bottom >= mhits[0].rect.top - 1:
                    self.player.rect.top = mhits[0].rect.bottom
        elif self.player.vel.y <= 0:
            jhits = pg.sprite.spritecollide(self.player, self.all_jumpPlatforms, True)
            if jhits:
                self.player.acc.y = 5
                self.player.vel.y = 0
                if self.player.rect.bottom >= mhits[0].rect.top - 1:
                    self.player.rect.top = mhits[0].rect.bottom

        # Collision handling for collecting coins
        chits = pg.sprite.spritecollide(self.player, self.all_Coins, True)
        if chits:
            print("I just got a coin!")
            self.coins += 1
        
                
            
    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites and display health and score
        self.all_sprites.draw(self.screen)
        self.draw_text("Health: " + str(self.score), 45, BLUE, WIDTH/2, HEIGHT/10)
        self.draw_text("Score: " + str(self.coins), 45, BLUE, WIDTH/2, HEIGHT/20)
        # buffer - after drawing everything, flip display
        pg.display.flip()

    # Function to draw text on the screen
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

# Instantiate the game class and run the game loop
g = Game()
while g.running:
    g.new()

# Quit Pygame when the game loop ends
pg.quit()