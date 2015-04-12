# Setup pygame
import pygame, sys, Globals, ObjSetter
from pygame.locals import *
pygame.init()

# Get Images
# Wall Image File
wif = "IceBrickWall.png"
wallImg = pygame.image.load(wif).convert_alpha()
# Spikes Image File
sif = "Spikes.png"
SpikesImg = pygame.image.load(sif).convert_alpha()
# Button Off/On Image Files
b0if = "ButtonOff.png"
b1if = "ButtonOn.png"
buttonOffImg = pygame.image.load(b0if).convert_alpha()
buttonOnImg = pygame.image.load(b1if).convert_alpha()
# Portal Image file
pif = "Portal.png"
portalImg = pygame.image.load(pif).convert_alpha()
# Wires
wlfif = "WireLR.png"
wireLRImg = pygame.image.load(wlfif).convert_alpha()
wudif = "WireUD.png"
wireUDImg = pygame.image.load(wudif).convert_alpha()
wluif = "WireLU.png"
wireLUImg = pygame.image.load(wluif).convert_alpha()
wdrif = "WireDR.png"
wireDRImg = pygame.image.load(wdrif).convert_alpha()

# door
dcif = "Dooryclosed.png"
doorClosedImg = pygame.image.load(dcif).convert_alpha()
doif = "Dooryopen.png"
doorOpenImg = pygame.image.load(doif).convert_alpha()


buttontest = False

def restart():
    Globals.playerX = 32
    Globals.playerY = 32    
    import Level1
    Level1.buttontest = False

