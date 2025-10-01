"""
The last attempt at borders worked but would not be best practise for a number of reasons:
    - Dont account for the radius (so you clip).
    - Can fail when you overshoot a border in a single frame: the condition still lets you go further out or prevents re-entry if you mix the inequalities wrong.
    - Get verbose as soon as you add more obstacles.
in this attempt i want to try what chat calls 'Move then clamp', the idea is that we define width, height and radius as vars, and then have a max and min that uses this
the other option is to use the rect function which we saw previously in the ball example
`` - from chatgpt
R = 40
w, h = 1280, 720  # or: w, h = screen.get_size()

# after youve updated player_pos.x/y with keys and dt:
player_pos.x = max(R, min(w - R, player_pos.x))
player_pos.y = max(R, min(h - R, player_pos.y))

``
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
R = 40
w, h = screen.get_size() # using screen get size to be a bit more dynamic, wonder how this works, I assume its getting what we have set above

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, R)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    player_pos.x = max(R, min(w - R, player_pos.x))
    player_pos.y = max(R, min(h - R, player_pos.y))
    
    #Okay so the idea here the min part will take whatever is smaller, either the centre or the boarder, and the same for the max, whichever is larger
    #so left edge is where x >= Radius, i.e. radius is 40, so when centre is at 40, our shape is at that edge
    #right edge is x <= w -R, i.e. the width, 1280 minus 40 is where the centre will sit at the edge
    #likewise for the top and bottom, and the centre must always stay in these bounds
    #this is very neat clamping
        
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()