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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)

    def update(self):
        self.rect.x+=5
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
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    
    pygame.display.flip()
    
    
pygame.quit()
sys.exit()

