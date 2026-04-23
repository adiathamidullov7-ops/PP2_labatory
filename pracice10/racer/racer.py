import pygame
import random

pygame.init()

# Размер окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race")

clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

# Дорога
ROAD_LEFT = 50
ROAD_WIDTH = 300

# Полосы (3 полосы)
lane_width = ROAD_WIDTH // 3
lanes = [
    ROAD_LEFT + lane_width // 2 - 25,
    ROAD_LEFT + lane_width + lane_width // 2 - 25,
    ROAD_LEFT + lane_width * 2 + lane_width // 2 - 25
]

# Игрок
player_width = 50
player_height = 90
player_lane = 1
player_x = lanes[player_lane]
player_y = HEIGHT - 120
player_speed = 5

# Трафик (3 машины)
traffic = []
for i in range(3):
    lane = random.randint(0, 2)
    x = lanes[lane]
    y = random.randint(-600, -100)
    speed = random.randint(4, 7)
    traffic.append([lane, x, y, speed])

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление (смена полос)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_lane = max(0, player_lane - 1)
        pygame.time.wait(150)
    if keys[pygame.K_RIGHT]:
        player_lane = min(2, player_lane + 1)
        pygame.time.wait(150)

    player_x = lanes[player_lane]

    # Дорога
    pygame.draw.rect(screen, (60, 60, 60), (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

    # Разметка 3 полос
    for x in [ROAD_LEFT + lane_width, ROAD_LEFT + lane_width * 2]:
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, WHITE, (x, y, 4, 20))

    # Игрок
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, RED, player_rect)

    # Трафик
    for car in traffic:
        lane, x, y, speed = car

        car_rect = pygame.Rect(x, y, 50, 90)
        pygame.draw.rect(screen, BLUE, car_rect)

        car[2] += speed

        # Перерождение машины
        if car[2] > HEIGHT:
            car[0] = random.randint(0, 2)
            car[1] = lanes[car[0]]
            car[2] = random.randint(-300, -100)
            car[3] = random.randint(4, 8)
            score += 1

        # Столкновение
        if player_rect.colliderect(car_rect):
            print("Game Over! Score:", score)
            running = False

    # Счёт
    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()