import pygame
from  pygame.locals import * #导入pygame中常量

SCREENWIDTH=822
SCREENHEIGHT=260
FPS=30

#定义背景对象
class MyMap():
    def __init__(self, x, y):
        self.bg = pygame.image.load('image/bg.png').convert_alpha()
        self.x = x
        self.y = y

    def map_rolling(self):
        if self.x < -790:
            self.x = 800
        else:
            self.x -= 5

    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


#恐龙类
from itertools import cycle
class Dinosaur():
    def __init__(self):
        #初始化恐龙图片的矩阵
        self.rect=pygame.Rect(0,0,0,0)
        self.jumpState=False#状态
        self.jumpHeight=130#高度
        self.lowest_y=140#步行高度
        self.jumpValue=0#跳跃速度
        #加载图片
        self.dinosaurIndex=0
        self.dinosaurIndexGen=cycle([0,1,2])
        self.dinosaur_img=(
            pygame.image.load('image/dinosaur1.png').convert_alpha(),
            pygame.image.load('image/dinosaur2.png').convert_alpha(),
            pygame.image.load('image/dinosaur3.png').convert_alpha(),
        )
        self.jump_audio=pygame.mixer.Sound('audio/jump.wav')
        self.rect.size=self.dinosaur_img[0].get_size()
        self.x=50
        self.y=self.lowest_y
        self.rect.topleft=(self.x,self.y)

    def jump(self):
        self.jumpState = True

    def move(self):
        if self.jumpState:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False #关闭跳跃状态

    def draw_dinosaur(self):
        #匹配恐龙动图
        dinosaurIndex=next(self.dinosaurIndexGen)
        SCREEN.blit(self.dinosaur_img[dinosaurIndex],
                    (self.x,self.rect.y))



#障碍物类
import random
class Obstacle():
    def __init__(self):
        self.rect=pygame.Rect(0,0,0,0)
        self.stone=pygame.image.load('image/stone.png').convert_alpha()
        self.cacti=pygame.image.load('image/cacti.png').convert_alpha()
        r=random.randint(0,1)
        if r==0:
            self.image=self.stone
        else:
            self.image=self.cacti
        self.rect.size=self.image.get_size()
        self.width,self.height=self.rect.size
        self.x=800
        self.y=200-(self.height/2)
        self.rect.center=(self.x,self.y)

    def obstacle_move(self):
        self.rect.x -= 5

    def draw_obstacle(self):
        SCREEN.blit(self.image,(self.rect.x,self.rect.y))

#游戏结束方法：
def game_over():
    pass



def mainGame():
    over=False
    global SCREEN,FPSCLOCK
    pygame.init()#初始化
    FPSCLOCK=pygame.time.Clock()
    SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('google small game')
    #创建地图
    bg1=MyMap(0,0)
    bg2=MyMap(800,0)
    #创建恐龙对象
    dinosaur=Dinosaur()
    #创建一个障碍物集合
    addObstacleTimer=0
    list=[]



    while True:
        #事件监控
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()

        #单击空格，跳跃
            if event.type==KEYDOWN and event.key == K_SPACE:
                if dinosaur.rect.y >= dinosaur.lowest_y:
                    dinosaur.jump()
                    dinosaur.jump_audio.play()
                if over==True:
                    mainGame()


        if over==False:
            bg1.map_update()#出现
            bg1.map_rolling()#滚动
            bg2.map_update()  # 出现
            bg2.map_rolling()  # 滚动
            dinosaur.move()#恐龙移动
            dinosaur.draw_dinosaur()#显示相应动画

            if addObstacleTimer>=1300:
                r=random.randint(0,100)
                if r > 40:
                    obstacle=Obstacle()
                    list.append(obstacle)
                addObstacleTimer=0


            for i in range(len(list)):
                list[i].obstacle_move()#出现的障碍物移动
                list[i].draw_obstacle()#显示出现的障碍物
                if pygame.sprite.collide_rect(dinosaur,list[i]):
                    over = True
                    game_over()

        addObstacleTimer+=20
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
        mainGame()