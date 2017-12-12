import sys
import pygame
from bullet import Bullet
from alien import Alien


# def check_keydown_events(event, ship):
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''响应按键按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

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
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''更新屏幕的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)  # 用背景色填充屏幕，每次循环都重绘屏幕
    
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)

    pygame.display.flip()  # 让最近绘制的屏幕可见，并擦去旧屏幕

def update_bullets(bullets):
    """更新子弹位置，并删除已经消失的子弹"""
    bullets.update()

    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没到达极限，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
    #创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    '''计算每行可容纳的外星人数量'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_aliens_y(ai_settings,ship_height, alien_height):
    '''计算屏幕可以容纳多少行的外星人'''
    available_space_y = (ai_settings.screen_height - 
                                (3 * alien_height) - ship_height) #计算公式用挂号括起来，确保每行不超过79字符
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return number_aliens_y

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''创建第一个外星人并将其加入当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可以容纳多少个外星人
    #外星人间距为外星人宽度
    alien =  Alien(ai_settings, screen)  #创建一个外星人的实例
    # alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_aliens_y(ai_settings, ship.rect.height, alien.rect.height)

    #创建第一个外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        
def update_aliens(aliens):
    '''更新外星人群中所有外星人的位置'''
    aliens.update()
