import pygame
import Screen_1
import Screen_2
import Screen_3

pygame.init()
# 设置窗体宽和高
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
# 设置窗体标题
SCREEN_TITLE = "Flappy Bird"
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(SCREEN_TITLE)
pygame.mouse.set_visible(True)

if __name__ == '__main__':
    game = Screen_1.main(screen)