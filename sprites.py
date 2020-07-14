import pygame as pg
from Colors import *
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        

        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)



    def update(self):
        
##        self.acc = vec(0,0)

        pressed = pg.key.get_pressed()
        if pressed[pg.K_RIGHT]:
            self.acc.x =  0.5
        elif pressed[pg.K_LEFT]:
            self.acc.x = - 0.5
##        print self.acc[0]

            
        self.vel.x = self.vel.x + self.acc.x
##        print self.vel[0]
        

        self.pos.x = self.vel.x + 0.5 * self.acc.x
        

        self.rect.center = self.pos
        

        

        
            
    
