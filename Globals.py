# Setup pygame
import pygame, sys, Globals
from os.path import join

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


def get_asset_name(atom):
    return join("assets", atom)

Globals.get_asset_name = get_asset_name
