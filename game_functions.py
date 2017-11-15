import sys
import pygame

def check_events():
	for event in pygame.event.get():
            if event.type == pygame.QUIT: #表示单击游戏窗口的关闭按钮
                sys.exit()