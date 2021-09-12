#imports
import pygame
from pygame.locals import *
import sys
import time
import random

#initialise pygame
pygame.init()

#set the clock
clock = pygame.time.Clock()

#define variables
correctCounter = 0
accuracy = 0
totalCharacters = 0
currentTime = 0
wpm = 0
j = -1
playerX = 0
computerX = 0
skyCompX = -100
skyPlayerX = -100
speedfactor = 0
oldTime = 0
wpmTotal = 0
accuracyTotal = 0
increment = 0
wpmAvg = 0
accuracyAvg = 0

#define lists
sentenceLIST = []
gameLIST = []
userLIST = []
userInputLIST = []
tempLIST = []
tempLIST2 = []
tempGameLIST = []
tempUserLIST = []
wpmLIST = []
accuracyLIST = []

#create screen, title and icon
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Typing game")
icon = pygame.image.load('placeholderIcon.PNG')
pygame.display.set_icon(icon)
screen.fill((135, 206, 235))

#Create user-input area
font = pygame.font.Font('freesansbold.ttf', 16)
inputArea = pygame.Rect(0, 30, 800, 32)
userText = ""

#create computer-generated area
computerArea = pygame.Rect(0, 0, 800, 32)

#computer choosing a sentence
def choose_sentence():
    sentences = open("sentences.txt", "r")
    contents = sentences.readlines()
    sentence = random.choice(contents)
    return sentence

def make_sentence_list():
    sentenceLIST = sentence.split()
    return sentenceLIST

#breaking down the preset list into singular words for comparison
def make_game_list():
    for i in range(len(sentenceLIST)):
        tempVar = sentenceLIST[i]
        tempLIST = list(tempVar)
        tempGameLIST.append(tempLIST)
        i += 1
    GameLIST = [i for sublist in tempGameLIST for i in sublist]
    return GameLIST

sentence = choose_sentence()
sentenceLIST = make_sentence_list()
GameLIST = make_game_list()

#create the players car
playerCar = pygame.image.load("carbackPlayer.PNG")

#create the computers car
computerCar = pygame.image.load("carbackComputer.PNG")

#create the divider
divider = pygame.image.load("divider.PNG")
dividerLong = pygame.transform.scale(divider, (800, 5))

#create the sky behind player/computer
skyTracing = pygame.image.load("skyTracing.PNG")

#create box for game results
resultsRect = pygame.Rect(300, 75, 200, 300)
resultFont = pygame.font.Font('freesansbold.ttf', 32)
winTextSurface = resultFont.render("You win :)", True, (0, 255, 0))
loseTextSurface = resultFont.render("You lose :(", True, (255, 0, 0))

def input_text():
    #draws rectangle where the sentence the user has to type is displayed
    pygame.draw.rect(screen, (0, 0, 0), computerArea)
    compTextSurface = font.render(sentence, True, (255, 255, 255))
    screen.blit(compTextSurface, (computerArea.x + 5, computerArea.y + 8))
                
    #draws the rectangle text is inputted
    pygame.draw.rect(screen, (0, 0, 0), inputArea)
    textSurface = font.render(userText, True, (255, 255, 255))
    screen.blit(textSurface, (inputArea.x + 5, inputArea.y + 8))
    pygame.display.flip()
    clock.tick(60)

def place_elements():
    #place cars 
    screen.blit(playerCar, (playerX, 200))
    screen.blit(computerCar, (computerX, 395))

    #place divider
    screen.blit(dividerLong, (0, 250))
    screen.blit(dividerLong, (0, 445))

    #place skyTracing
    screen.blit(skyTracing, (skyCompX, 395))
    screen.blit(skyTracing, (skyPlayerX, 200))

#text for returning to menu
smallfont = pygame.font.SysFont('Corbel', 28)
menuText = smallfont.render('Menu' , True , (255,255,255))

#mouse position
mouse = pygame.mouse.get_pos()

