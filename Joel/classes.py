import pygame
import colors
import images
import functions

class Board():
    def __init__(self,w,h,ic,ac):
        self.msg = "X"
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.action = None

    def draw(self):
        for y in range(100,1000,45):
            for x in range(500,1400, 45):
                functions.button(self.msg, x, y, self.w, self.h, self.ic, self.ac, self.action)


class Cards():
    pass

class Players():
    def __init__(self, player):
        self.player = player

    def name(self):
        pass

class Boats():
    def __init__(self, c, x, y, w, h):
        self.c = c
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.ellipse(screen, self.c, (self.x, self.y, self.w, self.h))

    def update(self):
        pass