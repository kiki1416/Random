'''The first example from pygame documentation'''
import sys, pygame
pygame.init()

size = width, height = 1280, 720 #size of window we can see this variable is used later when defining the screen size
speed = [2, 2] #thsi is just vectorised speed, could make it only bounce side to side with say [2, 0]
black = 0, 0, 0 #literally just the colour code for black, could also write 'black'
#note how we dont have a position starting var so it will just start in the top left(?)
screen = pygame.display.set_mode(size)

ball = pygame.image.load("1_Learning\intro_ball.gif")
ballrect = ball.get_rect() #pygame.Rect is a pygame object for storing rectangular coordinates

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed) #this tells it move (self explanatory but worth noting) with speed we defined, so move clearly takes the velocity vector (2D)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0] #all these do is reverese the speed ([2, 2]) when the ball hits the border of the screen
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black) #"Animation is nothing more than a series of single images, which when displayed in sequence do a very good job of fooling the human eye into seeing motion."
    screen.blit(ball, ballrect) # A blit basically means copying pixel colors from one image to another. #in this case, we give it the surface to draw (ball gif) and the position (rect coords)
    pygame.display.flip() #update the display