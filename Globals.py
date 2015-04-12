# Setup pygame
import pygame, sys, Globals
from pygame.locals import *
pygame.init()
# Put all global variables here
global screenwidth
global screenheight
global playerMoveSpeed
global levelnum
global screen
global playerX
global playerY
# Give values here
screenwidth = 1000
screenheight = 600
playerMoveSpeed = 0.5
levelnum = 1
screen = pygame.display.set_mode((screenwidth, screenheight),0,32)
playerX = 32
playerY = 32