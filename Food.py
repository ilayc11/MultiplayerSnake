import random
import pygame
from pygame import SurfaceType

WHITE=(255,255,255)
BLUE = (0, 0, 255)

class Food():
    def __init__(self,screen:SurfaceType,xbound1:float,xbound2:float,ybound1:float,ybound2:float) ->None :
        self.Xbound1 = xbound1
        self.Xbound2 = xbound2
        self.Ybound1 = ybound1
        self.Ybound2 = ybound2
        self.shape=pygame.Rect(0,0,20,20)
        self.screen=screen
        self.curXPos=None
        self.curYPos=None
        self.reset()
    def draw(self)->None:
        pygame.draw.rect(self.screen,BLUE,self.shape)
    def reset(self):
        self.curXPos = random.randint(self.Xbound1, self.Xbound2)
        self.curYPos = random.randint(self.Ybound1, self.Ybound2)
        self.shape.center = (self.curXPos, self.curYPos)
