import pygame

pygame.init()





pygame.init()

FPS = 60

SCREEN_WIDTH =1000
SCREEN_HEIGHT =800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

running = True

dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
destination = pygame.Vector2(screen.get_width()/3,screen.get_height()/3)
destination_2= pygame.Vector2(9,1)
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.draw.circle(screen, "red", player_pos, 40)
    player_pos += dt*300*(player_pos-destination).normalize()



    pygame.display.flip()


    dt = clock.tick(FPS) / 1000

pygame.quit()
