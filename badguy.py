import pygame, sys, random, time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640,650))
last_badguy_spawn_time = 0
score = 0
font = pygame.font.Font(None,20)

badguy_image = pygame.image.load("images/badguy.png").convert()
badguy_image.set_colorkey((0,0,0))
fighter_image = pygame.image.load("images/fighter.png").convert()
fighter_image.set_colorkey((255,255,255))
missile_image = pygame.image.load("images/missile.png").convert()
missile_image.set_colorkey((255,255,255))
GAME_OVER = pygame.image.load("images/gameover.png").convert()

screen.blit(font.render(str(shots),True,(255,255,255)),(266,320))
screen.blit(font.render(str(score),True,(255,255,255)),(266,348))
screen.blit(font.render(str(hits),True,(255,255,255)),(400,320))
screen.blit(font.render(str(misss),True,(255,255,255)),(400,337))
if shots == 0:
    screen.blit(font.render("--",True,(255,255,255)),(400,357))
else:
    screen.blit(font.render("{:.1f}%".format(100*hits/shots),True,(255,255,255)),(400,357))

#=============================================================================================================

class Badguy:
    def __init__(self):
        self.x = random.randint(0,570)
        self.y = -100
        self.dy = random.randint(2,6)           #y 가속값
        self.dx = random.choice((-1,1)*self.dy) #x 가속값
    def move(수
            i -= 1
        i += 1
    i = 0
    while i < len(badguys):
        j = 0
        while j < len(missiles):
            if badguys[i].touching(missiles[j]):
                badguy[i].score()        #badguy가 touch될때마다 score가 +10
                hits += 1                #badguy를 맞힌횟수
                del badguys[i]
                del missiles[j]
                i -= 1
                break
            j += 1
        i += 1

    screen.blit(font.render("Score: " + str(score), True,(255,255,255)),(5,5))    #font.render함수(출력값, antialiasing,text color, 위치

    for badguy in badguys:
        if fighter.hiy_by(badguy):
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                pygame.display.update()
                
    pygame.display.update()
