"""
Attempting to add a wall with collisions using rect functs
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
wall_pos = pygame.Vector2((screen.get_width() / 2) + 300, screen.get_height() / 2)

screen_rect = screen.get_rect()        
player_rect = pygame.Rect(0, 0, (R*2), (R*2))  
player_rect.center = player_pos  
wall_rect = pygame.Rect(0, 0, 40, 300)
wall_rect.center = wall_pos

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
 
    dx = (keys[pygame.K_d] - keys[pygame.K_a]) * SPEED * dt #this is cool boolean arithmetic as keys is just a tuple, i.e. here if u press a and d at the same time, dx will be 0
    dy = (keys[pygame.K_s] - keys[pygame.K_w]) * SPEED * dt 

    player_pos.x += dx # we can then just change the player position by the overall x movement multiplied by speed * time (distance)
    player_rect.centerx = round(player_pos.x) #stops python from truncating floats down and then making overall movement a bit jittery, i.e round() truncates 4.8 to 5 not 4
    
    collide = pygame.Rect.colliderect(player_rect, wall_rect)
    if collide:
        if dx > 0:
            player_rect.right = wall_rect.left
        elif dx < 0:
            player_rect.left = wall_rect.right
        
        player_pos.x = player_rect.centerx

    player_pos.y += dy
    player_rect.centery = round(player_pos.y)
    
    collide = pygame.Rect.colliderect(player_rect, wall_rect)
    if collide:
        if dy > 0:
            player_rect.bottom = wall_rect.top
        elif dy < 0:
            player_rect.top = wall_rect.bottom
        
        player_pos.y = player_rect.centery

    player_rect.center = player_pos
    player_rect.clamp_ip(screen_rect)        
    player_pos.update(player_rect.center) 

    
    
    screen.fill("purple") 
    pygame.draw.circle(screen, "red", player_pos, R)   
    pygame.draw.rect(screen, "green", wall_rect)
    
    pygame.display.flip() 
    
    dt = clock.tick(60) / 1000

pygame.quit()