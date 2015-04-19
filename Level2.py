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

button1 = False
button2 = False

wirex3,wirey3 = 2000,2000
wirex4,wirey4 = 2000,2000
wirex5,wirey5 = 2000,2000
wirex6,wirey6 = 2000,2000
wirex7,wirey7 = 2000,2000
wirex8,wirey8 = 2000,2000
wirex9,wirey9 = 2000,2000
wirex10,wirey10 = 2000,2000

nextwireid = 3

def restart():
    Globals.playerX = 32
    Globals.playerY = 32    
    ObjSetter.resetwires()
    Globals.wires = 0
    import Level2
    Level2.wirex3,Level2.wirey3 = 2000,2000
    Level2.wirex4,Level2.wirey4 = 2000,2000
    Level2.wirex5,Level2.wirey5 = 2000,2000
    Level2.wirex6,Level2.wirey6 = 2000,2000
    Level2.wirex7,Level2.wirey7 = 2000,2000
    Level2.wirex8,Level2.wirey8 = 2000,2000
    Level2.wirex9,Level2.wirey9 = 2000,2000
    Level2.wirex10,Level2.wirey10 = 2000,2000  
    Level2.button2 = False
    Level2.button1 = False
    
def playLevel():
    
    # Wires
    import Level2    
    ObjSetter.setwire(150,50,wireLRImg,1)
    ObjSetter.setwire(200,50,wireLRImg,2)
    if not Level2.wirex3 == 2000: ObjSetter.setwire(Level2.wirex3,Level2.wirey3,wireLRImg,3)
    if not Level2.wirex4 == 2000: ObjSetter.setwire(Level2.wirex4,Level2.wirey4,wireLRImg,4)
    if not Level2.wirex5 == 2000: ObjSetter.setwire(Level2.wirex5,Level2.wirey5,wireLRImg,5)
    if not Level2.wirex6 == 2000: ObjSetter.setwire(Level2.wirex6,Level2.wirey6,wireLRImg,6)
    if not Level2.wirex9 == 2000: ObjSetter.setwire(Level2.wirex9,Level2.wirey7,wireLRImg,7)
    if not Level2.wirex8 == 2000: ObjSetter.setwire(Level2.wirex8,Level2.wirey8,wireLRImg,8)
    if not Level2.wirex9 == 2000: ObjSetter.setwire(Level2.wirex9,Level2.wirey9,wireLRImg,9)
    if not Level2.wirex10 == 2000: ObjSetter.setwire(Level2.wirex10,Level2.wirey10,wireLRImg,10)    
    
    
    keys=pygame.key.get_pressed()
    
    if ObjSetter.setNonSolidObj(100,50,50,50,wireLRImg):
            if keys[K_z]:
                print("End wire, cannot be moved")    
    if ObjSetter.setNonSolidObj(250,50,50,50,wireLRImg):
            if keys[K_z]:
                print("End wire, cannot be moved")    
    if ObjSetter.setNonSolidObj(300,250,50,50,wireLRImg):
            if keys[K_z]:
                print("End wire, cannot be moved")  
    if ObjSetter.setNonSolidObj(650,300,50,50,wireLRImg):
        if keys[K_z]:
            print("End wire, cannot be moved")
            

    # Create Walls
    ObjSetter.setobj(100,0,50,50,wallImg)
    ObjSetter.setobj(150,0,50,50,wallImg)
    ObjSetter.setobj(200,0,50,50,wallImg)
    ObjSetter.setobj(250,0,50,50,wallImg)
    ObjSetter.setobj(300,0,50,50,wallImg)
    ObjSetter.setobj(350,0,50,50,wallImg)
    ObjSetter.setobj(400,0,50,50,wallImg)
    ObjSetter.setobj(450,0,50,50,wallImg)
    ObjSetter.setobj(500,0,50,50,wallImg)
    ObjSetter.setobj(550,0,50,50,wallImg)
    ObjSetter.setobj(600,0,50,50,wallImg)
    ObjSetter.setobj(650,0,50,50,wallImg)
    ObjSetter.setobj(700,0,50,50,wallImg)
    ObjSetter.setobj(750,0,50,50,wallImg)
    ObjSetter.setobj(800,0,50,50,wallImg)
    ObjSetter.setobj(850,0,50,50,wallImg)
    ObjSetter.setobj(900,0,50,50,wallImg)
    ObjSetter.setobj(950,0,50,50,wallImg) 
    
    ObjSetter.setobj(0,550,50,50,wallImg)
    ObjSetter.setobj(50,550,50,50,wallImg)    
    ObjSetter.setobj(100,550,50,50,wallImg)
    ObjSetter.setobj(150,550,50,50,wallImg)
    ObjSetter.setobj(200,550,50,50,wallImg)
    ObjSetter.setobj(250,550,50,50,wallImg)
    ObjSetter.setobj(300,550,50,50,wallImg)
    ObjSetter.setobj(350,550,50,50,wallImg)
    ObjSetter.setobj(400,550,50,50,wallImg)
    ObjSetter.setobj(450,550,50,50,wallImg)
    ObjSetter.setobj(500,550,50,50,wallImg)
    ObjSetter.setobj(550,550,50,50,wallImg)
    ObjSetter.setobj(600,550,50,50,wallImg)
    ObjSetter.setobj(650,550,50,50,wallImg)
    ObjSetter.setobj(700,550,50,50,wallImg)
    ObjSetter.setobj(750,550,50,50,wallImg)
    ObjSetter.setobj(800,550,50,50,wallImg)
    ObjSetter.setobj(850,550,50,50,wallImg)
    ObjSetter.setobj(900,550,50,50,wallImg)
    ObjSetter.setobj(950,550,50,50,wallImg)    
    
    ObjSetter.setobj(350,50,50,50,wallImg)
    ObjSetter.setobj(350,100,50,50,wallImg)
    ObjSetter.setobj(350,250,50,50,wallImg)
    ObjSetter.setobj(350,300,50,50,wallImg)
    ObjSetter.setobj(350,350,50,50,wallImg)
    ObjSetter.setobj(350,400,50,50,wallImg)
    ObjSetter.setobj(350,450,50,50,wallImg)
    ObjSetter.setobj(350,500,50,50,wallImg)
    
    ObjSetter.setobj(700,50,50,50,wallImg)
    ObjSetter.setobj(700,100,50,50,wallImg)
    ObjSetter.setobj(700,150,50,50,wallImg)
    ObjSetter.setobj(700,200,50,50,wallImg)
    ObjSetter.setobj(700,250,50,50,wallImg)
    ObjSetter.setobj(700,300,50,50,wallImg)
    ObjSetter.setobj(700,450,50,50,wallImg)
    ObjSetter.setobj(700,500,50,50,wallImg)      
    
    # Set Spikes
    # 1st area
    if ObjSetter.setNonSolidObj(200,150,50,50,SpikesImg) == True:
        restart() 
    if ObjSetter.setNonSolidObj(100,300,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(200,350,50,50,SpikesImg) == True:
        restart() 
    if ObjSetter.setNonSolidObj(100,400,50,50,SpikesImg) == True:
        restart() 
    if ObjSetter.setNonSolidObj(300,500,50,50,SpikesImg) == True:
        restart()    
    # 2nd area
    if ObjSetter.setNonSolidObj(450,150,50,50,SpikesImg) == True:
        restart() 
    if ObjSetter.setNonSolidObj(550,100,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(600,250,50,50,SpikesImg) == True:
        restart() 
    if ObjSetter.setNonSolidObj(400,500,50,50,SpikesImg) == True:
        restart() 
    if ObjSetter.setNonSolidObj(550,500,50,50,SpikesImg) == True:
        restart()   
    # 3rd area
    if ObjSetter.setNonSolidObj(950,100,50,50,SpikesImg) == True:
        restart() 
    if ObjSetter.setNonSolidObj(800,250,50,50,SpikesImg) == True:
        restart()
    if ObjSetter.setNonSolidObj(800,450,50,50,SpikesImg) == True:
        restart() 
    if ObjSetter.setNonSolidObj(900,350,50,50,SpikesImg) == True:
        restart()    
        
    # Doors
    # 1st door
    import Level2
    if Level2.button1 == False:
        if ObjSetter.setNonSolidObj(350,150,50,100,doorClosedImg) == True:
            restart()
        if ObjSetter.setNonSolidObj(230,265,20,20,buttonOffImg) == True:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if keys[K_RETURN]:
                        if ObjSetter.testpath(230,265,300,250) == True:
                            Level2.button1 = True
    else:
        ObjSetter.setNonSolidObj(350,150,50,100,doorOpenImg)
        if ObjSetter.setNonSolidObj(230,265,20,20,buttonOnImg) == True:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if keys[K_RETURN]:
                        if ObjSetter.testpath(230,265,300,250) == True:
                            Level2.button1 = False      
    # 2nd door                       
    import Level2
    if Level2.button2 == False:
        if ObjSetter.setNonSolidObj(700,350,50,100,doorClosedImg) == True:
            restart()
        if ObjSetter.setNonSolidObj(3*230-100,265+50,20,20,buttonOffImg) == True:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if keys[K_RETURN]:
                        if ObjSetter.testpath(3*230-100,265+50,650,300) == True:
                            Level2.button2 = True
    else:
        ObjSetter.setNonSolidObj(700,350,50,100,doorOpenImg)
        if ObjSetter.setNonSolidObj(3*230-100,265+50,20,20,buttonOnImg) == True:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if keys[K_RETURN]:
                        if ObjSetter.testpath(3*230-100,265+50,650,300) == True:
                            Level2.button2 = False        
    
    
    # Place wires
    if Globals.wires > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()       
            if event.type == KEYUP:
                if keys[K_x]:
                    if Level2.nextwireid == 3:
                        Level2.wirex3, Level2.wirey3 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    if Level2.nextwireid == 4:
                        Level2.wirex4, Level2.wirey4 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1                    
                    if Level2.nextwireid == 5:
                        Level2.wirex5, Level2.wirey5 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    if Level2.nextwireid == 6:
                        Level2.wirex6, Level2.wirey6 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    if Level2.nextwireid == 7:
                        Level2.wirex7, Level2.wirey7 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1                    
                    if Level2.nextwireid == 8:
                        Level2.wirex8, Level2.wirey8 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    if Level2.nextwireid == 9:
                        Level2.wirex9, Level2.wirey9 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    if Level2.nextwireid == 10:
                        Level2.wirex10, Level2.wirey10 = int(50 * round(float(Globals.playerX)/50)),int(50 * round(float(Globals.playerY)/50))
                        Globals.wires = Globals.wires - 1
                    Level2.nextwireid = Level2.nextwireid + 1    