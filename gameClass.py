import pygame

pygame.init()

best = 0
current = 0

class Image(pygame.sprite.Sprite):
    def __init__(self,file,pos = (0,0)):
        super().__init__()
        self.img = pygame.image.load(file)
        self.rect = self.img.get_rect()
        self.rect.topleft = pos

    def set_pos(self,pos):
        self.rect.topleft = pos

    def get_rect(self):
        return  self.img.get_rect(topleft = self.rect.topleft)

class BG(pygame.sprite.Sprite):
    def __init__(self,screen,img_url, deviation_x,deviation_y,speed):
        super().__init__()
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
        self.bgGroup = [self.bg1,self.bg2]
        self.fgGroup = [self.fg1,self.fg2]

    def drawBG(self):
        for i in self.bgGroup:
            i.draw()

    def drawFG(self):
        for i in self.fgGroup:
            i.draw()

    def update(self):
        for i in self.bgGroup:
            i.update()
        for i in self.fgGroup:
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
        super().__init__()
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
    def jump(self):
        self.v = -200
    def move(self,clock):
        if self.run:
            self.t = clock.get_time()
            self.v = self.v + self.a * self.t/1000
            self.pos[1] = self.pos[1] + self.v * self.t/1000
        if self.pos[1]>= 380:
            self.pos[1] =380

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
    def __init__(self,screen,pos):
        super().__init__()
        self.screen = screen
        self.pipe_up = pygame.image.load("img/pipe_up.png")
        self.pipe_down = pygame.image.load("img/pipe_down.png")
        self.pos_down = pos
        self.wall_height = 100
        self.wall_width = 1
        self.pos_up =[ self.pos_down[0],self.pos_down[1]+self.pipe_down.get_height()+self.wall_height]
        self.wall = pygame.draw.rect(self.screen,(0,0,0,0),(self.pos_down[0]+self.pipe_down.get_width(),self.pos_down[1]+self.pipe_down.get_height(),self.wall_width,self.wall_height))
        self.score = True
    def draw(self):
        self.screen.blit(self.pipe_down,self.pos_down)
        self.screen.blit(self.pipe_up,self.pos_up)
        self.wall = pygame.draw.rect(self.screen,(0,0,0,0),(self.wall.x,self.wall.y,0,50))
        pass
    def update(self,run = True):
        if run:
            self.pos_down[0] -= 2
            self.pos_up = [self.pos_down[0], self.pos_down[1] + self.pipe_down.get_height() + self.wall_height]
            self.wall.x = self.pos_down[0]+self.pipe_down.get_width()
            self.wall.y = self.pos_down[1] + self.pipe_down.get_height()
            if self.pos_down[0]<0-self.pipe_down.get_width():
                del self
                # self.kill()
    def get_rect(self):
        return self.pipe_down.get_rect(topleft = self.pos_down),(self.wall.x,self.wall.y,self.wall_width,self.wall_height),self.pipe_up.get_rect(topleft = self.pos_up)

def scoreToImg(score,score_img):
    score_list = []
    while not (score%10 == 0 and score<10):
        last = score % 10
        score_list.insert(0,score_img[last])
        score = score // 10
    return score_list
