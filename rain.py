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
last_hit_time = 0

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
class Mike:
    def __init__(self):
        self.x = 300
        self.y = 400

    def draw(self):
        if time.time() > last_hit_time+1:               #Mike가 1초동안 비를 맞지 않아야 우산이 없어짐
            screen.blit(mike_image,(self.x, self.y))
        else:
            screen.blit(mike_umbrella_image,(self.x, self.y))
    
    def hit_by(self,raindrop):
        return pygame.Rect(self.x, self.y,170,192).collidepoint((raindrop.x,raindrop.y))
    
raindrops = []
mike = Mike()
cloud = Cloud()

while 1:
    clock.tick(60) #초당 60 frame
    for event in pygame.event.get(): #큐에 저장된 마우스, 키보드 명령을 저장한다.
        if event.type == pygame.QUIT: #이벤트의 타입 확인
            sys.exit()

    pressed_key = pygame.key.get_pressed()

    screen.fill((255,255,255))
    mike.draw()
    cloud.draw()
    cloud.rain() #매 frame마다 raindrops list에 Raindrop class 10개 append
    cloud.move()

    i = 0
    while i < len(raindrops): #매 frame마다 10개씩 증가 된 raindrops list 만큼 순환
        raindrops[i].move()   #빗줄기 시작점을 random 만큼 아래로 이동
        raindrops[i].draw()   #빗줄기 그리기
        flag = False
        if raindrops[i].off_screen():   #빗줄기가 스크린 밖으로 나갔는지 체크
            flag = True
        if mike.hit_by(raindrops[i]):   #빗줄기가 Mike와 닫았는지 체크
            flag = True
            last_hit_time = time.time() #last_hit_time을 Mike.draw에 돌려줘서 mike_umbrella_image 불러옴
        if flag:                        #flag가 true인지 체크
            del raindrops[i]            #나갔으면 해당 list삭제
            i -= 1                      #삭제 되어 당겨진 list를 다음에 실행하기 위해 i값 -1
        i += 1                          #빗줄기가 살아있어야 하면 다음 list로 넘어감

    pygame.display.update()             #한 frame 끝내고 다음 frame으로 이동
