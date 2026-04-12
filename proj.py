import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()




class Player:
    def __init__(self,WIGHT,HEIGHT):
        self.player = pygame.Vector2(400, 500)
        self.image = pygame.image.load('../g.png')
        self.image = pygame.transform.scale(self.image, (100, 40))
        self.enemy_square = pygame.Vector2(random.randint(1, 800), random.randint(1, 600))
        self.square_speed = pygame.Vector2(random.choice([-1, 1]) * 200, random.choice([-1, 1]) * 200)
        self.enemy = pygame.Vector2(400, 100)
        self.coin = 0
        self.poc = pygame.Vector2(random.randint(0, WIGHT), random.randint(0, HEIGHT))
        self.speed = int(self.SPEED_PER)
        self.image3 = pygame.image.load('pygame_collisions/pipo-enemy047a2.png')
        self.image4 = pygame.image.load('pygame_collisions/pipo-enemy047a.png')
        self.anim = [seimage3, image4]
        self.anim_timer = 0
        self.anim_frame_speed = 0, 5
    def muvent(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT]:self.player.x -= 400 * dt
        if self.keys[pygame.K_UP]: self.player.y -= 400 * dt
        if self.keys[pygame.K_RIGHT]: self.player.x += 400 * dt
        if self.keys[pygame.K_DOWN]: self.player.y += 400 * dt
        if self.player.distance_to(self.enemy) < 40:
            self.enemy = pygame.Vector2(random.randint(1, 800), random.randint(1, 600))
            self.coin = self.coin + 1
        self.enemy_square += self.square_speed * dt
    def draw(self,screen,dt):
        text_surface = font.render(f'{self.coin}', True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(self.image, self.player)
        screen.blit(image2, self.enemy)
        pygame.draw.rect(screen, (255, 0, 0), (self.enemy_square.x, self.enemy_square.y, 30, 30))
        screen.blit(text_surface, (50, 100))
        frame = self.get_anim_frame(dt)
        blit_pos = (self.poc.x - frame.get_widht() // 2, self.poc.y - frame.get_heihgt() // 2)
        self.bilt(frame, blit_pos)
    def collision(self):
        if self.enemy_square.x <= 0 or self.enemy_square.x >= 780:
            self.square_speed.x *= -1
        if self.enemy_square.y <= 0 or self.enemy_square.y >= 580:
            self.square_speed.y *= -1
        if self.player.distance_to(self.enemy_square) < 30:
            running = False
    def get_animation_frame(self,dt):
        self.anim_timer+= dt
        if self.anim_timer >= self.anim_frame_speed:
            self.frame+= 1
            if self.frame == len(self.anim):
                self.frame = 0
            self.anim_timer = 0
        return self.anim[self.frame]
while running:
    dt = clock.tick(120) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 400 * dt
    if keys[pygame.K_UP]: player.y -= 400 * dt
    if keys[pygame.K_RIGHT]:
        player.x += 400 * dt
    if keys[pygame.K_DOWN]: player.y += 400 * dt
    if player.distance_to(enemy) < 40:
        enemy = pygame.Vector2(random.randint(1, 800), random.randint(1, 600))
        coin = coin + 1
    enemy_square += square_speed * dt
    if enemy_square.x <= 0 or enemy_square.x >= 780:
        square_speed.x *= -1
    if enemy_square.y <= 0 or enemy_square.y >= 580:
        square_speed.y *= -1

    if player.distance_to(enemy_square) < 40:
        running = False
    text_surface = font.render(f'{coin}/10', True, (255, 255, 255))
    if coin >= 10:
        running = False
    screen.fill((0, 0, 0))
    screen.blit(image, player)
    screen.blit(image2, enemy)
    # pygame.draw.circle(screen, (0,200,0), player, 20)    # pygame.draw.circle(screen, (255,255,0), enemy, 20)
    pygame.draw.rect(screen, (255, 0, 0), (enemy_square.x, enemy_square.y, 40, 40))
    screen.blit(text_surface, (50, 100))
    pygame.display.flip()