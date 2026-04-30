import pygame

def show_menu(screen):
    # размер экрана (важно для адаптации)
    WIDTH, HEIGHT = screen.get_size()

    font = pygame.font.SysFont("Arial", 40)
    small_font = pygame.font.SysFont("Arial", 25)

    # ===================== LOAD LOGO =====================
    logo = pygame.image.load(r"C:\Users\adiat\Music\pp2_adia\TSIS3\musics\NFS_MW.png")

    # 🔥 ВАЖНО: масштабируем под экран 400x700
    logo_width = int(WIDTH * 0.9)
    logo_height = int(HEIGHT * 0.4)

    logo = pygame.transform.scale(logo, (logo_width, logo_height))

    logo_rect = logo.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    # ===================== LOOP =====================
    while True:
        screen.fill((0, 0, 0))

        # title
        title = font.render("TRAFFIC RACER", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

        # logo (адаптированная под экран)
        screen.blit(logo, logo_rect)

        # start text
        start = small_font.render("Press SPACE to Start", True, (255, 200, 0))
        screen.blit(start, (WIDTH // 2 - start.get_width() // 2, HEIGHT - 120))

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    return