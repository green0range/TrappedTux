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
    
    # Wires
    import Level1    
    ObjSetter.setwire(50,500,wireLRImg,1)
    ObjSetter.setwire(100,500,wireLRImg,2)
    ObjSetter.setwire(150,500,wireLUImg,3)
    ObjSetter.setwire(150,450,wireUDImg,4)
    ObjSetter.setwire(150,400,wireUDImg,5)
    ObjSetter.setwire(150,350,wireUDImg,6)
    ObjSetter.setwire(150,300,wireDRImg,7)   
    if not Level1.wirex8 == 2000: ObjSetter.setwire(Level1.wirex8,Level1.wirey8,wireLRImg,8)
    if not Level1.wirex9 == 2000: ObjSetter.setwire(Level1.wirex9,Level1.wirey9,wireLRImg,9)
    if not Level1.wirex10 == 2000: ObjSetter.setwire(Level1.wirex10,Level1.wirey10,wireLRImg,10)
    
    keys=pygame.key.get_pressed()
    
    if ObjSetter.setNonSolidObj(200,300,50,50,wireLRImg):
        if keys[K_z]:
            print("End wire, cannot be moved")

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
    import Level1
    if Level1.buttontest == False:
        if ObjSetter.setNonSolidObj(250,200,50,100,doorClosedImg) == True:
            restart()
        if ObjSetter.setNonSolidObj(35,515,20,20,buttonOffImg) == True:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if keys[K_RETURN]:
                        if ObjSetter.testpath(25,500,200,300) == True:
                            Level1.buttontest = True
    else:
        ObjSetter.setNonSolidObj(250,200,50,100,doorOpenImg)
        if ObjSetter.setNonSolidObj(35,515,20,20,buttonOnImg) == True:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if keys[K_RETURN]:
                        if ObjSetter.testpath(25,500,200,300) == True:
                            Level1.buttontest = False    
                        
    # Portal
    if ObjSetter.setNonSolidObj(900,50,50,50,portalImg) == True:
        Globals.levelnum = 2
        restart()
    
    # Place wires
    if Globals.wires > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()       
            if event.type == KEYUP:
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
