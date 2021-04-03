import pygame
from pygame.locals import *
import gameClass
import random
import Screen_4
class Game():
    def __init__(self,screen):
        self.screen = screen
        self.bg = gameClass.BGgroup(self.screen)
        self.bird = gameClass.Bird(screen,self.screen.get_width()//4,self.screen.get_height()//2)
        self.text_game_over = pygame.image.load("img/text_game_over.png")
        self.text_game_over_rect = self.text_game_over.get_rect(
            topleft=((screen.get_width() - self.text_game_over.get_width()) / 2, screen.get_height() / 3))


        self.STATE = 'start'

        self.last_time = 0
        self.pipe_list = []
        self.score = 12
        self.score_img = [pygame.image.load("img/font_0{}.png".format(num+48)) for num in range(10)]
        self.score_list = [self.score_img[0]]
        self.score_size = self.score_img[0].get_size()

    def draw(self):
        self.screen.fill((0,0,0))
        self.bg.drawBG()
        for i in self.pipe_list:
            i.draw()
        self.bg.drawFG()
        if self.STATE == "end":
            self.screen.blit(self.text_game_over,self.text_game_over_rect)

        l = len(self.score_list)
        x = (self.screen.get_width()-self.score_size[0]*l)/2
        y = 20
        for img in self.score_list:
            self.screen.blit(img,(x,y))
            # print(self.score_list,x)
            x += img.get_width()+2
        self.bird.draw()
        pygame.display.flip()
    def update(self,clock):
        self.bird.update(clock)
        if self.STATE != "end":
            self.last_time += clock.get_time()
            self.bg.update()
            if self.last_time > 2000:
                deviation = random.randint(-250,-50)
                self.pipe_list.append(gameClass.Pipe(self.screen,[self.screen.get_width(),deviation]))
                self.last_time = 0
            for pipe in self.pipe_list:
                pipe.update()
                if self.bird.get_rect().colliderect(pipe.get_rect()[0]):
                    self.STATE = "end"
                if self.bird.get_rect().colliderect(pipe.get_rect()[1]):
                    if pipe.score:
                        self.score += 1
                        self.score_list = gameClass.scoreToImg(self.score,self.score_img)
                        pipe.score = False
                if self.bird.get_rect().colliderect(pipe.get_rect()[2]):
                    self.STATE = "end"
                pass
            if self.bird.get_rect().colliderect(self.bg.fg1.get_rect()) or self.bird.get_rect().colliderect(self.bg.fg2.get_rect()):
                self.STATE = "end"



    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == MOUSEBUTTONDOWN:
                if self.STATE=='end':
                    gameClass.current = self.score
                    Screen_4.main(self.screen,self.score)
                    return True
                else:
                    self.bird.jump()

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