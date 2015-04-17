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
                        
# Wire system, very messy. If anyone knows a better way to do this please do it.
# There is currently a limit of 10 wires per level
# This can be increased by increasing the variables and copy/pasting the code handling them

wire1 = 1
wire2 = 1
wire3 = 1
wire4 = 1
wire5 = 1
wire6 = 1
wire7 = 1
wire8 = 1
wire9 = 1
wire10 = 1

wirex1 = 2000
wirex2 = 2000
wirex3 = 2000
wirex4 = 2000
wirex5 = 2000
wirex6 = 2000
wirex7 = 2000
wirex8 = 2000
wirex9 = 2000
wirex10 = 2000

wirey1 = 2000
wirey2 = 2000
wirey3 = 2000
wirey4 = 2000
wirey5 = 2000
wirey6 = 2000
wirey7 = 2000
wirey8 = 2000
wirey9 = 2000
wirey10 = 2000

def setwire(x,y,img,idnum): # sets the wires in place, fill in varaibles needed for pathfinding
    keys=pygame.key.get_pressed()
    import ObjSetter
    if idnum == 1:
        if ObjSetter.wire1 == 1:
            ObjSetter.wirex1 = x
            ObjSetter.wirey1 = y
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire1 = 0
                ObjSetter.wirex1 = 2000
                ObjSetter.wirey1 = 2000             
                
    if idnum == 2:
        if ObjSetter.wire2 == 1:
            ObjSetter.wirex2 = x
            ObjSetter.wirey2 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire2 = 0  
                ObjSetter.wirex2 = 2000
                ObjSetter.wirey2 = 2000                
                            
    if idnum == 3:
        if ObjSetter.wire3 == 1:
            ObjSetter.wirex3 = x
            ObjSetter.wirey3 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire3 = 0    
                ObjSetter.wirex3 = 2000
                ObjSetter.wirey3 = 2000                
                                        
    if idnum == 4:
        if ObjSetter.wire4 == 1:
            ObjSetter.wirex4 = x
            ObjSetter.wirey4 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire4 = 0     
                ObjSetter.wirex4 = 2000
                ObjSetter.wirey4 = 2000                
                                                    
    if idnum == 5:
        if ObjSetter.wire5 == 1:
            ObjSetter.wirex5 = x
            ObjSetter.wirey5 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire5 = 0     
                ObjSetter.wirex5 = 2000
                ObjSetter.wirey5 = 2000                
                
    if idnum == 6:
        if ObjSetter.wire6 == 1:
            ObjSetter.wirex6 = x
            ObjSetter.wirey6 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire6 = 0
                ObjSetter.wirex6 = 2000
                ObjSetter.wirey6 = 2000                
                
    if idnum == 7:
        if ObjSetter.wire7 == 1:
            ObjSetter.wirex7 = x
            ObjSetter.wirey7 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire7 = 0  
                ObjSetter.wirex7 = 2000
                ObjSetter.wirey7 = 2000                
                            
    if idnum == 8:
        if ObjSetter.wire8 == 1:
            ObjSetter.wirex8 = x
            ObjSetter.wirey8 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire8 = 0  
                ObjSetter.wirex8 = 2000
                ObjSetter.wirey8 = 2000                
                                        
    if idnum == 9:
        if ObjSetter.wire9 == 1:
            ObjSetter.wirex9 = x
            ObjSetter.wirey9 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire9 = 0   
                ObjSetter.wirex9 = 2000
                ObjSetter.wirey9 = 2000                
                                                    
    if idnum == 10:
        if ObjSetter.wire10 == 1:
            ObjSetter.wirex10 = x
            ObjSetter.wirey10 = y            
            if ObjSetter.setNonSolidObj(x,y,50,50,img) == True and keys[K_z]:
                ObjSetter.wire10 = 0
                ObjSetter.wirex10 = 2000
                ObjSetter.wirey10 = 2000                
                
def testpath(startx,starty,endx,endy): # tests if an electrical path is complete
    for i in range (0,101):
        import ObjSetter
        if i == 1 or i == 11 or i == 21 or i == 31 or i == 41 or i == 51 or i == 61 or i == 71 or i == 81 or i == 91: x,y = ObjSetter.wirex1,ObjSetter.wirey1
        if i == 2 or i == 12 or i == 22 or i == 32 or i == 42 or i == 52 or i == 62 or i == 72 or i == 82 or i == 92: x,y = ObjSetter.wirex2,ObjSetter.wirey2
        if i == 3 or i == 13 or i == 23 or i == 33 or i == 43 or i == 53 or i == 63 or i == 73 or i == 83 or i == 93: x,y = ObjSetter.wirex3,ObjSetter.wirey3
        if i == 4 or i == 14 or i == 24 or i == 34 or i == 44 or i == 54 or i == 64 or i == 74 or i == 84 or i == 94: x,y = ObjSetter.wirex4,ObjSetter.wirey4
        if i == 5 or i == 15 or i == 25 or i == 35 or i == 45 or i == 55 or i == 65 or i == 75 or i == 85 or i == 95: x,y = ObjSetter.wirex5,ObjSetter.wirey5
        if i == 6 or i == 16 or i == 26 or i == 36 or i == 46 or i == 56 or i == 66 or i == 76 or i == 86 or i == 96: x,y = ObjSetter.wirex6,ObjSetter.wirey6
        if i == 7 or i == 17 or i == 27 or i == 37 or i == 47 or i == 57 or i == 67 or i == 77 or i == 87 or i == 97: x,y = ObjSetter.wirex7,ObjSetter.wirey7
        if i == 8 or i == 18 or i == 28 or i == 38 or i == 48 or i == 58 or i == 68 or i == 78 or i == 88 or i == 98: x,y = ObjSetter.wirex8,ObjSetter.wirey8
        if i == 9 or i == 19 or i == 29 or i == 39 or i == 49 or i == 59 or i == 69 or i == 79 or i == 89 or i == 99: x,y = ObjSetter.wirex9,ObjSetter.wirey9
        if i == 0 or i == 10 or i == 20 or i == 30 or i == 40 or i == 50 or i == 60 or i == 70 or i == 80 or i == 90: x,y = ObjSetter.wirex10,ObjSetter.wirey10  
        print(i)
        print(x)
        print(y)
        # If touching next wire
        if x <= startx + 60:	
            if x + 60 >= startx:
                if y <= starty + 45: 
                    if y + 60 >= starty:
                        print("got next wire")
                        # if touching next wire
                        if x <= endx + 60: # if touching end
                            if x + 60 >= endx:
                                if y <= endy + 45:
                                    if y + 60 >= endy:
                                        print("got end")
                                        return True; break
                                    else:
                                        startx,starty = x,y                      
                                else:
                                    startx,starty = x,y                                    
                            else:
                                startx,starty = x,y                                
                        else:
                            startx,starty = x,y     