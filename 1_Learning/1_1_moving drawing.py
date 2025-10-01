'''trying to make a simple game that moves a shape around'''
import pygame

#setup all over again woo
pygame.init()
screen = pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0 #no clue what this does yet, obv dt looks like a time step

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) 
#unsure why we divide by 2 just yet, player position seems self explanatory, vector 2 and 3 look like they refer to x and y axis respectively. 
#to be fair its probably just to find the centre of the screen

while running:
    for event in pygame.event.get(): #a list(?) of events happening per frame(?)
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    pygame.draw.circle(screen, 'red', player_pos, 40) #where: screen, #colour: red, radius: 40 (pixels(?))
    
    keys = pygame.key.get_pressed() #i guess keys is a list or perhaps a dictionary since we index with the key name and not th enumeric index(?), hence we can look through with the conditionals
    if keys[pygame.K_w]: #i.e. if key w is in the list of keys pressed
        player_pos.y -= 300 * dt #then we know player_pos is a coord so, take the y of the coord, and - 300 from it, multiplied by the time step(?)
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    pygame.display.flip() #we flip every frame(?) to update the display with each
   
    #we want to limit to 60 fps again, but the point of dt is the actual time in seconds since the last frame, thus our physics is framerate independent
    # i dont really understand this, for context in our first try we just had a single line that said clock.tick(60) so not entirely sure what the difference here is
    dt = clock.tick(60) / 1000

pygame.quit() #also useful to understand why we put this quit on the outside,
#i guess the idea is the only time the running loop will break is if we quit, and thus we want to quit the whole program
