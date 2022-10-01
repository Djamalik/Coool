from multiprocessing import Barrier
from struct import pack
from turtle import screensize
from pygame import *
mixer.init()
class GameSpirits(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSpirits):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSpirits.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if self.rect.x<= win_wight-ww*80 and self.x_speed>0 or self.rect.x >=0 and self.x_speed<0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = p.rect.left
        elif self.x_speed<0:
            for p in platforms_touched:
                self.rect.left = p.rect.right
        if self.rect.y<= win_hight-wh*80 and self.y_speed>0 or self.rect.y >=0 and self.y_speed<0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = p.rect.bottom               
        elif self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = p.rect.top

    def fire(self):
        bullet = Bullet('bullet.png', packman.rect.x+ww*80, packman.rect.y+wh*30, ww*15, wh*20, ww*15)
        bullets.add(bullet)

class Enemy(GameSpirits):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, live):
        GameSpirits.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.rect.x = player_x
        self.live = live
    def update(self):
        self.rect.x+=self.x_speed
        if self.rect.x >= ww*640 or self.rect.x <= ww*420:
            self.x_speed*=-1

class Bullet(GameSpirits):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed):
        GameSpirits.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.size_x = size_x
        self.size_y = size_y
    def update(self):
        self.rect.x += self.x_speed
        if self.rect.x > win_wight-ww*25:
            self.kill()


win_wight = 800
win_hight = 600
ww = win_wight/700
wh = win_hight/500
window = display.set_mode((win_wight,win_hight))
BLUE = (119,210,223)
back = (255,255,255)
display.set_caption('LABIRINT')

barriers = sprite.Group()
w1 = GameSpirits('platform1.png',ww*116, wh*250, ww*300, wh*50)
w2 = GameSpirits('platform2.png',ww*370, wh*100, ww*50, wh*400)
barriers.add(w1)
barriers.add(w2)

bullets = sprite.Group()
monsters = sprite.Group()
cyborg = Enemy('osel.jpg', ww*425, wh*100, ww*60, wh*80, ww*5, True)
monsters.add(cyborg)

packman = Player('shrek.png', ww*5, wh*420, ww*80, wh*80, 0, 0)
fullscreen = 1
final_sprite = GameSpirits('shrek_end.png', win_wight - ww*80, win_hight - wh*80, ww*80, wh*80)
finish = False

run = True

while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT or e.key == K_a:
                packman.x_speed = -5*ww
            elif e.key == K_RIGHT or e.key == K_d:
                packman.x_speed = 5*ww
            elif e.key == K_UP or e.key == K_w:
                packman.y_speed = -5*wh
            elif e.key == K_DOWN or e.key == K_s:
                packman.y_speed = 5*wh
            elif e.key == K_SPACE:
                packman.fire()
            elif e.key == K_f:
                packman.rect.x=packman.rect.x/ww
                packman.rect.y=packman.rect.y/wh
                if fullscreen == 1:
                    win_wight = 1200
                    win_hight = 800
                    fullscreen = 0
                    window = display.set_mode((win_wight,win_hight),FULLSCREEN)
                elif fullscreen == 0:
                    win_wight = 800
                    win_hight = 600
                    fullscreen = 1
                    window = display.set_mode((win_wight,win_hight))
                ww = win_wight/700
                wh = win_hight/500

                w1 = GameSpirits('platform1.png',ww*116, wh*250, ww*300, wh*50)
                w2 = GameSpirits('platform2.png',ww*370, wh*100, ww*50, wh*400)
                barriers = sprite.Group()
                barriers.add(w1)
                barriers.add(w2)
                if cyborg.live == True:
                    cyborg = Enemy('osel.jpg', ww*425, wh*100, ww*60, wh*80, ww*5, cyborg.live)
                    monsters = sprite.Group()
                    monsters.add(cyborg)
                packman = Player('shrek.png', packman.rect.x*ww, packman.rect.y*wh, ww*80, wh*80, 0,0)
                final_sprite = GameSpirits('shrek_end.png', win_wight - ww*80, win_hight - wh*80, ww*80, wh*80)

        elif e.type == KEYUP:
            if e.key == K_LEFT or e.key == K_a:
                packman.x_speed = 0
            elif e.key == K_RIGHT or e.key == K_d:
                packman.x_speed = 0
            elif e.key == K_UP or e.key == K_w:
                packman.y_speed = 0
            elif e.key == K_DOWN or e.key == K_s:
                packman.y_speed = 0

    if finish == False:
        window.fill(back)

        bullets.draw(window)
        bullets.update()
        sprite.groupcollide(bullets,barriers,True,False)

        barriers.draw(window)
        final_sprite.reset()

        packman.reset()
        packman.update()

        if not(sprite.groupcollide(bullets,monsters,True,True)):
            monsters.draw(window)
            monsters.update()
        else:
            cyborg.live = False

        if sprite.spritecollide(packman,monsters,True):
            finish = True
            img = image.load('game-over_1.png')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_wight, win_hight)),(0,0))

        if sprite.collide_rect(packman,final_sprite):
            finish = True
            img = image.load('shrek_win.png')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(win_wight, win_hight)),(0,0))
    display.update()