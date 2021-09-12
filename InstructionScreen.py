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

#create the players car
instructionCar = pygame.image.load("carbackPlayerInstruction.PNG")

running = True
try:
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #mouse position
        mouse = pygame.mouse.get_pos()

        #draw "play" button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 331 <= mouse[0] <= 331+140 and 390 <= mouse[1] <= 390+40:
                import Main
                    
        if 331 <= mouse[0] <= 331+140 and 380 <= mouse[1] <= 380+40:
            pygame.draw.rect(screen,color_light,[331,390,140,40])             
        else:
            pygame.draw.rect(screen,color_dark,[331,390,140,40])
        screen.blit(playText , (370,392))

        #instruction text
        font = pygame.font.Font('freesansbold.ttf', 24)
        smallfont = pygame.font.Font('freesansbold.ttf', 13)
        instructionArea = pygame.Rect(100, 25, 600, 350)
        pygame.draw.rect(screen, (0, 0, 0), instructionArea)
        instructionSurface = font.render("How to play:", True, (255, 255, 255))
        screen.blit(instructionSurface, (instructionArea.x + 18, instructionArea.y + 25))
        
        playerExplainedSurface = smallfont.render("You the player control the red car pictured below, by typing both quickly and accurately.", True, (255, 255, 255))
        screen.blit(playerExplainedSurface, (120, 100))

        howToWinSurface = smallfont.render("To win, ensure you type quickly and accurately in order to beat the enemy car to the finish.", True, (255, 255, 255))
        screen.blit(howToWinSurface, (120, 180))

        screen.blit(instructionCar, (125, 115))

        pygame.display.update()

    pygame.quit()
except SystemExit:
    pygame.quit()
