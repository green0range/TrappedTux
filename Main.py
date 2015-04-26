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
import introstory, Level1, Level2 # and new levels here

#Animation
def changeFaceDir(direction):
    if direction == "up":
        cif = Globals.get_asset_name("tuxTopViewLookingUp.png")
    if direction == "down":
        cif = Globals.get_asset_name("tuxTopViewLookingDown.png")   
    if direction == "right":
        cif = Globals.get_asset_name("tuxTopViewLookingRight.png")
    if direction == "left":
        cif = Globals.get_asset_name("tuxTopViewLookingLeft.png")
    playerImg = pygame.image.load(cif).convert_alpha()

# Display font
black = (0,0,0)
Font = pygame.font.SysFont("Times New Roman", 12)
wireVarRender = Font.render(str(Globals.wires), 1, black)

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
    if gamestarted == True:

        # Draw Background
        Globals.screen.blit(backgroundImg,(0,0))
        # Controls the movement of the player
        Movement.checkMovement()        
        
        if Globals.levelnum == 1:
            Level1.playLevel()
        elif Globals.levelnum == 2:
            Level2.playLevel()
            
        # This will be drawn last    
        # Insert things to be drawn on top of the object setter
        Globals.screen.blit(playerImg,(Globals.playerX,Globals.playerY))
        Globals.screen.blit(wireVarRender, (0,0))          
    else:
        introstory.playintro()

    # Updates the display
    pygame.display.flip()
    
    clock.tick(frameLimit)
    
