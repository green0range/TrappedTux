# Setup pygame
import pygame, sys, Globals
from os.path import join

from pygame.locals import *
pygame.init()
# Give values here
screenwidth = 1000
screenheight = 600
playerMoveSpeed = 0.85
levelnum = 3
screen = pygame.display.set_mode((screenwidth, screenheight),0,32)
playerX = 32
playerY = 32
wires = 0
keydelay = 0 # Delay between registering key presses, stops it from sensing 1 long press as 2 presses
# No, KEYUP event doesn't work, unless it coisides exactly with a frame draw, which is unlikely
# Movement key overide the delay system

def get_asset_name(atom):
    return join("assets", atom)

Globals.get_asset_name = get_asset_name
