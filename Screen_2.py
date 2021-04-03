import pygame
from pygame.locals import *
import gameClass
import Screen_3
class Game():
    def __init__(self,screen):
        self.screen = screen

        self.bg = gameClass.BGgroup(self.screen)
        self.bird = gameClass.Bird(self.screen,self.screen.get_width() // 3, self.screen.get_height() // 2)
        self.img_text_ready = pygame.image.load(('img/text_ready.png'))
        self.img_tutorial = pygame.image.load(('img/tutorial.png'))
        self.img_tutorial_rect = self.img_tutorial.get_rect(
            topleft=((screen.get_width() - self.img_tutorial.get_width()) / 2, screen.get_height() / 2))

    def draw(self):
        self.screen.fill((0,0,0))
        self.bg.drawBG()
        self.bg.drawFG()
        self.bird.draw()
        self.screen.blit(self.img_tutorial,self.img_tutorial_rect)
        self.screen.blit(self.img_text_ready,self.img_text_ready.get_rect(topleft =((self.screen.get_width() - self.img_text_ready.get_width()) / 2, self.screen.get_height() / 5) ))

        pygame.display.flip()
    def update(self,clock):
        self.bg.update()
        self.bird.update(clock)
        if self.bird.pos[1] > self.bird.height + 10:
            self.bird.v = -200
        pass

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == MOUSEBUTTONDOWN:
                Screen_3.main(self.screen)
                return True
        return False

def main(screen):

    game = Game(screen)

    done = False
    clock = pygame.time.Clock()
    clock.tick()
    while not done:
        # ticks = pygame.time.get_ticks()
        game.draw()
        game.update(clock)
        done = game.process_events()
        clock.tick(60)

    pygame.quit()
if __name__ == '__main__':
    # 设置窗体宽和高
    SCREEN_WIDTH = 288
    SCREEN_HEIGHT = 512
    # 设置窗体标题
    SCREEN_TITLE = "Flappy Bird"
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption(SCREEN_TITLE)
    pygame.mouse.set_visible(True)
    main(screen)