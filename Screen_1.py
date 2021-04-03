import pygame
import gameClass
import Screen_2

class Game():
    def __init__(self,screen):
        self.screen = screen
        self.bg = gameClass.BGgroup(self.screen)
        self.bird = gameClass.Bird(self.screen,self.screen.get_width()//4,self.screen.get_height()//2)
        self.img_title = pygame.image.load("img/title.png")
        self.img_title_rect = self.img_title.get_rect(topleft = ((screen.get_width()-self.img_title.get_width())/2,screen.get_height()/6))
        self.img_button_play = pygame.image.load(('img/button_play.png'))
        self.img_button_play_rect = self.img_button_play.get_rect(topleft = ((screen.get_width()-self.img_button_play.get_width())/2,screen.get_height()/2))
    def draw(self):
        self.screen.fill((0,0,0))
        self.bg.drawBG()
        self.bg.drawFG()
        self.bird.draw()
        self.screen.blit(self.img_title,self.img_title_rect)
        self.screen.blit(self.img_button_play,self.img_button_play_rect)

        pygame.display.flip()
    def update(self,clock):
        self.bg.update()
        self.bird.update(clock)
        if self.bird.pos[1] > self.bird.height + 10:
            self.bird.v = -200
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.img_button_play_rect.collidepoint((x,y)):
                    Screen_2.main(self.screen)
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