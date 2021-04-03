import pygame
pygame.init()

class Image():
    def __init__(self,file,pos):
        self.file = file
        self.pos = pos
        self.img = pygame.image.load(self.file)

    def get_rect(self):
        return  self.img.get_rect(topleft = self.pos)

class BG(pygame.sprite.Sprite):
    def __init__(self,screen,img_url, deviation_x,deviation_y,speed):
        self.screen = screen
        self.image = pygame.image.load(img_url)
        self.width = self.screen.get_width() - self.image.get_width() + deviation_x
        self.height = self.screen.get_height() - self.image.get_height() +deviation_y
        self.pos = [self.width ,self.height]
        self.speed = speed

    def update(self):
        if self.pos[0]<=-self.screen.get_width():
            self.pos[0] = self.screen.get_width()
        self.pos[0] -=self.speed

    def draw(self):
        self.screen.blit(self.image,self.pos)

    def get_rect(self):
        return self.image.get_rect(topleft = self.pos)

    def set_speed(self,speed):
        self.speed = speed

class BGgroup():
    def __init__(self,screen):
        self.bg1 = BG(screen, "img/bg_day.png", 0, 0, 1)
        self.bg2 = BG(screen, "img/bg_day.png", screen.get_width(), 0, 1)
        self.fg1 = BG(screen, "img/land.png", 0, 0, 3)
        self.fg2 = BG(screen, "img/land.png", screen.get_width(), 0, 3)
        self.bgGroup = [self.bg1,self.bg2,self.fg1,self.fg2]

    def draw(self):
        for i in self.bgGroup:
            i.draw()

    def update(self):
        for i in self.bgGroup:
            i.update()

    def get_rect(self,img):
        return img.get_rect()

bird_list = [
    "img/bird0_0.png",
    "img/bird0_1.png",
    "img/bird0_2.png",
    "img/bird0_1.png",
]
class Bird(pygame.sprite.Sprite):
    def __init__(self,screen,width=0, height=0):
        self.screen = screen
        self.img_list= bird_list

        self.image = []
        self.now_frame = 0
        for i in self.img_list:
            self.image.append(pygame.image.load(i))


        self.width = width - self.image[0].get_width()
        self.height = height -self.image[0].get_height()
        self.pos = [self.width, self.height]
        self.a = 400
        self.t = 0
        self.v = -200
        self.last_time = 0
        self.run = True

    def flash(self,clock,rate=300):
        self.last_time += clock.get_time()
        if self.last_time > rate:
            self.now_frame += 1
            if self.now_frame >= len(self.image):
                self.now_frame = 0
            self.last_time = 0

    def move(self,clock):
        if self.run:
            self.t = clock.get_time()
            self.v = self.v + self.a * self.t/1000
            self.pos[1] = self.pos[1] + self.v * self.t/1000

    def update(self,clock):
        self.flash(clock)
        self.move(clock)

    def draw(self):
        self.screen.blit(self.image[self.now_frame],self.pos)

    def get_rect(self):
        return self.image[self.now_frame].get_rect(topleft = self.pos)

    def set_pos(self,width, height):
        self.pos[0] = width
        self.pos[1] = height

class Pipe(pygame.sprite.Sprite):
    def __init__(self,screen,width,height):
        self.screen = screen
        self.pipe_up = pygame.image.load("img/pipe_up.png")
        self.pipe_down = pygame.image.load("img/pipe_down.png")
        self.width = width
        self.heiht = height
        self.wall = pygame.draw.rect(self.screen,(0,0,0,0),(self.width,self.heiht+self.pipe_down.get_height(),1,50))
        self.pos = [self.width,self.heiht]

    def draw(self):
        self.screen.blit(self.pipe_down,self.pos)
        self.screen.blit(self.pipe_up,(self.width,self.heiht+self.pipe_down.get_height()+self.wall.height))

    def update(self):
        self.pos[0] -= 2
        if self.pos[0]<0-self.pipe_down.get_width():
            self.kill()
        print(self.pos[0])
class Game():
    def __init__(self,screen):
        self.screen = screen
        self.bg = BGgroup(self.screen)
        self.bird = Bird(self.screen,self.screen.get_width()//4,self.screen.get_height()//2)
        self.img_title = pygame.image.load("img/title.png")
        self.img_title_rect = self.img_title.get_rect(topleft = ((screen.get_width()-self.img_title.get_width())/2,screen.get_height()/6))
        self.img_button_play = pygame.image.load(('img/button_play.png'))
        self.img_button_play_rect = self.img_button_play.get_rect(topleft = ((screen.get_width()-self.img_button_play.get_width())/2,screen.get_height()/2))
    def draw(self):
        self.screen.fill((0,0,0))
        self.bg.draw()
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
    game = main(screen)