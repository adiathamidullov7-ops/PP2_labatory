import os
import pygame


class Button:
    def __init__(self, x, y, width, height, text, color=(70, 70, 70), hover_color=(100, 100, 100)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("arial", 28)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2, border_radius=10)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)


class MP3Player:
    def __init__(self, music_folder, screen):
        self.music_folder = music_folder
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        pygame.mixer.init()

        self.font_title = pygame.font.SysFont("arial", 30, bold=True)
        self.font_info = pygame.font.SysFont("arial", 24)

        self.play_button = Button(180, 500, 140, 50, "Play")
        self.stop_button = Button(380, 500, 140, 50, "Stop")
        self.next_button = Button(580, 500, 140, 50, "Next")

        self.tracks = self.load_tracks()
        self.current_track_index = 0
        self.is_playing = False

        self.current_image = None
        if self.tracks:
            self.load_current_track_assets()

    def load_tracks(self):
        tracks = []

        if not os.path.exists(self.music_folder):
            print(f"FILE NOT FOUND: {self.music_folder}")
            return tracks

        for file_name in os.listdir(self.music_folder):
            if file_name.lower().endswith(".mp3"):
                mp3_path = os.path.join(self.music_folder, file_name)
                base_name = os.path.splitext(file_name)[0]

                image_path = None
                for ext in [".png", ".jpg", ".jpeg", ".webp"]:
                    possible_image = os.path.join(self.music_folder, base_name + ext)
                    if os.path.exists(possible_image):
                        image_path = possible_image
                        break

                tracks.append({
                    "title": base_name,
                    "mp3": mp3_path,
                    "image": image_path
                })

        tracks.sort(key=lambda x: x["title"].lower())
        return tracks

    def load_current_track_assets(self):
        if not self.tracks:
            self.current_image = None
            return

        track = self.tracks[self.current_track_index]

        if track["image"] and os.path.exists(track["image"]):
            try:
                image = pygame.image.load(track["image"]).convert_alpha()
                self.current_image = pygame.transform.smoothscale(image, (320, 320))
            except Exception as e:
                print(f"ERROR IMAGINE FILE {track['image']}: {e}")
                self.current_image = None
        else:
            self.current_image = None

    def play(self):
        if not self.tracks:
            return

        track = self.tracks[self.current_track_index]
        try:
            pygame.mixer.music.load(track["mp3"])
            pygame.mixer.music.play()
            self.is_playing = True
        except Exception as e:
            print(f"ERROR {track['mp3']}: {e}")

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.tracks:
            return

        self.current_track_index = (self.current_track_index + 1) % len(self.tracks)
        self.load_current_track_assets()
        self.play()

    def handle_event(self, event):
        if self.play_button.is_clicked(event):
            self.play()

        elif self.stop_button.is_clicked(event):
            self.stop()

        elif self.next_button.is_clicked(event):
            self.next_track()

    def draw(self):
        if not self.tracks:
            no_tracks_text = self.font_title.render("MP3 NOT FOUND", True, (255, 80, 80))
            self.screen.blit(no_tracks_text, (250, 50))
            return

        track = self.tracks[self.current_track_index]

        title_text = self.font_title.render(f"NOW PLAYING: {track['title']}", True, (255, 255, 255))
        self.screen.blit(title_text, (220, 30))

        status = "PLAYING" if self.is_playing and pygame.mixer.music.get_busy() else "STOPPED"
        status_text = self.font_info.render(f"STATUS: {status}", True, (200, 200, 200))
        self.screen.blit(status_text, (360, 80))

        if self.current_image:
            img_rect = self.current_image.get_rect(center=(self.screen_width // 2, 260))
            self.screen.blit(self.current_image, img_rect)
        else:
            placeholder_rect = pygame.Rect(290, 100, 320, 320)
            pygame.draw.rect(self.screen, (60, 60, 60), placeholder_rect, border_radius=12)
            pygame.draw.rect(self.screen, (180, 180, 180), placeholder_rect, 2, border_radius=12)

            no_img_text = self.font_info.render("NO IMAGE", True, (220, 220, 220))
            no_img_rect = no_img_text.get_rect(center=placeholder_rect.center)
            self.screen.blit(no_img_text, no_img_rect)

        self.play_button.draw(self.screen)
        self.stop_button.draw(self.screen)
        self.next_button.draw(self.screen)