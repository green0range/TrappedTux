#! /usr/bin/python

# The Main script handles window creation, menus, level numbers and which other scripts and run.
# Only run this script.

# Setup pygame
import pygame, sys, Globals, Movement # Main imports
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Trapped Tux")

gamestarted = False

# Resource setup
# Background Image File
bif = Globals.get_asset_name("background.png")
backgroundImg = pygame.image.load(bif).convert_alpha()
# Character Image File
cif = Globals.get_asset_name("tuxTopViewLookingDown.png")
playerImg = pygame.image.load(cif).convert_alpha()
# Level imports
import introstory, Level1, Level2, Level3  # and new levels here

# Animation
def changeFaceDir(direction):
    import Main
    if direction == "up":
        Main.cif = Globals.get_asset_name("tuxTopViewLookingUp.png")
    if direction == "down":
        Main.cif = Globals.get_asset_name("tuxTopViewLookingDown.png")
    if direction == "right":
        Main.cif = Globals.get_asset_name("tuxTopViewLookingRight.png")
    if direction == "left":
        Main.cif = Globals.get_asset_name("tuxTopViewLookingLeft.png")
    Main.playerImg = pygame.image.load(cif).convert_alpha()

# Display font
black = (0,0,0)
Font = pygame.font.SysFont("Times New Roman", 12)

# Frame limiter
frameLimit = 60 # Set this to the refresh rate of your monitor
Globals.playerMoveSpeed = (frameLimit / (frameLimit * 0.1)) * 0.2
clock = pygame.time.Clock()

# Main loop
while True:
    # Closes game when X button pressed
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                
    # Draw Background
    Globals.screen.blit(backgroundImg,(0,0))

    # Controls the movement of the player
    Movement.checkMovement() 
    
    # Controls which level is called
    if gamestarted:

        # Draw Backgrounds/beneath ObjSetter
        Globals.screen.blit(backgroundImg,(0,0))
        # Controls the movement of the player
        Movement.checkMovement()        
        
        # ObjSetter draws in this
        if Globals.levelnum == 1:
            Level1.playLevel()
        elif Globals.levelnum == 2:
            Level2.playLevel()
        elif Globals.levelnum == 3:
            Level3.playLevel()
            
        # This will be drawn last    
        # Insert things to be drawn on top of the object setter
        Globals.screen.blit(playerImg,(Globals.playerX,Globals.playerY))
        wireVarRender = Font.render(str(Globals.wires), 1, black)
        Globals.screen.blit(wireVarRender, (0, 0))
    else:
        introstory.playintro()

    import ObjSetter
    #ObjSetter.setMoveObj(0,0,900,500,100,True,playerImg,False)
        
    if not Globals.keydelay <= 0:
        Globals.keydelay -= 1

    # Updates the display
    pygame.display.flip()
    
    clock.tick(frameLimit)
    
