from time import sleep

import pygame
import sys
from Food import Food
from Scoreboard import Scoreboard
from Snake import Snake
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
MOVE_INTERVAL = 100  # Snake moves every 150 milliseconds





pygame.init()
clock=pygame.time.Clock()
MOVE_SNAKE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE_EVENT, MOVE_INTERVAL)

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
snake = Snake(window)
game_over=False
font = pygame.font.SysFont('Arial', 100)

def display_game_over():
    text = font.render("Game Over!", True, (255, 0, 0))
    window.blit(text, (WINDOW_WIDTH // 2-100 , WINDOW_HEIGHT // 2-300 ))
    pygame.display.update()
    sleep(2)

while running:
    window.fill(BLACK)
    snake.draw()
    food.draw()
    scoreboard.displayScore()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
            game_over=False
            snake=Snake(window)
            scoreboard.reset()
            food.reset()
            sleep(3)
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP:
                snake.set_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.set_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.set_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.set_direction((1, 0))
        elif event.type == MOVE_SNAKE_EVENT:  # Move the snake on the timer event
            snake.move()

    if not game_over and snake.segments[0].colliderect(food.shape):
        food.reset()
        snake.extend()  # Extend the snake
        scoreboard.increaseScore()
    if snake.check_collision_with_self():
        game_over=True
        display_game_over()
    if not game_over:
        pygame.display.update()
        #scoreboard.increaseScore()
    clock.tick(60)