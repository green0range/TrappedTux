# Setup pygame
import pygame, sys, Globals, ObjSetter
from pygame.locals import *
pygame.init()

# Get Images
# Wall Image File
wif = Globals.get_asset_name("IceBrickWall.png")
wallImg = pygame.image.load(wif).convert_alpha()
# Spikes Image File
sif = Globals.get_asset_name("Spikes.png")
SpikesImg = pygame.image.load(sif).convert_alpha()
# Button Off/On Image Files
b0if = Globals.get_asset_name("ButtonOff.png")
b1if = Globals.get_asset_name("ButtonOn.png")
buttonOffImg = pygame.image.load(b0if).convert_alpha()
buttonOnImg = pygame.image.load(b1if).convert_alpha()
# Portal Image file
pif = Globals.get_asset_name("Portal.png")
portalImg = pygame.image.load(pif).convert_alpha()
# Wires
wlfif = Globals.get_asset_name("WireLR.png")
wireLRImg = pygame.image.load(wlfif).convert_alpha()
wudif = Globals.get_asset_name("WireUD.png")
wireUDImg = pygame.image.load(wudif).convert_alpha()
wluif = Globals.get_asset_name("WireLU.png")
wireLUImg = pygame.image.load(wluif).convert_alpha()
wdrif = Globals.get_asset_name("WireDR.png")
wireDRImg = pygame.image.load(wdrif).convert_alpha()

# door
dcif = Globals.get_asset_name("Dooryclosed.png")
doorClosedImg = pygame.image.load(dcif).convert_alpha()
doif = Globals.get_asset_name("Dooryopen.png")
doorOpenImg = pygame.image.load(doif).convert_alpha()

buttontest = False

wirex8,wirey8 = 2000,2000
wirex9,wirey9 = 2000,2000
wirex10,wirey10 = 2000,2000

nextwireid = 8

def restart():
    Globals.playerX = 32
    Globals.playerY = 32
    import Level1
    Level1.buttontest = False
    ObjSetter.resetwires()
    Level1.nextwireid = 8
    Level1.wirex8,Level1.wirey8 = 2000,2000
    Level1.wirex9,Level1.wirey9 = 2000,2000
    Level1.wirex10,Level1.wirey10 = 2000,2000
    Globals.wires = 0

def playLevel():

    # Create Walls
    ObjSetter.setobj(300,0,50,50,wallImg)
    ObjSetter.setobj(250,50,50,50,wallImg)
    ObjSetter.setobj(200,100,50,50,wallImg)
    ObjSetter.setobj(150,150,50,50,wallImg)
    ObjSetter.setobj(100,200,50,50,wallImg)

    ObjSetter.setobj(0,550,50,50,wallImg)
    ObjSetter.setobj(50,500,50,50,wallImg)
    ObjSetter.setobj(100,450,50,50,wallImg)
    ObjSetter.setobj(150,400,50,50,wallImg)
    ObjSetter.setobj(200,350,50,50,wallImg)
    ObjSetter.setobj(250,300,50,50,wallImg)
    ObjSetter.setobj(300,250,50,50,wallImg)
    ObjSetter.setobj(350,200,50,50,wallImg)
    ObjSetter.setobj(400,150,50,50,wallImg)

    ObjSetter.setobj(450,400,50,50,wallImg)
    ObjSetter.setobj(500,400,50,50,wallImg)
    ObjSetter.setobj(550,400,50,50,wallImg)
    ObjSetter.setobj(600,400,50,50,wallImg)
    ObjSetter.setobj(650,400,50,50,wallImg)
    ObjSetter.setobj(700,400,50,50,wallImg)

    ObjSetter.setobj(800,0,50,50,wallImg)
    ObjSetter.setobj(800,50,50,50,wallImg)
    ObjSetter.setobj(800,100,50,50,wallImg)
    ObjSetter.setobj(800,150,50,50,wallImg)
    ObjSetter.setobj(800,200,50,50,wallImg)
    ObjSetter.setobj(800,250,50,50,wallImg)
    ObjSetter.setobj(800,300,50,50,wallImg)


    # Set Traps
    if ObjSetter.setNonSolidObj(0,400,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(50,400,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(100,400,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(0,450,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(50,450,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(0,500,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(100,500,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(50,550,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(100,550,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(200,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(250,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(200,50,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(50,350,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(350,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(400,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(600,150,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(600,200,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(550,250,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(650,500,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(650,550,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(600,550,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(850,450,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(900,450,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(750,350,50,50,SpikesImg) == True:
        restart()

    # Portal
    if ObjSetter.setNonSolidObj(900,50,50,50,portalImg) == True:
        Globals.levelnum = 2
        restart()

    if ObjSetter.setMoveObj(400,200,400,550,75,True,SpikesImg,False):
        restart()

    # Place wires
    if Globals.wires > 0:
        if Globals.keydelay <= 0:
                if keys[K_x]:
                    if Level1.nextwireid == 8:
                        Level1.wirex8, Level1.wirey8 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    if Level1.nextwireid == 9:
                        Level1.wirex9, Level1.wirey9 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    if Level1.nextwireid == 10:
                        Level1.wirex10, Level1.wirey10 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    Level1.nextwireid = Level1.nextwireid + 1
                    Globals.keydelay = 60
