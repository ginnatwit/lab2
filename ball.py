import pygame

class Ball:
   # pass
   #class variables
    RADIUS = 25

    def __init__(self, x,y, vx,vy, screen, fgcolor, bgcolor, CONSTS):
        #instance variables
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS
    
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)
    
    def update(self):
        #np = op + dp
        #delete old ball
        self.show(self.bgcolor)
        px = self.x + self.vx
        py = self.y + self.vy
        #Check if i'm colliding (wall position)
            #flip the velocity
        #left wall
        if px < (self.CONSTS.BORDER + self.RADIUS): 
            self.vx = -self.vx
        #bottom wall
        if py > ((self.CONSTS.HEIGHT - (self.CONSTS.BORDER * 2)) + self.RADIUS):
            self.vy = -self.vy
        #top wall
        if py <= (self.CONSTS.BORDER + self.RADIUS):
            self.vy = -self.vy



        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)
        