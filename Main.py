# The Main script handles window creation, menus, level numbers and which other scripts and run.
# Only run this script.

# Setup pygame
import pygame, sys, Globals, Movement # Main imports
from pygame.locals import *
pygame.init()

gamestarted = True

# Resource setup
# Background Image File
bif = "background.png"
backgroundImg = pygame.image.load(bif).convert_alpha()
# Character Image File
cif = "tuxTopViewLookingDown.png"
playerImg = pygame.image.load(cif).convert_alpha()
# Level imports
import Level1, Level2 # and new levels here

#Animation
def changeFaceDir(direction):
    if direction == "up":
        cif = "tuxTopViewLookingUp.png"
    if direction == "down":
        cif = "tuxTopViewLookingDown.png"   
    if direction == "right":
        cif = "tuxTopViewLookingRight.png"
    if direction == "left":
        cif = "tuxTopViewLookingLeft.png"
    playerImg = pygame.image.load(cif).convert_alpha()


Font = pygame.font.SysFont("Times New Roman", 12)

# Main loop
while True:
    # Closes game when X button pressed
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Updates the display
    pygame.display.update()
    
    # Draw Background
    Globals.screen.blit(backgroundImg,(0,0))
    
    
    # Controls the movement of the player
    Movement.checkMovement() 
    
    # Controls which level is called
    if gamestarted == True:
        if Globals.levelnum == 1:
            Level1.playLevel()
        elif Globals.levelnum == 2:
            Level2.playLevel()
            
    # This will be drawn last    
    # Insert things to be drawn on top of the object setter
    Globals.screen.blit(playerImg,(Globals.playerX,Globals.playerY))
    
    # Draw variables on screen
    black = (0,0,0)

    wireVarRender = Font.render(str(Globals.wires), 1, black)
    Globals.screen.blit(wireVarRender, (0,0))
