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
WIDTH = 360
HEIGHT = 480
FPS = 30

#defining colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

#NOW THE INITIALIZING SECTION
pygame.init()
pygame.mixer.init()

#defining the screen for gameplay
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
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

