import pygame, sys, random, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640,650))
last_badguy_spawn_time = 0

badguy_image = pygame.image.load("images/badguy.png").convert()
badguy_image.set_colorkey((0,0,0))
fighter_image = pygame.image.load("images/fighter.png").convert()
fighter_image.set_colorkey((255,255,255))
missile_image = pygame.image.load("images/missile.png").convert()
missile_image.set_colorkey((255,255,255))

#=============================================================================================================

class Badguy:
    def __init__(self):
        self.x = random.randint(0,570)
        self.y = -100
        self.dy = random.randint(2,6)           #y 가속값
        self.dx = random.choice((-1,1)*self.dy) #x 가속값
    def move(self):                     #badguy 이동
        self.x += self.dx               #x축 이동
        self.dy += 0.1                  #y축 가속
        self.y += self.dy               #y축 이동
        if self.y > 150 and self.y < 250:   #y축 이동에 따른 x값의 변동
            self.x += 5
        if self.y > 250:
            self.x -= 5
    def bounce(self):                   #badguy 벽에 닫으면 반대로 이동
        if self.x < 0 or self.x > 570:  #x축 limit 정하기
            self.dx *= -1
    def draw(self):                     #badguy그리기
        screen.blit(badguy_image,(self.x, self.y))
    def off_screen(self):               #badguy 아래로 떨어지면 지울수 있도록 true 반환
        return self.y > 640
    def touching(self, missile):
        return (self.x+35-missile.x)**2+(self.y+22-missile.y)**2 < 1225
    
class Fighter:
    def __init__(self):
        self.x = 320
    def move(self):
        if pressed_keys[K_LEFT]: #and self.x > 0:
            self.x -= 3
        if pressed_keys[K_RIGHT]: #and self.x < 540:
            self.x += 3
    def draw(self):
        screen.blit(fighter_image,(self.x, 591))
    def fire(self):
        missiles.append(Missile(self.x+50))

class Missile:
    def __init__(self, x):
        self.x = x
        self.y = 591
    def move(self):
        self.y -= 5
    def screen_off(self):
        return self.y < -8
    def draw(self):
        screen.blit(missile_image,(self.x-4,self.y))
#=============================================================================================================

badguys = []
fighter = Fighter()
missiles = []

#=============================================================================================================

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            fighter.fire()
    pressed_keys = pygame.key.get_pressed()             #fighter의 움직임 key 확인

    if time.time() - last_badguy_spawn_time > 0.5:      #badguy spawn time 정하기
        badguys.append(Badguy())
        last_badguy_spawn_time = time.time()

    screen.fill((0,0,0))
    fighter.move()
    fighter.draw()
    #=================================================================
    i = 0
    while i < len(badguys):             #badguy spawn time에 따라 연속적으로 발생
        badguys[i].move()
        badguys[i].bounce()
        badguys[i].draw()
        if badguys[i].off_screen():
            del badguys[i]
            i -= 1
        i += 1
    i = 0
    while i < len(missiles):            #발사된 미사일 이동
        missiles[i].move()
        missiles[i].draw()
        if missiles[i].screen_off():
            del missiles[i]
            i -= 1
        i += 1
    i = 0
    while i < len(badguys):
        j = 0
        while j < len(missiles):
            if badguys[i].touching(missiles[j]):
                del badguys[i]
                del missiles[j]
                i -= 1
                break
            j += 1
        i += 1
    
    pygame.display.update()