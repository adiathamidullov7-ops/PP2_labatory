import math
import datetime as dt
from pathlib import Path

import pygame


class MickeyClock:
    def __init__(self, image_path: str, width: int = 900, height: int = 900):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mickey Mouse Clock")

        self.timer = pygame.time.Clock()
        self.running = True

        self.image_path = Path(image_path)
        self.background = self.load_background()

        # Центр часов
        self.center_x = self.width // 2
        self.center_y = self.height // 2

        # Длина стрелок
        self.hour_len = 150
        self.minute_len = 230

        # Цвета
        self.hour_color = (150, 150, 150)
        self.minute_color = (200, 0, 0)
        self.center_color = (0, 0, 0)

    def load_background(self):
        if not self.image_path.exists():
            surface = pygame.Surface((self.width, self.height))
            surface.fill((240, 240, 240))
            return surface

        image = pygame.image.load(str(self.image_path)).convert_alpha()
        image = pygame.transform.smoothscale(image, (self.width, self.height))
        return image

    def get_hand_end(self, angle_deg, length):
        angle_rad = math.radians(angle_deg - 90)
        x = self.center_x + math.cos(angle_rad) * length
        y = self.center_y + math.sin(angle_rad) * length
        return int(x), int(y)

    def draw_clock_hands(self):
        now = dt.datetime.now()

        hour = now.hour % 12
        minute = now.minute
        second = now.second

        # Углы стрелок
        hour_angle = (hour + minute / 60 + second / 3600) * 30
        minute_angle = (minute + second / 60) * 6

        hour_end = self.get_hand_end(hour_angle, self.hour_len)
        minute_end = self.get_hand_end(minute_angle, self.minute_len)

        # Минутная стрелка
        pygame.draw.line(
            self.screen,
            self.minute_color,
            (self.center_x, self.center_y),
            minute_end,
            6
        )

        # Часовая стрелка
        pygame.draw.line(
            self.screen,
            self.hour_color,
            (self.center_x, self.center_y),
            hour_end,
            10
        )

        # Центральная точка
        pygame.draw.circle(
            self.screen,
            self.center_color,
            (self.center_x, self.center_y),
            10
        )

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.background, (0, 0))
            self.draw_clock_hands()

            pygame.display.flip()
            self.timer.tick(60)

        pygame.quit()