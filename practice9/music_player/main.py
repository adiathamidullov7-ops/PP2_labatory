import os
import pygame
from player import MP3Player


def main():
    pygame.init()

    WIDTH, HEIGHT = 1200, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame MP3 Player")

    clock = pygame.time.Clock()

 
    music_folder = r"C:\Users\adiat\Music\pp2_adia\practice9\music_player\music"

    player = MP3Player(music_folder, screen)

    running = True
    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            player.handle_event(event)

        player.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()