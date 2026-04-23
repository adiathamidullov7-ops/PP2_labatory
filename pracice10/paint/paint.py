import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App V2")

clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
RED = (220, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 220)
YELLOW = (240, 240, 50)

# Холст
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Настройки
color = BLACK
brush_size = 6
eraser = False
drawing = False

font = pygame.font.SysFont(None, 24)

def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 60))

    # кнопки цветов
    colors = [BLACK, RED, GREEN, BLUE, YELLOW]
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (10 + i * 50, 10, 40, 40))

    # ластик
    pygame.draw.rect(screen, WHITE, (300, 10, 80, 40))
    text = font.render("ERASER", True, BLACK)
    screen.blit(text, (305, 20))

    # очистка
    pygame.draw.rect(screen, (150, 150, 150), (400, 10, 80, 40))
    text2 = font.render("CLEAR", True, BLACK)
    screen.blit(text2, (410, 20))

running = True
while running:
    clock.tick(120)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if y < 60:
                # выбор цвета
                if 10 < x < 50:
                    color = BLACK
                    eraser = False
                elif 60 < x < 100:
                    color = RED
                    eraser = False
                elif 110 < x < 150:
                    color = GREEN
                    eraser = False
                elif 160 < x < 200:
                    color = BLUE
                    eraser = False
                elif 210 < x < 250:
                    color = YELLOW
                    eraser = False

                # ластик
                elif 300 < x < 380:
                    eraser = True

                # очистка
                elif 400 < x < 480:
                    canvas.fill(WHITE)

            else:
                drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    # рисование
    if drawing:
        mx, my = pygame.mouse.get_pos()
        draw_color = WHITE if eraser else color
        pygame.draw.circle(canvas, draw_color, (mx, my), brush_size)

    # вывод
    screen.blit(canvas, (0, 0))
    draw_toolbar()

    pygame.display.update()

pygame.quit()