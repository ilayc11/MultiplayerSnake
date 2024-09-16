from time import sleep

import pygame
import sys
from Food import Food
from Scoreboard import Scoreboard
pygame.init()
clock=pygame.time.Clock()
WINDOW_HEIGHT = 1280
WINDOW_WIDTH = 1024
window=pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
BLACK = (0,0,0)
WHITE = (255,255,255)
window.fill(BLACK)
pygame.display.set_caption('Multiplayer Snake')
pygame.display.flip()
running = True
food = Food(window,200,800,200,800)
scoreboard=Scoreboard(window)
while running:
    for event in pygame.event.get():
        window.fill(BLACK)
        scoreboard.displayScore()
        food.draw()
        if event.type == pygame.QUIT:
            running = False

            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event.button = pygame.mouse.get_pressed()[0]
            scoreboard.reset()
            sleep(3)
        scoreboard.increaseScore()
    clock.tick(60)