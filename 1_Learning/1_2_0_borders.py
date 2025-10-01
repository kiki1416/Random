'''taken the prev lesson code and now attempting to add collision boarders'''
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y > 0:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] and player_pos.y < 720:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] and player_pos.x > 0:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] and player_pos.x < 1280:
        player_pos.x += 300 * dt

    #the idea here is that we use the player position coords to say each control only works when the shape is inside the borders
    #initially i wanted to group them all together, or at least have the x axis boundaries and y axis boundaries grouped with an and
    #however the issue is then that once u get to the border, u have no way of getting out of the border, i wonder if there is a better way though, cos this seems a bit long
        
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()