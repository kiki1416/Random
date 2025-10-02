"""
Okay so doing the clamping went very well, its also a good idea to try experimenting with this rect feature like we saw in the ball demo
`` -chatgpt
R = 40
screen_rect = screen.get_rect()          # <Rect(0, 0, 1280, 720)>
player_rect = pygame.Rect(0, 0, R*2, R*2)
player_rect.center = player_pos
player_rect.clamp_ip(screen_rect)        # in-place clamp to screen
player_pos = pygame.Vector2(player_rect.center)
``
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

SPEED = 300 #useful to 'magic numbers' basically independent vars at the top like radius, width, height or speed
R = 40
w, h = screen.get_size() 

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

screen_rect = screen.get_rect()          # so this is the rectangle coords of the whole screen (Rect(0, 0, 1280, 720))
player_rect = pygame.Rect(0, 0, R*2, R*2) #this describes the bounding box around the circle, just defining the diameter as 2* radius, i.e. the width and height of the rectangle should be the diameter
player_rect.center = player_pos  #this aligns our rectangle with wherever our circle position is


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= SPEED * dt
    if keys[pygame.K_s]:
        player_pos.y += SPEED * dt
    if keys[pygame.K_a]:
        player_pos.x -= SPEED * dt
    if keys[pygame.K_d]:
        player_pos.x += SPEED * dt
    
    player_rect.center = player_pos
    player_rect.clamp_ip(screen_rect)        # in-place clamp to screen, so if any part of the player rect is not inside screen rect, it moves it so it is
    player_pos.update(player_rect.center) #and thus if clamping did take place, this updates the player position to the corrected clamped movement
    #note instead of redefining the variable, we can just update it every time
    
    
    
    screen.fill("purple") #common to put the draws together at the end
    pygame.draw.circle(screen, "red", player_pos, R) #we can put the draw at the end so we are always inline with game time instead of a tick behind    
    
    pygame.display.flip() #flip is part of draw operations
    
    dt = clock.tick(60) / 1000

pygame.quit()