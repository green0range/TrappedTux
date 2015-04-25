import pygame, sys, Globals
from pygame.locals import *
pygame.init()

i1if=Globals.get_asset_name("StorylineARCintro.png")
introback1Img = pygame.image.load(i1if).convert_alpha()

i2if=Globals.get_asset_name("storyline-storm.png")
introback2Img = pygame.image.load(i2if).convert_alpha()

stage = 1

def playintro():
    import introstory
    keys=pygame.key.get_pressed()
    
    if introstory.stage == 1:
        
        Globals.screen.blit(introback1Img,(0,0))
        # Could have this in a language file for multi-language support
        introtextl1 = "The Antarctica Research Centre (ARC) is the biggest research facility in the world, it attempts to find a way" 
        introtextl2 = "of controlling atmospheric conditions."
        instructiontext = "[ENTER]"
        
        gray = (168,168,168)
        Font = pygame.font.SysFont("Times New Roman", 16)
        l1VarRender = Font.render(str(introtextl1), 1, gray)
        l2VarRender = Font.render(str(introtextl2), 1, gray)
        instructVarRender = Font.render(str(instructiontext), 1, gray)
        Globals.screen.blit(l1VarRender, (50,10))   
        Globals.screen.blit(l2VarRender, (50,30)) 
        Globals.screen.blit(instructVarRender, (800,200)) 
    elif introstory.stage == 2:
        Globals.screen.blit(introback2Img,(0,0))
        instructiontext = "[ENTER]"
        gray = (168,168,168)
        Font = pygame.font.SysFont("Times New Roman", 16)   
        instructVarRender = Font.render(str(instructiontext), 1, gray)
        Globals.screen.blit(instructVarRender, (900,575)) 
    else:
        import Main
        Main.gamestarted = True
        
    for event in pygame.event.get():
        if event.type == KEYUP:    
            if keys[K_RETURN]:
                introstory.stage +=1