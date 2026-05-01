import pygame
import random

pygame.init()

# ================= НАСТРОЙКИ =================
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_W = WIDTH // GRID_SIZE
GRID_H = HEIGHT // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Full Screen Grid")

clock = pygame.time.Clock()

# цвета
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

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

    def shrink(self):
        if len(self.body) > 1:
            self.body.pop()
        else:
            self.reset()

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
                (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            )

# ================= FOOD =================
class Food:
    TYPES = [
        {"score": 5, "color": GREEN},
        {"score": 10, "color": YELLOW},
        {"score": 15, "color": RED},
    ]

    def __init__(self):
        self.spawn()

    def spawn(self):
        self.kind = random.choice(self.TYPES)
        self.pos = (
            random.randint(0, GRID_W - 1),
            random.randint(0, GRID_H - 1)
        )

    def draw(self, screen):
        x, y = self.pos
        pygame.draw.rect(
            screen,
            self.kind["color"],
            (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

# ================= POISON =================
class PoisonFood:
    def __init__(self):
        self.pos = None

    def spawn(self, snake_body):
        while True:
            pos = (
                random.randint(0, GRID_W - 1),
                random.randint(0, GRID_H - 1)
            )
            if pos not in snake_body:
                self.pos = pos
                break

    def draw(self, screen):
        if self.pos:
            x, y = self.pos
            pygame.draw.rect(
                screen, RED,
                (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            )

# ================= BARRIER =================
class Barrier:
    def __init__(self):
        self.blocks = []

    def generate(self, count=20):
        self.blocks = []
        for _ in range(count):
            pos = (
                random.randint(0, GRID_W - 1),
                random.randint(0, GRID_H - 1)
            )
            self.blocks.append(pos)

    def draw(self, screen):
        for x, y in self.blocks:
            pygame.draw.rect(
                screen, GRAY,
                (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            )

# ================= GAME OVER =================
def draw_game_over(screen, score):
    font_big = pygame.font.SysFont(None, 60)
    font_small = pygame.font.SysFont(None, 35)

    text1 = font_big.render("GAME OVER", True, RED)
    text2 = font_small.render(f"Score: {score}", True, WHITE)
    text3 = font_small.render("Press R to Restart", True, YELLOW)

    screen.blit(text1, (WIDTH//2 - text1.get_width()//2, HEIGHT//2 - 60))
    screen.blit(text2, (WIDTH//2 - text2.get_width()//2, HEIGHT//2))
    screen.blit(text3, (WIDTH//2 - text3.get_width()//2, HEIGHT//2 + 50))

# ================= ИГРА =================
snake = Snake()
food = Food()
poison = PoisonFood()
barrier = Barrier()

poison.spawn(snake.body)
barrier.generate()

score = 0
font = pygame.font.SysFont(None, 30)
game_over = False

running = True

while running:
    clock.tick(10)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

            if game_over and event.key == pygame.K_r:
                snake.reset()
                food.spawn()
                poison.spawn(snake.body)
                barrier.generate()
                score = 0
                game_over = False

    if not game_over:
        snake.move()

        if snake.collision():
            game_over = True

        if snake.body[0] == food.pos:
            snake.grow_snake()
            score += food.kind["score"]
            food.spawn()

        if poison.pos and snake.body[0] == poison.pos:
            snake.shrink()
            score -= 5
            poison.spawn(snake.body)

        if snake.body[0] in barrier.blocks:
            game_over = True

    # отрисовка
    snake.draw(screen)
    food.draw(screen)
    poison.draw(screen)
    barrier.draw(screen)

    # счет
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        draw_game_over(screen, score)

    pygame.display.flip()

pygame.quit()