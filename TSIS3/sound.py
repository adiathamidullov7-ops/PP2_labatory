import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.current = None

    def play_menu_music(self):
        self._play(r"C:\Users\adiat\Music\pp2_adia\TSIS3\musics\menu.mp3")

    def play_game_music(self):
        self._play(r"C:\Users\adiat\Music\pp2_adia\TSIS3\musics\assetsgame.mp3")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current = None

    def _play(self, path):
        if self.current == path:
            return  # уже играет

        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)  # loop
        self.current = path