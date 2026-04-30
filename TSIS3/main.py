import pygame
import sys

from ui import show_menu
from sound import SoundManager
from racer import run_game

pygame.init()

# ===================== SCREEN =====================
screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption("Traffic Racer")

# ===================== SOUND =====================
sound = SoundManager()

# ===================== MENU =====================
sound.play_menu_music()
show_menu(screen)

# если игрок закрыл окно в меню
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

# ===================== GAME START =====================
sound.play_game_music()
run_game(screen)