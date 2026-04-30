import pygame
import sys
import db
from game import Snake, Food, PoisonFood, PowerUp
from config import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + UI_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20)
big = pygame.font.SysFont("Arial", 40)

def ask_name():
    name = ""
    while True:
        screen.fill(BLACK)

        t = big.render("Enter name", True, WHITE)
        screen.blit(t, (200, 100))

        n = font.render(name, True, YELLOW)
        screen.blit(n, (250, 200))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return name
                elif e.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += e.unicode

def game(username):
    snake = Snake()
    food = Food()
    poison = PoisonFood()
    power = PowerUp()

    score = 0
    level = 1

    delay = 120
    last = pygame.time.get_ticks()

    while True:
        screen.fill(BLACK)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif e.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif e.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif e.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        now = pygame.time.get_ticks()

        if now - last > delay:
            snake.move()
            last = now

            if snake.collision():
                return score, level

            if snake.body[0] == food.pos:
                snake.grow_snake()
                score += food.kind["score"]
                food.spawn()

        food.draw(screen)
        snake.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

def main():
    db.setup_schema()
    username = ask_name()

    while True:
        score, level = game(username)
        db.save_session(username, score, level)

if __name__ == "__main__":
    main()