def game_over():
    pygame.draw.rect(screen, (255, 255, 255), resultsRect)
    screen.blit(wpmSurface, (370, 150))
    screen.blit(accuracySurface, (340, 200))
    pygame.draw.rect(screen,(100,100,100),[331,250,140,40])             
    screen.blit(menuText , (368,260))

#game loop
running = True
try:
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #gets time for wpm calculation
            currentTime = pygame.time.get_ticks()
            if increment == 0:
                oldTime = currentTime
            increment += 1  

            #takes what the user inputs and displays it and appends to list
            try:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if userText[-1] != " ":
                            userText = userText[:-1]
                            userInputLIST.pop(j)
                            j -= 1
                        else:
                            userText = userText[:-1]
                    else:
                        j += 1
                        userText += event.unicode
                        userInputLIST.append(event.unicode)
                        if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_SPACE]:
                            userInputLIST.pop(j)
                            j -= 1
            except:
                pass

        input_text()

        #determine how much of the list is correct
        try:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    userInputLIST.pop(j)
                    j -= 1
                    for i in range(len(userInputLIST)):
                        if userInputLIST[i] == GameLIST[i]:
                            correctCounter += 1
                            if len(userInputLIST) > len(GameLIST):
                                GameLIST.append("#")
        except:
            pass

        if event.type == pygame.KEYDOWN  and len(userInputLIST) > 0:
            if event.key == pygame.K_RETURN:
                #calculate accuracy
                totalCharacters = len(GameLIST)
                accuracy = (correctCounter/totalCharacters)*100
                accuracyLIST.append(accuracy)

                #calculate time (this could be shortened using the original version ngl)
                typingTime = (currentTime - oldTime)/60000
                oldTime = currentTime
                wpm = len(sentenceLIST)/typingTime
                wpmLIST.append(wpm)

                #resetting variables for a second run
                sentenceLIST.clear()
                gameLIST.clear()
                userLIST.clear()
                userInputLIST.clear()
                tempLIST.clear()
                tempLIST2.clear()
                tempGameLIST.clear()
                tempUserLIST.clear()

                correctCounter = 0
                accuracy = 0
                totalCharacters = 0
                currentTime = 0
                wpm = 0
                permanent = 0
                j = -1
                
                userText = ""
                sentence = choose_sentence()
                sentenceLIST = make_sentence_list()
                GameLIST = make_game_list()

                #calculate total WPM
                wpmTotal = 0
                for i in range(len(wpmLIST)):
                    wpmTotal += wpmLIST[i]
                    wpmAvg = wpmTotal/len(wpmLIST)
                
                #calculate total accuracy
                accuracyTotal = 0
                for i in range(len(accuracyLIST)):
                    accuracyTotal += accuracyLIST[i]
                    accuracyAvg = accuracyTotal/len(accuracyLIST)

        #speed at which objects move
        skyPlayerX += 0.2 + speedfactor
        playerX += 0.2 + speedfactor        
        skyCompX += 0.4
        computerX += 0.4

        #make string of wpm and accuracy
        wpmString = "wpm: " + str(round(wpmAvg))
        accuracyString = "accuracy: " + str(round(accuracyAvg, 2)) + "%"

        #calculate speed factor
        speedfactor = (wpmAvg * accuracyAvg)/10000

        #create wpm and accuracy text textSurface
        wpmSurface = font.render(wpmString, (325, 150), (0, 0, 0))
        accuracySurface = font.render(accuracyString, (325, 200), (0, 0, 0))

        place_elements()

        #game outcome
        if playerX > 700:
            game_over()
            screen.blit(winTextSurface, (325, 100))
        elif computerX > 700:
            game_over()
            screen.blit(loseTextSurface, (325, 100))
            speedfactor = -0.2
            
        pygame.display.update()
        
    pygame.quit()
except SystemExit:
    pygame.quit()
