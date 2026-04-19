import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 32)
beck= pygame.image.load('pygame_collisions/bec.jpg')
class Player:
    alive = True
    SPEED_PER_SEC = 200
    frame = 0
    def __init__(self,pos):
        self.pos = pygame.Vector2(pos)
        self.speed = int(self.SPEED_PER_SEC)

        a = pygame.image.load("pygame_collisions/pipo-enemy047a.png")
        b = pygame.image.load("pygame_collisions/pipo-enemy047a2.png")
        self.frame_ust= pygame.image.load('pygame_collisions/characters.png').convert_alpha()
        self.anim = [a, b]
        self.curret_frame= 0
        self.animation_timer = 0
        self.anim_frame_speed = 5.00
        self.hught=128
        self.wught=736
        self.col= 23
        self.row= 4
        self.frames=[]
        self.frame_w= self.wught // self.col
        self.frame_h= self.hught// self.row
        for i in range(self.col):
            x=i*self.frame_w
            rect= pygame.Rect(x,0,self.frame_w,self.frame_h)
            frame = self.frame_ust.subsurface(rect)
            frame = pygame.transform.smoothscale(frame,(100,100))
            self.frames.append(frame)
    def move(self, keys, dt):
        if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
            self.pos.x -= 600 * dt
        if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
            self.pos.x += 600 * dt
        if keys[pygame.K_UP] and keys[pygame.K_LSHIFT]:
            self.pos.y -= 600 * dt
        if keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT]:
            self.pos.y += 600 * dt
        if keys[pygame.K_LEFT]:
            self.pos.x -= 400 * dt
        if keys[pygame.K_RIGHT]:
            self.pos.x += 400 * dt
        if keys[pygame.K_UP]:
            self.pos.y -= 400 * dt
        if keys[pygame.K_DOWN]:
            self.pos.y += 400 * dt

    def draw_me(self, screen, dt):
        self.curret_frame += self.anim_frame_speed* dt
        if self.curret_frame >=len(self.frames):
            self.curret_frame = 0
        self.drow= self.frames[int(self.curret_frame)]
        screen.blit(self.drow,self.pos)

class Enemy:
    def __init__(self, image):
        self.image = pygame.transform.scale(image, (100, 100))
        self.respawn()

    def respawn(self):
        self.pos = pygame.Vector2(random.randint(1, 800),random.randint(1, 600))

    def draw(self, screen):
        screen.blit(self.image, self.pos)


class MovingSquare:
    def __init__(self):
        self.pos = pygame.Vector2(random.randint(1, 800),random.randint(1, 600))
        self.speed = pygame.Vector2(random.choice([-1, 1]) * 700,random.choice([-1, 1]) * 700)
        self.size = 40
        self.player_img = pygame.image.load('pygame_collisions/pipo-enemy047a2.png')
        self.player_img2 = pygame.image.load('pygame_collisions/pipo-enemy047a.png')
        self.anim = [self.player_img,self.player_img2]
    def update(self, dt):
        self.pos += self.speed * dt

        if self.pos.x <= 0 or self.pos.x >= 1000 - self.size:
            self.speed.x *= -1
        if self.pos.y <= 0 or self.pos.y >= 800 - self.size:
            self.speed.y *= -1

    def draw(self, screen):
        # frame = self.get_anim_frame(dt)
        # bilt_pos= (self.pos.x - frame.get_w)
        self.player_img = pygame.transform.smoothscale(self.player_img,(70,70))
        screen.blit(self.player_img,self.pos)
        # pygame.draw.rect(screen, (255, 0, 0),(self.pos.x, self.pos.y, self.size, self.size))



enemy_img = pygame.image.load('pygame_collisions/d.png')

player = Player((400,300))
enemy = Enemy(enemy_img)
square = MovingSquare()

coin = 0
running = True


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys, dt)

    square.update(dt)

    if player.pos.distance_to(enemy.pos) < 40:
        enemy.respawn()
        coin += 1

    if player.pos.distance_to(square.pos) < 40:
        running = False
    if coin>= 10:
        running= False
    text_surface = font.render(f'10/{coin}', True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(beck, (0, 0))
    player.draw_me(screen,dt)
    enemy.draw(screen)
    square.draw(screen)
    screen.blit(text_surface, (50, 50))

    pygame.display.flip()