import pygame , sys, random, time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Rain")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
raindrop_spawn_time = 0
mike_image = pygame.image.load("images/Mike.png").convert()
mike_umbrella_image = pygame.image.load("images/Mike_umbrella.png").convert()
cloud_image = pygame.image.load("images/cloud.png").convert()
lase_hit_time = 0

class Raindrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5,18)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > 800

    def draw(self):
        pygame.draw.line(screen,(0,0,0),(self.x,self.y),(self.x,self.y+5),1)

class Mike:
    def __init__(self):
        self.x = 300
        self.y = 400

    def draw(self):
        if time.time() > lase_hit_time+1:
            screen.blit(mike_image,(self.x, self.y))
        else:
            screen.blit(mike_umbrella_image,(self.x, self.y))
    
    def hit_by(self,raindrop):
        return pygame.Rect(self.x, self.y,170,192).collidepoint((raindrop.x,raindrop.y))

class Cloud:
    def __init__(self):
        self.x = 300
        self.y = 50

    def draw(self):
        screen.blit(cloud_image,(self.x, self.y))

    def rain(self):
        for i in range(10):
            raindrops.append(Raindrop(random.randint(self.x, self.x+300),self.y+100))

    def move(self):
        if pressed_key[K_RIGHT]:
            self.x +=1
        if pressed_key[K_LEFT]:
            self.x -=1

raindrops = []
mike = Mike()
cloud = Cloud()

while 1:
    clock.tick(60) #초당 60 frame
    for event in pygame.event.get(): #큐에 저장된 마우스, 키보드 명령을 저장한다.
        if event.type == pygame.QUIT: #이벤트의 타입 확인
            sys.exit()

    pressed_key = pygame.key.get_pressed()

    #raindrops.append(Raindrop())
    screen.fill((255,255,255))
    mike.draw()
    cloud.draw()
    cloud.rain()
    cloud.move()

    """for raindrop in raindrops:
        raindrop.move()
        raindrop.draw()
    """

    i = 0
    while i < len(raindrops):
        raindrops[i].move()
        raindrops[i].draw()
        flag = False
        if raindrops[i].off_screen():
            del raindrops[i]
            i -= 1
            flag = True
        if mike.hit_by(raindrops[i]):
            del raindrops[i]
            flag = True
            lase_hit_time = time.time()
            i -= 1
        if flag:
            del raindrops[i]
            i -= 1
        i += 1

    pygame.display.update()
