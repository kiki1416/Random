"""
Attempting to add multiple wall with collisions using rect functs and possibly a for loop
also converting our screen clamp borders into walls with rec
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

SPEED = 300 
R = 40
w, h = screen.get_size() 


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

      
player_rect = pygame.Rect(0, 0, (R*2), (R*2))  
player_rect.center = player_pos 

## wall definitions
wall1_rect = pygame.Rect((screen.get_width() / 2) + 300, (screen.get_height() / 2) - 150, 40, 300)
wall2_rect = pygame.Rect((screen.get_width() / 2) - 300, (screen.get_height() / 2) - 100, 100, 200)
left_border_rect = pygame.Rect(-1,0,1,h) # note the minus 1 values as this basically puts our walls off screen
right_border_rect = pygame.Rect(w,0,1,h) # if we wanted different types of walls, we might make a dictionary or list of lists 
top_border_rect = pygame.Rect(0,-1,w,1) # then we can put other properties to iterate through later (colour, behaviour, etc.)
bot_border_rect = pygame.Rect(0,h,w,1)

wall_list = [wall1_rect, wall2_rect, # for now we put all the wall rects in a list for iteration
             left_border_rect, right_border_rect, 
             top_border_rect, bot_border_rect] 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
 
    dx = (keys[pygame.K_d] - keys[pygame.K_a]) * SPEED * dt 
    dy = (keys[pygame.K_s] - keys[pygame.K_w]) * SPEED * dt 

    player_pos.x += dx 
    player_rect.centerx = round(player_pos.x) 
    
    for rect in wall_list: # iterate through our wall lift to add collisions to all of them, makes it super easy to define or append new walls to the list
        if player_rect.colliderect(rect):
            if dx > 0:
                player_rect.right = rect.left
            elif dx < 0:
                player_rect.left = rect.right
            
            player_pos.x = player_rect.centerx

    player_pos.y += dy # we have to keep the actual movement outside of the loops
    player_rect.centery = round(player_pos.y)
    
    for rect in wall_list:    
        if player_rect.colliderect(rect):
            if dy > 0:
                player_rect.bottom = rect.top
            elif dy < 0:
                player_rect.top = rect.bottom
            
            player_pos.y = player_rect.centery

    player_rect.center = player_pos      
    player_pos.update(player_rect.center) 

    
    
    screen.fill("purple") 
    pygame.draw.circle(screen, "red", player_pos, R)   
    for wrect in wall_list:
        pygame.draw.rect(screen, "green", wrect)
    # notice that we got rid of the screenclamping as now we have defined our screen borders as walls
    pygame.display.flip() 
    
    dt = clock.tick(60) / 1000

pygame.quit()