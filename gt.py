import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
enemy = pygame.Vector2(400,100)
enemy2 = pygame.Vector2(100,300)
player = pygame.Vector2(400, 500)
KOL = pygame.Rect(100, 100, 50, 50)
g= pygame.Rect(200,150,50,50)
coin = 0
running = True
alive= True
SPEED_PER= 200
frame=0
font = pygame.font.SysFont('Arial', 32)
text_surface = font.render(f'{coin}/10', True, (255, 255, 255))
image= pygame.image.load('pygame_collisions/g.png')
image2= pygame.image.load('pygame_collisions/t.png')
image= pygame.transform.scale(image,(100,40))
image2= pygame.transform.scale(image2,(100,40))
image3= pygame.image.load('pygame_collisions/pipo-enemy047a2.png')
image4= pygame.image.load('pygame_collisions/pipo-enemy047a.png')
anim = [image3,image4]
anim_timer= 0
anim_frame_speed= 0,5
flip= pygame.transform.flip(image,False,True)
enemy_square = pygame.Vector2(random.randint(1, 800), random.randint(1, 600))
square_speed = pygame.Vector2(random.choice([-1, 1]) * 200, random.choice([-1, 1]) * 200)
class MOB:
    alive= True
    SPEED_PER= 200
    frame=0
    def __init__(self,WIGHT,HEIGHT):
        self.poc= pygame.Vector2(random.randint(0,WIGHT), random.randint(0,HEIGHT))
        self.speed = int(self.SPEED_PER)
        self.image3 = pygame.image.load('pygame_collisions/pipo-enemy047a2.png')
        self.image4 = pygame.image.load('pygame_collisions/pipo-enemy047a.png')
        self.anim = [image3, image4]
        self.anim_timer = 0
        self.anim_frame_speed = 0, 5
    def draw(self,screen,dt):
        frame = self.get_anim_frame(dt)
        blit_pos =(self.poc.x - frame.get_widht()//2,self.poc.y - frame.get_heihgt()//2)
        self.bilt(frame,blit_pos)
    def get_animation_frame(self,dt):
        self.anim_timer+= dt
        if self.anim_timer >= self.anim_frame_speed
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
        coin = coin+1
    enemy_square += square_speed * dt
    if enemy_square.x <= 0 or enemy_square.x >= 780:
        square_speed.x *= -1
    if enemy_square.y <= 0 or enemy_square.y >= 580:
        square_speed.y *= -1

    if player.distance_to(enemy_square) < 40:
        running = False
    text_surface = font.render(f'{coin}/10', True, (255, 255, 255))
    if coin >= 10:
        running= False
    screen.fill((0,0,0))
    screen.blit(image, player)
    screen.blit(image2, enemy)
    # pygame.draw.circle(screen, (0,200,0), player, 20)    # pygame.draw.circle(screen, (255,255,0), enemy, 20)
    pygame.draw.rect(screen, (255, 0, 0), (enemy_square.x, enemy_square.y, 40, 40))
    screen.blit(text_surface, (50, 100))
    pygame.display.flip()