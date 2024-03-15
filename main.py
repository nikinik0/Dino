import pygame
import random
from math import sqrt
from time import sleep

pygame.init()
screen = pygame.display.set_mode((900,400))
pygame.display.set_caption("DINO-GAME")
clock = pygame.time.Clock()
FPS = 60
slow = 10
running = True
my_font = pygame.font.SysFont('arial', 20) 
my_font2 = pygame.font.SysFont('arial', 30) 
score = None
score_max = 0
flag = False
slow2 = 30
class Cloud:
    def __init__(self,img,x,y,speed):
        self.img = img
        self.x = x
        self.y = y
        self.speed = speed
    def show(self,j=True):
        if j:
            self.x-=self.speed
            screen.blit(self.img,(self.x,self.y))
        else:
            screen.blit(self.img,(self.x,self.y))

class Bird:
    def __init__(self,img,x,y,speed):
        self.img = img
        self.x = x
        self.y = y
        self.speed = speed
        self.iter = 0
    def show(self,j=True):
        if j:
            self.x-=self.speed
            self.iter+=1
            sprit = self.iter // slow2 % 2
            screen.blit(self.img[sprit],(self.x,self.y))
        else:
            sprit = self.iter // slow2 % 2
            screen.blit(self.img[sprit],(self.x,self.y))
            


class Kaktus:
    def __init__(self,img, x,y):
        self.img = img
        self.x = x+10
        self.y = y
        self.width = img.get_width()
        self.height = img.get_width()
    def show(self,j=True):
        if j: self.x-=5
        screen.blit(self.img,(self.x,self.y))
   
class Player:
    def __init__(self,img, x, y):
        self.img = img
        self.x = x + 10
        self.y = y + 250
        self.up = False
        self.up_iter = 0
        self.iter = 0
        self.score = 0
        self.width = img[0].get_width()
        self.height = img[0].get_width()
        self.game = 1
        
    def move_up(self):
        self.up = True
        self.up_iter = 0
    def show(self,j=True):
        if not j:
            img = self.img[2]
            screen.blit(img,(self.x,self.y))
        else:
            if self.up:
                self.up_iter+=1
                if 1 <= self.up_iter <= 40:
                    self.y-= 6
                if 40 <= self.up_iter <= 80:
                    self.y+= 6
                if self.up_iter == 80: self.up = False
            else:
                self.y = 250
                self.up = False            
            self.iter+=1
            if self.iter // slow % 2 == 0: img = self.img[0]
            if self.iter // slow % 2 == 1: img = self.img[1]
            self.score+=1
            scor = my_font.render(f'Счёт: {self.score}', True, (0,0,0))
            screen.blit(scor,(800,30))
            if self.up == True: img = self.img[2]
            screen.blit(img,(self.x,self.y))
            for i in cact:
                if not self.win(i): self.game = 0

    def win(self,kaktus): # True - победили кактусы
        if ((kaktus.x - self.width <= self.x <= kaktus.x + (kaktus.width-30)) and (kaktus.y - self.height <= self.y <= kaktus.y + (kaktus.height-25))): return False
        else: return True

        

bg = pygame.image.load('Fon.png')
dino0 = pygame.image.load('dino0.png')
dino1 = pygame.image.load('dino1.png')
dino2 = pygame.image.load('dino2.png')
kaktus1 = pygame.image.load("Kaktus_1.png")
kaktus2 = pygame.image.load("Kaktus_2.png")
kaktus3 = pygame.image.load("Kaktus_3.png")
kaktus4 = pygame.image.load("Kaktus_4.png")
kaktus5 = pygame.image.load("Kaktus_5.png")
kaktus6 = pygame.image.load("Kaktus_6.png")
kaktus7 = pygame.image.load("Kaktus_7.png")
reload = pygame.image.load("reload.png")
esc = pygame.image.load("esc.png")
cloud = pygame.image.load("cloud.png")
dinop = [dino0,dino1,dino2]
dino = Player(dinop,0,0)
bird1 = pygame.image.load("bird1.png")
bird2 = pygame.image.load("bird2.png")
icon = pygame.image.load("icon.png")
birdp = [bird1,bird2]
pygame.display.set_icon(icon)
cact = []
flag2 = False
clouds = []
for i in range(500):
    r = random.randint(1,100)
    rr = random.randint(10,100)
    rrr = random.randint(1,4)
    c = Cloud(cloud,i*800+r,rr,rrr)
    clouds.append(c)

birds = []
for i in range(500):
    r = random.randint(1,100)
    rr = random.randint(10,100)
    rrr = random.randint(1,4)
    b = Bird(birdp,i*800+r,rr,rrr)
    birds.append(b)

for i in range(3000):
    r = random.randint(1,100)
    rr = random.randint(1,7)
    y = 250
    if rr == 1: kaktus = kaktus1
    if rr == 2: kaktus = kaktus2
    if rr == 3: kaktus = kaktus3
    if rr == 4: kaktus = kaktus4
    if rr == 5:
        kaktus = kaktus5
        y = 272
    if rr == 6:
        kaktus = kaktus6
        y = 272
    if rr == 7:
        kaktus = kaktus7
        y = 272
    
    k = Kaktus(kaktus,i*600+r,y)
    cact.append(k)
cact.pop(0)
cact.pop(0)
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()  #Получаем координаты места нажатия
                flag = True  #На кнопку нажали
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if dino.game == 2: dino.game = 1
                elif dino.game == 1: dino.game = 2
    #Обновление значений переменных


    if dino.game == 0: 
        screen.fill((255,255,255))
        if score is None:
            score = dino.score
            if score_max < score: score_max = score
            sc = my_font2.render(f'Счёт: {score}', True, (0,0,0))
            sc_max = my_font2.render(f'Максимальный счёт: {score_max}', True, (0,0,0))
        screen.blit(sc,(430,150))
        screen.blit(sc_max,(375,100))
        screen.blit(reload, (450,200))
        if flag == True: #Начинаем обработку. Проверяем координаты нажатия
            if (450 <= pos[0] <= 450 + 60 and 200 <= pos[1] <= 200 + 60):
                dino = Player(dinop,0,0)
                cact = []
                for i in range(3000):
                    r = random.randint(1,100)
                    rr = random.randint(1,7)
                    y = 250
                    if rr == 1: kaktus = kaktus1
                    if rr == 2: kaktus = kaktus2
                    if rr == 3: kaktus = kaktus3
                    if rr == 4: kaktus = kaktus4
                    if rr == 5:
                        kaktus = kaktus5
                        y = 272
                    if rr == 6:
                        kaktus = kaktus6
                        y = 272
                    if rr == 7:
                        kaktus = kaktus7
                        y = 272
                    
                    k = Kaktus(kaktus,i*600+r,y)
                    cact.append(k)
                cact.pop(0)
                cact.pop(0)
                score = None
                flag = False #Завершаем обработку
    if dino.game == 1:
        if pygame.key.get_pressed() [pygame.K_SPACE] and dino.up == False:
            dino.move_up()

        screen.fill((255,255,255))
        screen.blit(bg, (0,338))
        for i in clouds:
            i.show()
        for i in cact:
            i.show()
        for i in birds:
            i.show()
        dino.show()
    if dino.game == 2:
        screen.fill((255,255,255))
        screen.blit(bg, (0,338))
        for i in clouds:
            i.show(False)
        for i in cact:
            i.show(False)
        for i in birds:
            i.show(False)
        dino.show(False)
        screen.blit(esc,(400,150))

        


    pygame.display.flip()

sleep(2)
pygame.quit()  