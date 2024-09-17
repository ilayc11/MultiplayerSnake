import pygame

# Constants for snake movement
CELL_SIZE = 20
MOVE_DISTANCE = CELL_SIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
STARTPOS = [(0, 0), (-20, 0), (-40, 0)]
WHITE = (255, 255, 255)

class Snake:
    def __init__(self,screen):
        self.segments = []
        self.direction = RIGHT
        self.create_snake()
        self.screen = screen

    def create_snake(self):
        for pos in STARTPOS:
            self.add_segment(pos)

    def add_segment(self, position):
        self.segments.append(pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE))

    def extend(self):
        tail = self.segments[-1]
        tail_pos = (tail.x, tail.y)
        self.add_segment(tail_pos)

    def move(self):
        # Move all segments
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].x = self.segments[i - 1].x
            self.segments[i].y = self.segments[i - 1].y
        # Move head
        head = self.segments[0]
        head.x += self.direction[0] * MOVE_DISTANCE
        head.y += self.direction[1] * MOVE_DISTANCE

    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.direction = RIGHT

    def set_direction(self, new_direction):
        # Prevent reversing direction
        opposite_directions = {
            UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT
        }
        if self.direction != opposite_directions.get(new_direction, None):
            self.direction = new_direction

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(self.screen, WHITE, segment)

    def check_collision_with_self(self):
        # Check if the snake's head collides with any of its body segments
        head = self.segments[0]
        for segment in self.segments[1:]:
            if head.colliderect(segment):
                return True
        return False

