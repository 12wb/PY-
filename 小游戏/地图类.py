import pygame
from pygame.locals import *  # 导入pygame常量
class MyMap():
    def __init__(self,x,y):  # 构造函数
        self.bg=pygame.image.load('image/bg.png').convert_alpha()  # 进行图形判断，将背景与其相关的图片透明化
        self.x=x
        self.y=y


    def map_rolling(self):  # 滚动
        if self.x<-790:
            self.x=800
        else:
            self.x-=5  # 每帧以5个像素，表示像素移动的距离

        def map_update(self):
            SCREEN.blit(self.bg,(self.x,self.y))