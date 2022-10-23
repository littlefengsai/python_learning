import pygame
from plane_sprites import *


pygame.init()

##编写游戏代的代码
##创建英雄
#hero_rect = pygame.Rect(100,500,120,125)
#print("英雄的原点 %d %d" % (hero_rect.x,hero_rect.y))
#print("英雄的尺寸 %d %d" % (hero_rect.width,hero_rect.height))
#print("%d %d" % hero_rect.size)

#创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480,700))

#绘制背景图片
#1.加载图像数据
bg = pygame.image.load("./images/background.png")
#2.blit绘制图像
screen.blit(bg,(0,0))
#3.update更新屏幕显示
pygame.display.update()

#绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
#screen.blit(hero,(150,500))
#pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()

#1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,300,97,124)

#创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)
#创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)


#游戏循环 ->意味着游戏的正式开始
while True:

    #可以指定循环体内部的代码执行的频率
    clock.tick(60)

    ##捕获事件
    #event_list = pygame.event.get()
    #if len(event_list) > 0:
    #    print(event_list)

    #监听事件
    for event in pygame.event.get():
        #判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            #quit卸载所有模块
            pygame.quit()
            #exit()直接终止当前正在执行的程序
            exit() 


    #2.修改飞机的位置
    hero_rect.y -= 1

    #判断飞机的位置
    if hero_rect.bottom <= 0:  #bottom=y+height
        hero_rect.bottom = 700

    #3.调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    #让精灵组调用两个方法
    #update - 让组中的所有精灵更新位置
    enemy_group.update()

    #draw - 在screen上绘制所有的精灵
    enemy_group.draw(screen)

    #4.调用update方法更新图像
    pygame.display.update()

    pass


#print("游戏的代码...")

pygame.quit()




