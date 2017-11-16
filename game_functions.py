import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 表示单击游戏窗口的关闭按钮
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  #注意这里不是event.type, 而是event.key
                # 向右移动飞船
                # ship.rect.centerx += 1
                ship.moving_right  = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    '''更新屏幕的图像，并切换到新屏幕'''

    screen.fill(ai_settings.bg_color)  # 用背景色填充屏幕，每次循环都重绘屏幕
    ship.blitme()

    pygame.display.flip()  # 让最近绘制的屏幕可见，并擦去旧屏幕