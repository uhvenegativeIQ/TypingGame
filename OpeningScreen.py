#imports
import pygame
from pygame.locals import *
import sys
import time
import random

#initialise pygame
pygame.init()

#define font
font = pygame.font.SysFont('Corbel',35)
smallfont = pygame.font.SysFont('Corbel', 28)

#create screen, title and icon
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Typing game")
icon = pygame.image.load('placeholderIcon.PNG')
pygame.display.set_icon(icon)
screen.fill((135, 206, 235))

#colours for buttons
color_light = (170,170,170)
color_dark = (100,100,100)

#rendering text for the screen
playText = font.render('Play' , True , (255,255,255))
instructionText = smallfont.render('Instructions' , True , (255,255,255))

running = True
try: 
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Main game text
        font = pygame.font.Font('freesansbold.ttf', 32)
        userSelectArea = pygame.Rect(275, 50, 250, 350)
        pygame.draw.rect(screen, (0, 0, 0), userSelectArea)
        userSelectSurface = font.render("TypingGame", True, (255, 255, 255))
        screen.blit(userSelectSurface, (userSelectArea.x + 25, userSelectArea.y + 25))

        #mouse position
        mouse = pygame.mouse.get_pos()

        #draw "play" button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 331 <= mouse[0] <= 331+140 and 150 <= mouse[1] <= 150+40:
                import Main
                    
        if 331 <= mouse[0] <= 331+140 and 150 <= mouse[1] <= 150+40:
            pygame.draw.rect(screen,color_light,[331,150,140,40])             
        else:
            pygame.draw.rect(screen,color_dark,[331,150,140,40])
        screen.blit(playText , (374,152))

        #draw "instructions" button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 331 <= mouse[0] <= 331+140 and 210 <= mouse[1] <= 210+40:
                import InstructionScreen
                    
        if 331 <= mouse[0] <= 331+140 and 210 <= mouse[1] <= 210+40:
            pygame.draw.rect(screen,color_light,[331,210,140,40])             
        else:
            pygame.draw.rect(screen,color_dark,[331,210,140,40])
        screen.blit(instructionText , (337,218))

        pygame.display.update()

    pygame.quit()
except SystemExit:
    pygame.quit()
    
            
