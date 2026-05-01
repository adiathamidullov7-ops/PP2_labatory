import pygame
import random
import sys

pygame.init()

# ===================== WINDOW =====================
WIDTH, HEIGHT = 400, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 22)

# ===================== ROAD =====================
ROAD_W = 240
ROAD_X = (WIDTH - ROAD_W) // 2
LANE_W = ROAD_W // 3

# ===================== COLORS =====================
GRASS = (34, 177, 76)
ROAD = (60, 60, 60)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (20, 20, 20)

# ===================== NEW COLORS =====================
BLUE = (0, 120, 255)     # NITRO
ORANGE = (255, 140, 0)   # SHIELD

# ===================== IMAGES =====================
player_img = pygame.image.load(r"C:\Users\adiat\Music\pp2_adia\TSIS3\musics\player_car.png")
traffic_img = pygame.image.load(r"C:\Users\adiat\Music\pp2_adia\TSIS3\musics\traffic_car.png")

player_img = pygame.transform.scale(player_img, (40, 80))
traffic_img = pygame.transform.scale(traffic_img, (40, 80))

# ===================== PLAYER =====================
player = pygame.Rect(ROAD_X + LANE_W, HEIGHT - 120, 40, 80)

base_speed = 6
speed = base_speed

score = 0
timer = 0

cars = []
barriers = []
oil_spots = []
potholes = []

spawn_timer = 0
slow_timer = 0

# ===================== POWERUPS =====================
nitro = False
nitro_timer = 0

shield = False


# ===================== ROAD =====================
def draw_road():
    pygame.draw.rect(screen, ROAD, (ROAD_X, 0, ROAD_W, HEIGHT))

    for i in range(1, 3):
        x = ROAD_X + i * LANE_W
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, WHITE, (x - 2, y, 4, 20))


# ===================== SPAWN =====================
def lane_x(lane):
    return ROAD_X + lane * LANE_W + 10


def spawn_car():
    return pygame.Rect(lane_x(random.randint(0, 2)), -100, 40, 80)


def spawn_barrier():
    return pygame.Rect(lane_x(random.randint(0, 2)), -100, 50, 50)


def spawn_oil():
    return pygame.Rect(lane_x(random.randint(0, 2)), -100, 60, 40)


def spawn_pothole():
    return pygame.Rect(lane_x(random.randint(0, 2)), -100, 50, 30)


# ===================== RESET =====================
def reset():
    global cars, barriers, oil_spots, potholes
    global score, speed, timer, slow_timer
    global nitro, nitro_timer, shield

    cars = []
    barriers = []
    oil_spots = []
    potholes = []

    score = 0
    speed = base_speed
    timer = 0
    slow_timer = 0

    nitro = False
    nitro_timer = 0

    shield = False

    player.x = ROAD_X + LANE_W


# ===================== GAME OVER =====================
def game_over():
    while True:
        screen.fill((0, 0, 0))

        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (120, 250))
        screen.blit(font.render(f"Score: {score}", True, WHITE), (130, 300))
        screen.blit(font.render("R - Restart | ESC - Quit", True, WHITE), (70, 350))

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    reset()
                    return
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


# ===================== SLOW =====================
def apply_slow(amount, duration):
    global speed, slow_timer
    speed = max(3, speed - amount)
    slow_timer = duration


def update_slow():
    global speed, slow_timer

    if slow_timer > 0:
        slow_timer -= 1
    else:
        if speed < base_speed:
            speed += 0.02


# ===================== POWERUPS =====================
def update_powerups():
    global speed, nitro, nitro_timer, shield

    # 🔵 NITRO
    if nitro:
        speed = base_speed + 6
        nitro_timer -= 1
        if nitro_timer <= 0:
            nitro = False

    # вернуть скорость если нет нитро
    if not nitro:
        speed = max(speed, base_speed)


# ===================== MAIN =====================
def run_game(screen):
    global spawn_timer, score, speed, timer
    global nitro, nitro_timer, shield

    reset()

    while True:
        clock.tick(60)
        timer += 1

        screen.fill(GRASS)
        draw_road()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed

        # 🔵 NITRO (SPACE)
        if keys[pygame.K_SPACE] and not nitro:
            nitro = True
            nitro_timer = 120

        # 🟠 SHIELD (SHIFT)
        if keys[pygame.K_LSHIFT] and not shield:
            shield = True

        player.x = max(ROAD_X + 5, min(ROAD_X + ROAD_W - 45, player.x))

        # spawn
        spawn_timer += 1
        if spawn_timer > 45:
            t = random.randint(1, 4)

            if t == 1:
                cars.append(spawn_car())
            elif t == 2:
                barriers.append(spawn_barrier())
            elif t == 3:
                oil_spots.append(spawn_oil())
            else:
                potholes.append(spawn_pothole())

            spawn_timer = 0

        # cars
        for c in cars[:]:
            c.y += speed

            if c.y > HEIGHT:
                cars.remove(c)
                score += 1

            # 🟠 SHIELD LOGIC
            if player.colliderect(c):
                if shield:
                    shield = False   # уничтожается после удара
                    cars.remove(c)
                    score += 2
                    continue
                else:
                    game_over()

            screen.blit(traffic_img, (c.x, c.y))

        # barriers (НЕ ТРОГАЕМ)
        for b in barriers:
            b.y += speed
            pygame.draw.rect(screen, YELLOW, b)

        # oil (НЕ ТРОГАЕМ)
        for o in oil_spots:
            o.y += speed
            pygame.draw.rect(screen, BLACK, o)

        # potholes (НЕ ТРОГАЕМ)
        for p in potholes:
            p.y += speed
            pygame.draw.rect(screen, (80, 80, 80), p)

        # player
        screen.blit(player_img, (player.x, player.y))

        update_slow()
        update_powerups()

        # ===================== UI =====================
        screen.blit(font.render(
            f"Score: {score} Speed: {round(speed,1)}"
            + (" | NITRO" if nitro else "")
            + (" | SHIELD" if shield else ""),
            True, WHITE
        ), (10, 10))

        pygame.display.update()