# Setup pygame
import pygame, sys, Globals, ObjSetter
from pygame.locals import *
pygame.init()

# Get Images
# Wall Image File
wif = "IceBrickWall.png"
wallImg = pygame.image.load(wif).convert_alpha()

def playLevel():
    ObjSetter.setobj(100,0,50,50,wallImg)
    ObjSetter.setobj(100,50,50,50,wallImg)
    ObjSetter.setobj(100,200,50,50,wallImg)
    ObjSetter.setobj(100,250,50,50,wallImg)
    ObjSetter.setobj(100,300,50,50,wallImg)
    ObjSetter.setobj(50,300,50,50,wallImg)
    ObjSetter.setobj(0,300,50,50,wallImg)
    
    ObjSetter.setobj(200,50,50,50,wallImg)
    ObjSetter.setobj(250,50,50,50,wallImg)
    ObjSetter.setobj(300,50,50,50,wallImg)
    ObjSetter.setobj(200,100,50,50,wallImg)
    ObjSetter.setobj(250,100,50,50,wallImg)
    ObjSetter.setobj(300,100,50,50,wallImg)    
    ObjSetter.setobj(250,150,50,50,wallImg)
    ObjSetter.setobj(300,150,50,50,wallImg)
    ObjSetter.setobj(350,150,50,50,wallImg) 
    
    ObjSetter.setobj(500,300,50,50,wallImg)
    ObjSetter.setobj(550,300,50,50,wallImg)
    ObjSetter.setobj(600,300,50,50,wallImg)
    ObjSetter.setobj(500,350,50,50,wallImg)
    ObjSetter.setobj(550,350,50,50,wallImg)
    ObjSetter.setobj(600,350,50,50,wallImg)    
    ObjSetter.setobj(500,400,50,50,wallImg)
    ObjSetter.setobj(550,400,50,50,wallImg)
    ObjSetter.setobj(600,400,50,50,wallImg)      