import pygame

pygame.init()
pygame.display.set_caption('Battle Cats Animation Viewer')
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 4)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    print(clock.tick(60))

pygame.quit()