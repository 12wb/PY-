import pygame
import sys

pygame.init()  # 载入游戏引擎
size = width,height=640,480  # 设置一个窗口
# screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((640,480))  # 因为size为元组所以要再添加一个括号
color = (0,0,0)
ball = pygame.image.load(r'D:/test.png')
ballrect = ball.get_rect()  # 对象有效范围矩阵
spend = [5,1]  # x,y轴上移动距离
clock = pygame.time.Clock()  # 计时器实例


# 运行后窗口会一闪而过，为什么呢？因为帧率为0

# 无限循环，保证一直都有输出，窗口不会关闭
while True:
    clock.tick(30)  # 计时器实现帧率
    for event in pygame.event.get():  # 检查事件
        if event.type == pygame.QUIT:  # 监控窗口按键，如果QUIT为小写，则不能进行窗口关闭
            sys.exit()

    ballrect = ballrect.move(spend)  # 有效矩阵移动spend
    if ballrect.left<0 or ballrect.right>width:  # x轴碰到窗口
        spend[0]=-spend[0]  # 那么方向可改
    if ballrect.top<0 or ballrect.bottom>height:
        spend[1] = -spend[1]

    screen.fill(color)  # 填充背景色
    screen.blit(ball,ballrect)  # 将对象和有效范围，进入窗口
    pygame.display.flip()  # 更新全部显示

pygame.quit

