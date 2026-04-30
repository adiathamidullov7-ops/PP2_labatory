import pygame, sys, datetime
from tools import draw_shape, flood_fill

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("TSIS 2 Paint")
clk = pygame.time.Clock()
fnt = pygame.font.SysFont("Verdana", 14)
text_fnt = pygame.font.SysFont("Arial", 32)

surf = pygame.Surface((w, h))
surf.fill((255, 255, 255))

cc = (0, 0, 0)
tool = "brush"
size = 5
flag = False
x1, y1 = 0, 0
last_x, last_y = 0, 0

is_typing = False
text_input = ""
text_pos = (0, 0)

# 🎨 цвета (остаются слева сверху)
colors_gui = [
    (pygame.Rect(10, 10, 30, 30), (0, 0, 0)),
    (pygame.Rect(50, 10, 30, 30), (255, 0, 0)),
    (pygame.Rect(90, 10, 30, 30), (0, 255, 0)),
    (pygame.Rect(130, 10, 30, 30), (0, 0, 255)),
    (pygame.Rect(170, 10, 30, 30), (255, 255, 0)),
    (pygame.Rect(210, 10, 30, 30), (255, 105, 180)),
    (pygame.Rect(250, 10, 30, 30), (128, 0, 128)),
    (pygame.Rect(290, 10, 30, 30), (128, 128, 128))
]

# 🧰 ВСЕ КНОПКИ В ПРАВОМ ВЕРХНЕМ УГЛУ
tools_gui = [
    (pygame.Rect(720, 10, 70, 25), "brush"),
    (pygame.Rect(720, 40, 70, 25), "square"),
    (pygame.Rect(720, 70, 70, 25), "eraser"),
    (pygame.Rect(720, 100, 70, 25), "r_tri"),
    (pygame.Rect(720, 130, 70, 25), "eq_tri"),
    (pygame.Rect(720, 160, 70, 25), "rhomb"),
    (pygame.Rect(720, 190, 70, 25), "rect"),
    (pygame.Rect(720, 220, 70, 25), "circle"),
    (pygame.Rect(720, 250, 70, 25), "line"),
    (pygame.Rect(720, 280, 70, 25), "fill"),
    (pygame.Rect(720, 310, 70, 25), "text")
]


def render_ui():
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, w, 80))

    # цвета
    for r, c in colors_gui:
        pygame.draw.rect(screen, c, r)
        if c == cc:
            pygame.draw.rect(screen, (255, 255, 255), r, 2)

    # панель инструментов справа сверху
    for r, t in tools_gui:
        bg = (160, 160, 160) if t == tool else (110, 110, 110)
        pygame.draw.rect(screen, bg, r)

        txt = fnt.render(t, True, (255, 255, 255))
        screen.blit(txt, txt.get_rect(center=r.center))

    info = fnt.render(f"Size: {size} | Ctrl+S save", True, (50, 50, 50))
    screen.blit(info, (10, 50))


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        elif e.type == pygame.KEYDOWN:
            if is_typing:
                if e.key == pygame.K_RETURN:
                    txt = text_fnt.render(text_input, True, cc)
                    surf.blit(txt, text_pos)
                    is_typing = False
                    text_input = ""
                elif e.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += e.unicode
            else:
                if e.key == pygame.K_1:
                    size = 2
                elif e.key == pygame.K_2:
                    size = 5
                elif e.key == pygame.K_3:
                    size = 10

                elif e.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    pygame.image.save(surf, f"canvas_{name}.png")
                    print("Saved:", name)

        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:

                # 🎨 цвета
                if e.pos[1] < 80:
                    for r, c in colors_gui:
                        if r.collidepoint(e.pos):
                            cc = c

                # 🧰 инструменты справа
                for r, t in tools_gui:
                    if r.collidepoint(e.pos):
                        tool = t

                # 🎯 холст
                if e.pos[1] >= 80:
                    if tool == "fill":
                        flood_fill(surf, e.pos, cc)

                    elif tool == "text":
                        is_typing = True
                        text_input = ""
                        text_pos = e.pos

                    else:
                        flag = True
                        x1, y1 = e.pos
                        last_x, last_y = e.pos

        elif e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1 and flag:
                flag = False
                if tool not in ["brush", "eraser"]:
                    draw_shape(surf, tool, cc, x1, y1, e.pos[0], e.pos[1], size)

        elif e.type == pygame.MOUSEMOTION:
            if flag:
                if tool == "brush":
                    pygame.draw.line(surf, cc, (last_x, last_y), e.pos, size)
                    last_x, last_y = e.pos

                elif tool == "eraser":
                    pygame.draw.line(surf, (255, 255, 255), (last_x, last_y), e.pos, size * 4)
                    last_x, last_y = e.pos

    screen.blit(surf, (0, 0))

    if flag and tool not in ["brush", "eraser"]:
        mx, my = pygame.mouse.get_pos()
        draw_shape(screen, tool, cc, x1, y1, mx, my, size)

    if is_typing:
        txt = text_fnt.render(text_input + "|", True, cc)
        screen.blit(txt, text_pos)

    render_ui()

    pygame.display.update()
    clk.tick(120)