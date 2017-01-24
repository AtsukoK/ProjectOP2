import pygame
import functions
import colors

class Board():
    def __init__(self,w,h,ic,ac):
        self.msg = ""
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.action = None

    def draw(self):
        for y in range(0,600,30):
            for x in range(100, 700, 30):
                functions.button(self.msg, x, y, self.w, self.h, self.ic, self.ac, self.action)


class Card():
    pass

class Player():
    def __init__(self, player):
        self.player = player

class Boat():
    def __init__(self, c, x, y, w, h):
        self.c = c
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.ellipse(functions.screen, self.c, (self.x, self.y, self.w, self.h))

    def update(self):
        pass
