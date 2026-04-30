import pygame
import random
from config import *

# ================= SNAKE =================
class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [(10, 10), (9, 10), (8, 10)]
        self.direction = RIGHT
        self.next_dir = RIGHT
        self.grow = 0

    def change_direction(self, d):
        if (d[0]*-1, d[1]*-1) != self.direction:
            self.next_dir = d

    def move(self):
        self.direction = self.next_dir
        x, y = self.body[0]
        dx, dy = self.direction

        new_head = (x + dx, y + dy)
        self.body.insert(0, new_head)

        if self.grow > 0:
            self.grow -= 1
        else:
            self.body.pop()

    def grow_snake(self):
        self.grow += 1

    def collision(self):
        h = self.body[0]
        if h in self.body[1:]:
            return True
        if h[0] < 0 or h[1] < 0 or h[0] >= GRID_W or h[1] >= GRID_H:
            return True
        return False

    def draw(self, screen):
        for i, (x, y) in enumerate(self.body):
            color = DARK_GREEN if i == 0 else GREEN
            pygame.draw.rect(
                screen, color,
                (x * GRID_SIZE, y * GRID_SIZE + UI_HEIGHT, GRID_SIZE, GRID_SIZE)
            )

# ================= FOOD =================
class Food:
    TYPES = [
        {"score": 5, "color": GREEN},
        {"score": 10, "color": YELLOW},
        {"score": 15, "color": RED},
    ]

    def __init__(self):
        self.kind = random.choice(self.TYPES)
        self.pos = (0, 0)
        self.spawn()

    def spawn(self):
        self.kind = random.choice(self.TYPES)
        self.pos = (
            random.randint(0, GRID_W - 1),
            random.randint(0, GRID_H - 1)
        )

    def draw(self, screen):
        if not self.kind:
            self.kind = random.choice(self.TYPES)

        x, y = self.pos
        pygame.draw.rect(
            screen,
            self.kind["color"],
            (x * GRID_SIZE, y * GRID_SIZE + UI_HEIGHT, GRID_SIZE, GRID_SIZE)
        )

# ================= POISON =================
class PoisonFood:
    def __init__(self):
        self.pos = None

    def spawn(self):
        self.pos = (
            random.randint(0, GRID_W - 1),
            random.randint(0, GRID_H - 1)
        )

    def draw(self, screen):
        if self.pos:
            x, y = self.pos
            pygame.draw.rect(
                screen, RED,
                (x * GRID_SIZE, y * GRID_SIZE + UI_HEIGHT, GRID_SIZE, GRID_SIZE)
            )

# ================= POWERUP =================
class PowerUp:
    def __init__(self):
        self.pos = None

    def spawn(self):
        self.pos = (
            random.randint(0, GRID_W - 1),
            random.randint(0, GRID_H - 1)
        )

    def draw(self, screen):
        if self.pos:
            x, y = self.pos
            pygame.draw.rect(
                screen, (0, 255, 255),
                (x * GRID_SIZE, y * GRID_SIZE + UI_HEIGHT, GRID_SIZE, GRID_SIZE)
            )