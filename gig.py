from random import randint
import pygame as pg
import sys

pg.init()
pg.time.set_timer(pg.USEREVENT,3000)

W= 1920
H=1080
WHITE = (255,255,255)
CARS = ('./cer.png','./re.png','./fre.png')
CARS_SURF = []
sc = pg.display.set_mode((W,H))

for i in range(len(CARS)):
    CARS_SURF.append(pg.image.load(CARS[i]).convert_alpha())
class Car(pg.sprite.Sprite):
    def __init__(self,x,surf,group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)
        self.speed = randint(1,3)
    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            self.kill()
cars = pg.sprite.Group()
Car(randint(1,W),CARS_SURF[randint(0,2)],cars)

# car= Car(randint(1,W), './cer.png')
# car2=Car(randint(1,W),'./re.png')
# car3= Car(randint(1,W),'./fre.png')
# car.image = pg.transform.scale(car.image, (400, 400))
# car3.image = pg.transform.scale(car3.image, (400, 400))
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Car(randint(1,W),CARS_SURF[randint(0,2)],cars)

    sc.fill(WHITE)
    # sc.blit(car.image,car.rect)
    # sc.blit(car2.image, car2.rect)
    # sc.blit(car3.image, car3.rect)
    # pg.display.update()
    # pg.time.delay(20)
    # car.update()
    # car2.update()
    # car3.update()
    pg.display.update()
    cars.draw(sc)
    pg.time.delay(20)
    cars.update()
