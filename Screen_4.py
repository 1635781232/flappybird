import pygame
from pygame.locals import *
import gameClass
import Screen_1
class Game():
    def __init__(self,screen,score):
        self.screen = screen

        self.score = score
        self.bg = gameClass.BGgroup(self.screen)

        self.img_score_panel = gameClass.Image(('img/score_panel.png'))
        self.img_score_panel.set_pos(((self.screen.get_width() - self.img_score_panel.rect.width) / 2, self.screen.get_height() / 5))

        self.img_medals = [gameClass.Image(('img/medals_{}.png'.format(i))) for  i in range(4)]
        for i in self.img_medals:
            i.set_pos((self.img_score_panel.get_rect().left+32,self.img_score_panel.get_rect().top+44))
        self.medals_num = 0

        gameClass.current = 10

        self.img_score = [gameClass.Image(('img/number_score_0{}.png'.format(i))) for  i in range(10)]
        l = len(str(gameClass.current))
        for i in self.img_score:
            i.set_pos((self.img_score_panel.get_rect().left+193-16*l,self.img_score_panel.get_rect().top+40))
        self.score_list = gameClass.scoreToImg(gameClass.current,self.img_score)
        print(self.score_list)


    def draw(self):
        self.screen.fill((0,0,0))
        self.bg.drawBG()
        self.bg.drawFG()

        self.screen.blit(self.img_score_panel.img,self.img_score_panel.get_rect())

        self.screen.blit(self.img_medals[self.medals_num].img,self.img_medals[self.medals_num].get_rect())

        # self.screen.blit(self.)

        pygame.display.flip()
    def update(self,clock):
        self.bg.update()
        if gameClass.current <10:
            self.medals_num = 0
        elif gameClass.current < 20:
            self.medals_num = 1
        elif gameClass.current <50:
            self.medals_num = 2
        else:
            self.medals_num = 3


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == MOUSEBUTTONDOWN:
                Screen_1.main(self.screen)
                return True
        return False

def main(screen,score = 0):

    game = Game(screen,score)

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