# Setup pygame
import pygame, sys, Globals
from pygame.locals import *
pygame.init()

def checkcollisions(x,y): # Checks collisions with sides
    if x < 0:
        return 0
    if x > Globals.screenwidth - 45:
        return 1
    if y < 0:
        return 3
    if y > Globals.screenheight - 45:
        return 4

def checkMovement(): # Check keyboard input and moves the player accordingly 
    import Main
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        if not (checkcollisions(Globals.playerX, Globals.playerY) == 0) :
            Globals.playerX = Globals.playerX - Globals.playerMoveSpeed
        else:
            Globals.playerX = Globals.playerX + Globals.playerMoveSpeed
        Main.changeFaceDir("left")
    if keys[K_RIGHT]:
        if not (checkcollisions(Globals.playerX, Globals.playerY) == 1):
            Globals.playerX = Globals.playerX + Globals.playerMoveSpeed
        else:
            Globals.playerX = Globals.playerX - Globals.playerMoveSpeed   
        Main.changeFaceDir("right")        
    if keys[K_DOWN]:
        if not(checkcollisions(Globals.playerX, Globals.playerY) == 4):
            Globals.playerY = Globals.playerY + Globals.playerMoveSpeed
        else:
            Globals.playerY = Globals.playerY - Globals.playerMoveSpeed  
        Main.changeFaceDir("down")            
    if keys[K_UP]:
        if not (checkcollisions(Globals.playerX, Globals.playerY) == 3):
            Globals.playerY = Globals.playerY - Globals.playerMoveSpeed
        else:
            Globals.playerY = Globals.playerY + Globals.playerMoveSpeed  
        Main.changeFaceDir("up")    