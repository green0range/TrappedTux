# Setup pygame
import pygame, sys, Globals
from pygame.locals import *
pygame.init()

def setNonSolidObj(x,y,width,height,img):
    Globals.screen.blit(img, (x,y))
    if x <= Globals.playerX + 45: # Right of RW
        if x + width >= Globals.playerX: # Left of LW
            if y <= Globals.playerY + 45: # Below TW
                if y + height >= Globals.playerY: # Above BW
                    return True # Tells caller player is inside obj (i.e: spikes, finish marker)

def setobj(x,y,width,height,img): # Draws the object to the screen, and stops collisions (i.e: walls)
    Globals.screen.blit(img, (x,y))
    # Checks each boundary
    
    if x <= Globals.playerX + 45: # Right of RW
        if x + width >= Globals.playerX: # Left of LW
            if y <= Globals.playerY + 45: # Below TW
                if y + height >= Globals.playerY: # Above BW
                    # Player is inside the object
                    # Find nearest side to push player out of
                    if (x - Globals.playerX) < (Globals.playerX - x + 64):
                        Globals.playerX = Globals.playerX + Globals.playerMoveSpeed
                    else:
                        Globals.playerX = Globals.playerX - Globals.playerMoveSpeed
                    if (y - Globals.playerY) < (Globals.playerY - y + 64):
                        Globals.playerY = Globals.playerY + Globals.playerMoveSpeed
                    else:
                        Globals.playerY = Globals.playerY - Globals.playerMoveSpeed                    