"""
This is much more of a test, I just want to play around with being extremely newtonian
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0
vy = 0.0
vx = 0.0
GRAVITY = 1600
JUMP_SPEED = 800
grounded = False 
SPEED = 300
R = 40
w, h = screen.get_size()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_rect = pygame.Rect(0, 0, R*2, R*2)
player_rect.center = player_pos

left_border_rect = pygame.Rect(-1,0,1,h) 
right_border_rect = pygame.Rect(w,0,1,h) 
top_border_rect = pygame.Rect(0,-1,w,1) 
bot_border_rect = pygame.Rect(0,h,w,1)

wall_list = [left_border_rect, right_border_rect, 
             top_border_rect, bot_border_rect]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    dx = (keys[pygame.K_d] - keys[pygame.K_a]) * SPEED * dt 

    player_pos.x += dx 
    player_rect.centerx = round(player_pos.x) 
    
    for rect in wall_list: 
        if player_rect.colliderect(rect):
            if dx > 0:
                player_rect.right = rect.left
            elif dx < 0:
                player_rect.left = rect.right
            
            player_pos.x = player_rect.centerx
    
    vy += GRAVITY * dt
    player_pos.y += vy * dt
    player_rect.centery = round(player_pos.y)
    grounded = False
    for rect in wall_list:
        if player_rect.colliderect(rect):
            if vy > 0:
                player_rect.bottom = rect.top
                player_pos.y = player_rect.centery
                vy = 0
                grounded = True
                break
            elif vy < 0:
                player_rect.top = rect.bottom
                player_pos.y = player_rect.centery
                vy = 0
            
    
    if keys[pygame.K_SPACE] and grounded:
        vy = -JUMP_SPEED
        grounded = False

    player_rect.center = player_pos      
    player_pos.update(player_rect.center) 

    screen.fill("white") 
    pygame.draw.circle(screen, "black", player_pos, R)   
    for wrect in wall_list:
        pygame.draw.rect(screen, "green", wrect)
    
    pygame.display.flip() 
    
    dt = clock.tick(60) / 1000

pygame.quit()     