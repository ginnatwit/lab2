import pygame
import random
from paddle import Paddle
from ball import Ball
from collections import namedtuple

def pongwalls():

    pygame.init()

    pygame.display.set_caption("Lab3")

    WIDTH = 1440
    HEIGHT = 960
    VELOCITY = 5
    BORDER = 50
    FPS = 60 #FRAMERATE

    MyConstants = namedtuple("MyConstants", ("WIDTH", "HEIGHT", "VELOCITY", "BORDER", "FPS"))

    CONSTS = MyConstants(WIDTH, HEIGHT, VELOCITY, BORDER, FPS)
    print(CONSTS.BORDER)


    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.update()

    #walls 
    fgcolor = pygame.Color("blue")
    wcolor1 = pygame.Color("white")
    bgcolor = pygame.Color("black") 
    #upper wall
    #Rect((left, top), (width, height))
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0),(WIDTH,BORDER)))

    #left wall
    pygame.draw.rect(screen, wcolor1, pygame.Rect((0,0),(BORDER,HEIGHT)))

    #bottom wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))
    
    #Ball init
    x0 = (random.randint(BORDER ,WIDTH - Ball.RADIUS))
    #x0 = WIDTH - Ball.RADIUS
    #y0 = HEIGHT // 2
    y0 = (random.randint(BORDER - 10, HEIGHT // 2))
    #vx0 = -VELOCITY
    vx0 = -VELOCITY
    #vy0 = VELOCITY
    vy0 = (random.randint(-VELOCITY, VELOCITY))
    #TODO +/- degree/radius 


    b0 = Ball(x0, y0, vx0,vy0, screen, fgcolor, bgcolor, CONSTS)
    b0.show(fgcolor)

    pygame.display.update()

    
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    
# main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)

        #Ball
        b0.update()

if __name__=="__main__":
    # call the main function
    pongwalls()