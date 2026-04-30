import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
YELLOW = (255, 215, 0)

ROAD_LEFT = 50
ROAD_WIDTH = 300

lane_width = ROAD_WIDTH // 3
lanes = [
    ROAD_LEFT + lane_width // 2 - 25,
    ROAD_LEFT + lane_width + lane_width // 2 - 25,
    ROAD_LEFT + lane_width * 2 + lane_width // 2 - 25
]

player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 120
player_speed = 6

# CARS
traffic = []
for i in range(3):
    lane = random.randint(0, 2)
    x = lanes[lane]
    y = random.randint(-600, -100)
    speed = random.randint(4, 7)
    traffic.append([lane, x, y, speed])

# COINS
coins = []
for i in range(2):
    lane = random.randint(0, 2)
    x = lanes[lane] + 15
    y = random.randint(-600, -100)
    speed = 5
    coins.append([lane, x, y, speed])

score = 0
coin_score = 0

font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    # MOMETS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

   
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    
    player_x = max(ROAD_LEFT, min(player_x, ROAD_LEFT + ROAD_WIDTH - player_width))

    # ROAD
    pygame.draw.rect(screen, (60, 60, 60), (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

    
    for x in [ROAD_LEFT + lane_width, ROAD_LEFT + lane_width * 2]:
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, WHITE, (x, y, 4, 20))

    # PLAYER
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, RED, player_rect)

    #        TRAFFIC
    for car in traffic:
        lane, x, y, speed = car

        car_rect = pygame.Rect(x, y, 50, 90)
        pygame.draw.rect(screen, BLUE, car_rect)

        car[2] += speed

        if car[2] > HEIGHT:
            car[0] = random.randint(0, 2)
            car[1] = lanes[car[0]]
            car[2] = random.randint(-300, -100)
            car[3] = random.randint(4, 8)
            score += 1

        if player_rect.colliderect(car_rect):
            print("Game Over! Score:", score, "Coins:", coin_score)
            running = False

    # COINS logic
    for coin in coins:
        lane, x, y, speed = coin

        coin_rect = pygame.Rect(x, y, 20, 20)
        pygame.draw.ellipse(screen, YELLOW, coin_rect)

        coin[2] += speed

        if coin[2] > HEIGHT:
            coin[0] = random.randint(0, 2)
            coin[1] = lanes[coin[0]] + 15
            coin[2] = random.randint(-300, -100)

        if player_rect.colliderect(coin_rect):
            coin_score += 1
            coin[0] = random.randint(0, 2)
            coin[1] = lanes[coin[0]] + 15
            coin[2] = random.randint(-300, -100)

    # text coins and score
    text1 = font.render(f"Score: {score}", True, GREEN)
    text2 = font.render(f"Coins: {coin_score}", True, YELLOW)

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 50))

    pygame.display.update()

pygame.quit()