# Setup pygame
import pygame, sys, Globals
from pygame.locals import *
pygame.init()
# Give values here
screenwidth = 1000
screenheight = 600
playerMoveSpeed = 0.85
levelnum = 1
screen = pygame.display.set_mode((screenwidth, screenheight),0,32)
playerX = 32
playerY = 32
wires = 0