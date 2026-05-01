import pygame

def show_menu(screen):
    WIDTH, HEIGHT = screen.get_size()

    font = pygame.font.SysFont("Arial", 40)
    small_font = pygame.font.SysFont("Arial", 25)

    # ===================== LOAD LOGO =====================
    logo = pygame.image.load(r"C:\Users\adiat\Music\pp2_adia\TSIS3\musics\NFS_MW.png")
    logo_width = int(WIDTH * 0.9)
    logo_height = int(HEIGHT * 0.4)
    logo = pygame.transform.scale(logo, (logo_width, logo_height))
    logo_rect = logo.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    # ===================== MUSIC =====================
    pygame.mixer.music.load(r"C:\Users\adiat\Music\pp2_adia\TSIS3\musics\menu.mp3")
    pygame.mixer.music.play(-1)  

    # ===================== INPUT =====================
    player_name = ""
    active = True

    input_box = pygame.Rect(WIDTH//2 - 150, HEIGHT - 200, 300, 40)
    color_inactive = (100, 100, 100)
    color_active = (255, 255, 255)
    color = color_active

    # ===================== LOOP =====================
    while True:
        screen.fill((0, 0, 0))

        # title
        title = font.render("TRAFFIC RACER", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

        # logo
        screen.blit(logo, logo_rect)

        # input label
        label = small_font.render("Enter your name:", True, (255, 255, 255))
        screen.blit(label, (WIDTH // 2 - label.get_width() // 2, HEIGHT - 250))

        # input box
        pygame.draw.rect(screen, color, input_box, 2)

        name_surface = small_font.render(player_name, True, (255, 255, 255))
        screen.blit(name_surface, (input_box.x + 5, input_box.y + 5))

        # start text
        start = small_font.render("Press ENTER to Start", True, (255, 200, 0))
        screen.blit(start, (WIDTH // 2 - start.get_width() // 2, HEIGHT - 120))

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return None

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    if player_name.strip() != "":
                        pygame.mixer.music.stop()
                        return player_name

                elif e.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]

                else:
                    if len(player_name) < 15:
                        player_name += e.unicode