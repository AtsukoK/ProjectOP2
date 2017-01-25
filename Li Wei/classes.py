import pygame
import functions
import colors

screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

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




    def name(self):
        pass

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

class Boat():
    def __init__(self, mouse, w, h):
        self.mouse = mouse
        self.w = w
        self.h = h

    def draw(self):
        if 100 < self.mouse[0] < 700:
            pygame.draw.ellipse(screen, colors.black, (self.mouse[0], self.mouse[1], self.w, self.h))
            if click[0] == 1:
                pygame.draw.ellipse(screen, colors.green, (self.mouse[0], self.mouse[1], self.w, self.h))

    def update(self):
        pass
