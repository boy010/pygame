# -*- coding:utf-8 -*-

import sys  #为退出游戏使用
import pygame

def run_game():
	#初始化游戏并创建一个屏幕对象
    pygame.init()  #初始化背景设置
    screen = pygame.display.set_mode((1200,600))  # 创建一个名为screen的显示窗口，元组指定游戏窗口的大小
    pygame.display.set_caption("Alien Invasion")
 
    bg_color = (230, 230, 230) #set background color:

    # 开始游戏的主循环
    while True:
    	#监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #表示单击游戏窗口的关闭按钮
                sys.exit()

        screen.fill(bg_color)  # 用背景色填充屏幕，每次循环都重绘屏幕

        pygame.display.flip() # 让最近绘制的屏幕可见，并擦去旧屏幕

run_game()



