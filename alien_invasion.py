# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
#from alien import Alien   
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()  #初始化背景设置
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 创建一个名为screen的显示窗口，元组指定游戏窗口的大小
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings, screen)

    # #创建一个外星人
    # alien = Alien(ai_settings, screen)  #移动到create_fleet()函数中了

    #创建一个用于存储子弹的编组和一个外星人编组
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()



