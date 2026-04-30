import pygame
black = (0, 0, 0)
white = (255, 255, 255)
pygame.init()
size = (400, 300)
dis = pygame.display.set_mode(size)
pygame.display.set_caption('Zhusup')
game_over = False
x1 = 300
y1 = 300

x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
while not game_over:
    for event in event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.K_s:
            if event.key  == pygame.K_a:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_w:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_s:
                y1_change = 10
                x1_change = 0
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 100] )
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
                
    
                