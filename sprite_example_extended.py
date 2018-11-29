# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#this is a comment
import pygame
import os
import sys
#import random

#for the window
WIDTH = 600
HEIGHT = 480
FPS = 30

#defining colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

#setting up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #changing from surface to image
        self.image = pygame.image.load(os.path.join(img_folder,"alien_jump.png")).convert()
        #making black background of sprite transparent 
        self.image.set_colorkey(BLACK)
        #self.image.fill(GREEN) ->becomes redundant
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.yspeed=5

    def update(self):
        self.rect.x+=5
        self.rect.y+=self.yspeed
        if self.rect.bottom>(HEIGHT-100):
            self.yspeed=-5
        if self.rect.top <200:
            self.yspeed=5
        if self.rect.left>WIDTH:
            self.rect.right=0

#NOW THE INITIALIZING SECTION
pygame.init()
pygame.mixer.init()

#defining the screen for gameplay
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#game loop
running=True
while running:
    clock.tick(FPS)
    #process inputs
    for event in pygame.event.get():
        #checking if close button is clicked
        if event.type==pygame.QUIT:
            running = False
    
    
    #update
    all_sprites.update()
    #draw/render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    
    
    pygame.display.flip()
    
    
pygame.quit()
sys.exit()