def playLevel():
    
    # Wires
    ObjSetter.setNonSolidObj(40,485,50,50,wireLRImg)
    ObjSetter.setNonSolidObj(90,485,50,50,wireLRImg)
    ObjSetter.setNonSolidObj(140,485,50,50,wireLUImg)
    ObjSetter.setNonSolidObj(140,435,50,50,wireUDImg)
    ObjSetter.setNonSolidObj(140,385,50,50,wireUDImg)
    ObjSetter.setNonSolidObj(140,335,50,50,wireUDImg)
    ObjSetter.setNonSolidObj(140,285,50,50,wireDRImg)
    ObjSetter.setNonSolidObj(190,285,50,50,wireLRImg)
    ObjSetter.setNonSolidObj(240,285,50,50,wireLRImg)    

    # Create Walls
    ObjSetter.setobj(100,0,50,50,wallImg)
    ObjSetter.setobj(100,50,50,50,wallImg)
    ObjSetter.setobj(100,100,50,50,wallImg)
    ObjSetter.setobj(100,150,50,50,wallImg)
    ObjSetter.setobj(100,300,50,50,wallImg)
    ObjSetter.setobj(100,350,50,50,wallImg)
    ObjSetter.setobj(100,400,50,50,wallImg)
    ObjSetter.setobj(50,400,50,50,wallImg)
    ObjSetter.setobj(0,400,50,50,wallImg)
    
    ObjSetter.setobj(250,0,50,50,wallImg)
    ObjSetter.setobj(250,50,50,50,wallImg)
    ObjSetter.setobj(250,100,50,50,wallImg)
    ObjSetter.setobj(250,150,50,50,wallImg)
    ObjSetter.setobj(250,300,50,50,wallImg)
    ObjSetter.setobj(250,350,50,50,wallImg)
    ObjSetter.setobj(250,400,50,50,wallImg)
    ObjSetter.setobj(250,450,50,50,wallImg)
    ObjSetter.setobj(250,500,50,50,wallImg)
    ObjSetter.setobj(250,550,50,50,wallImg)
    ObjSetter.setobj(200,550,50,50,wallImg)
    ObjSetter.setobj(150,550,50,50,wallImg)
    ObjSetter.setobj(100,550,50,50,wallImg)
    ObjSetter.setobj(50,550,50,50,wallImg)
    ObjSetter.setobj(0,550,50,50,wallImg)
    ObjSetter.setobj(300,0,50,50,wallImg)
    ObjSetter.setobj(300,50,50,50,wallImg)
    ObjSetter.setobj(300,100,50,50,wallImg)   
    ObjSetter.setobj(350,0,50,50,wallImg)
    ObjSetter.setobj(350,50,50,50,wallImg)    
    ObjSetter.setobj(400,0,50,50,wallImg)
    ObjSetter.setobj(400,50,50,50,wallImg) 
    ObjSetter.setobj(450,0,50,50,wallImg)
    
    ObjSetter.setobj(400,350,50,50,wallImg)
    ObjSetter.setobj(400,400,50,50,wallImg)
    ObjSetter.setobj(400,450,50,50,wallImg)
    ObjSetter.setobj(400,500,50,50,wallImg)
    
    ObjSetter.setobj(650,0,50,50,wallImg)
    ObjSetter.setobj(650,50,50,50,wallImg)
    ObjSetter.setobj(650,100,50,50,wallImg)
    ObjSetter.setobj(650,150,50,50,wallImg)
    ObjSetter.setobj(650,200,50,50,wallImg)
    ObjSetter.setobj(650,250,50,50,wallImg)
    ObjSetter.setobj(650,300,50,50,wallImg)
    ObjSetter.setobj(650,350,50,50,wallImg)
    ObjSetter.setobj(650,400,50,50,wallImg)
    ObjSetter.setobj(650,450,50,50,wallImg)
    
    ObjSetter.setobj(800,150,50,50,wallImg)
    ObjSetter.setobj(850,150,50,50,wallImg)
    ObjSetter.setobj(900,150,50,50,wallImg)
    ObjSetter.setobj(800,200,50,50,wallImg)
    ObjSetter.setobj(850,200,50,50,wallImg)
    ObjSetter.setobj(900,200,50,50,wallImg) 
    
    ObjSetter.setobj(750,350,50,50,wallImg)
    ObjSetter.setobj(800,350,50,50,wallImg)
    ObjSetter.setobj(850,350,50,50,wallImg)
    ObjSetter.setobj(750,400,50,50,wallImg)
    ObjSetter.setobj(800,400,50,50,wallImg)
    ObjSetter.setobj(850,400,50,50,wallImg)
    
    ObjSetter.setobj(500,0,50,50,wallImg)
    # To think I wrote all that and got it off by 50px on the x axis. URRGGEEE
    
    # Set Traps
    if ObjSetter.setNonSolidObj(150,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(200,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(550,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(450,50,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(350,100,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(0,350,50,50,SpikesImg) == True:
        restart()       
    if ObjSetter.setNonSolidObj(50,350,50,50,SpikesImg) == True:
        restart()      
    if ObjSetter.setNonSolidObj(150,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(200,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(550,0,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(350,100,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(0,350,50,50,SpikesImg) == True:
        restart()       
    if ObjSetter.setNonSolidObj(50,350,50,50,SpikesImg) == True:
        restart()      
    if ObjSetter.setNonSolidObj(200,500,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(300,350,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(300,400,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(350,300,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(350,350,50,50,SpikesImg) == True:
        restart()       
    if ObjSetter.setNonSolidObj(350,400,50,50,SpikesImg) == True:
        restart()      
    if ObjSetter.setNonSolidObj(450,225,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(600,200,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(500,400,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(950,500,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(950,550,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(900,550,50,50,SpikesImg) == True:
        restart()           
        
    # Door
    keys=pygame.key.get_pressed()
    import Level1
    if Level1.buttontest == False:
        if ObjSetter.setNonSolidObj(250,200,50,100,doorClosedImg) == True:
            restart()
        if ObjSetter.setNonSolidObj(25,500,20,20,buttonOffImg) == True:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if keys[K_RETURN]:
                        Level1.buttontest = True
    else:
        ObjSetter.setNonSolidObj(250,200,50,100,doorOpenImg)
        if ObjSetter.setNonSolidObj(25,500,20,20,buttonOnImg) == True:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if keys[K_RETURN]:
                        Level1.buttontest = False    
                        
    # Portal
    if ObjSetter.setNonSolidObj(900,50,50,50,portalImg) == True:
        Globals.levelnum = 2
        restart()
        