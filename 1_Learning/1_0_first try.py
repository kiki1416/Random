'''first try just using pygame based on documentation etc.'''
import pygame

#This stuff below looks to be the general setup whenevr we start any instance/game, probably worth reading further into this
pygame.init() #initialisation
screen = pygame.display.set_mode((1280, 720)) # remember if u put 1920 by 1080 u should probs figure out how to make it bordered otherwise its (full) fullscreen
clock = pygame.time.Clock()
running = True #this is not some special variable, could call it whatever u like

while running:
    #they call this poll for events, not really sure what that means yet
    #makes sense to have a quit feature though to break from the while loops, and presumably pygame.QUIT is some sort of 'event' that we poll for
    for event in pygame.event.get(): #loop that goes through each event that happens
        if event.type == pygame.QUIT:
            running = False
    #this whole thing makes a lot of sense and is nicely concise.
    screen.fill('blue') #this is literally just to clear the frame - we are still sorting the setup
    
    ##THIS IS WHERE THE ACTUAL GAME WOULD GO
    
    pygame.display.flip() #when i get rid of this nothing we code actually gets displayed, so it looks like this is what actually updates the display (?)
    
    clock.tick(60) #literally 60 ticks (frames) per second cap
    
pygame.quit()