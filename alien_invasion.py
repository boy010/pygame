# -*- coding:utf-8 -*-

import sys
import pygame

def run_game():
	#初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,600))  # 800 is too big for my screen
    pygame.display.set_caption("Alien Invasion")
 
    bg_color = (230, 230, 230) #set background color:

    # 开始游戏的主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)  # 每次循环都重绘屏幕

        pygame.display.flip() # 让最近绘制的屏幕可见

run_game()



