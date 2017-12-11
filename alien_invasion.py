# -*- coding:utf-8 -*-

# import sys  #为退出游戏使用 , commented due to move to module game_function.py
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()  #初始化背景设置
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200,600))  # 创建一个名为screen的显示窗口，元组指定游戏窗口的大小
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))  # 创建一个名为screen的显示窗口，元组指定游戏窗口的大小

    pygame.display.set_caption("Alien Invasion")
 
    # bg_color = (230, 230, 230) #设置背景色

    #创建一艘飞船
    ship = Ship(ai_settings, screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT: #表示单击游戏窗口的关闭按钮
        #         sys.exit()
        
        #将以上监控事件动作放到game_funcitons.py中
        # gf.check_events(ship)
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        # bullets.update()

        # #删除已经消失的子弹
        # for bullet in bullets.copy():
        # 	if bullet.rect.bottom <= 0:
        # 		bullets.remove(bullet)
        # print(len(bullets))  # 用来检查子弹有没有被删除掉  #调试使用，之后删除这条，否则影响速度

        # screen.fill(bg_color)  # 用背景色填充屏幕，每次循环都重绘屏幕
        # screen.fill(ai_settings.bg_color)  # 用背景色填充屏幕，每次循环都重绘屏幕
        # ship.blitme()
        #
        # pygame.display.flip() # 让最近绘制的屏幕可见，并擦去旧屏幕
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()



