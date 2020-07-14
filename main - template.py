import pygame as pg
import os
import random
import sys
from Colors import *
from settings import *
from sprites import *

class game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption('test')

        clock.tick(FPS)

    def new(self):
        self.run()

        

    

    def run(self):
        self.running = True
        while self.running:
            self.event()
            self.update()
            self.draw()
            
            
    

    def update(self):
        pass


    def draw(self):
        pass
        
        
    def event(self):
        for e in pg.event.get():
            if e.type== pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()
                


    def start_screen(self):
        pass


    def gameover_screen(self):
        pass

g = game()

playing = True
while playing:
    g.new()

pg.quit()

        
