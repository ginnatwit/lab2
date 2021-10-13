import pygame

def pongwalls():

    pygame.init()

    pygame.display.set_caption("Lab2")

    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.update()

    #walls 
    wcolor = pygame.Color("blue")
    wcolor1 = pygame.Color("white")
    BORDER = 50
    #upper wall
    #Rect((left, top), (width, height))
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH,BORDER)))

    #left wall
    pygame.draw.rect(screen, wcolor1, pygame.Rect((0,0),(BORDER,HEIGHT)))

    #bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((50,550),(WIDTH,BORDER)))

    pygame.display.update()

    
    # define a variable to control the main loop
    running = True
    
# main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
if __name__=="__main__":
    # call the main function
    pongwalls()