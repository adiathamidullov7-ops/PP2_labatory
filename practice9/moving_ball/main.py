import pygame
from ball import Ball

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()

    ball = Ball(
        x=WIDTH // 2,
        y=HEIGHT // 2,
        radius=25,
        color=(255, 0, 0),
        screen_width=WIDTH,
        screen_height=HEIGHT,
        step=20,
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move(0, -ball.step)
                elif event.key == pygame.K_DOWN:
                    ball.move(0, ball.step)
                elif event.key == pygame.K_LEFT:
                    ball.move(-ball.step, 0)
                elif event.key == pygame.K_RIGHT:
                    ball.move(ball.step, 0)

        screen.fill(BACKGROUND_COLOR)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()