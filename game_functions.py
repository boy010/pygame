import sys
import pygame
from bullet import Bullet


# def check_keydown_events(event, ship):
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''响应按键按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
    	#创建一颗子弹，并将其加入到编组bullets中
    	new_bullet = Bullet(ai_settings, screen, ship)
    	bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''响应按键松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 表示单击游戏窗口的关闭按钮
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            # if event.key == pygame.K_RIGHT:  #注意这里不是event.type, 而是event.key
            #     # 向右移动飞船
            #     # ship.rect.centerx += 1
            #     ship.moving_right  = True
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    '''更新屏幕的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)  # 用背景色填充屏幕，每次循环都重绘屏幕
    
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
    	bullet.draw_bullet()
    ship.blitme()

    pygame.display.flip()  # 让最近绘制的屏幕可见，并擦去旧屏幕