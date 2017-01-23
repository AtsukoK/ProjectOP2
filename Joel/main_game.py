""" Battleport
Copyright 2017, Bush did Harambe Studios
"""

import pygame
import colors
import images
import functions
import classes
pygame.init()
screen_width = 1920
screen_heigt = 1080
size = (screen_width, screen_heigt)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleport")

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

player1_boat_small = Boats(colors.red,960,960,50,20)

def intro():
    while not functions.game():
        screen.fill(colors.white)
        screen.blit(images.battleport_img, (screen_width * 0.4,0))
        functions.button("Start", 925, 500, 150, 50,  colors.green, colors.brigth_green, main_game)
        functions.button("Game Rules", 925, 600, 150, 50,  colors.blue, colors.brigth_blue, game_rules_1)   
        functions.button("Highscores", 925, 700, 150, 50, colors.yellow , colors.brigth_yellow, highscores)
        functions.button("Settings", 925, 800, 150, 50, colors.snow , colors.brigth_snow, settings)
        functions.button("Exit", 925, 900, 150, 50,  colors.red, colors.brigth_red, functions.quitgame)

        pygame.display.flip()

def pause():
    while not functions.game():
        pygame.draw.rect(screen,colors.brigth_snow, (500,200,960,540))
        functions.text("comicsansms", 150, "Paused", (screen_width/2), (screen_heigt/4))
        functions.button("Continue", 650, 600, 150, 50,  colors.green, colors.brigth_green, main_game)
        functions.button("Quit", 1000, 600, 150, 50,  colors.red, colors.brigth_red, intro)
        pygame.display.flip()

def main_game():
    while not functions.game():
        screen.fill(colors.navy_blue)
        functions.button("pause", 0, 0, 150, 50,  colors.snow, colors.brigth_snow, pause)
        pygame.display.flip()

def game_rules_1():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        screen.blit(images.instruction_img_1, (screen_width * 0.25,0))
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_2)
        pygame.display.flip()

def game_rules_2():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.brigth_snow, intro)
        screen.blit(images.instruction_img_2, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_1)
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_3)
        pygame.display.flip()

def game_rules_3():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        screen.blit(images.instruction_img_3, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_2)
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_4)
        pygame.display.flip()

def game_rules_4():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        screen.blit(images.instruction_img_4, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_3)
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_5)
        pygame.display.flip()

def game_rules_5():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        screen.blit(images.instruction_img_5, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_4)
        pygame.display.flip()

def settings():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        pygame.display.flip()

def highscores():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        pygame.display.flip()

intro()
pygame.quit()
quit()
    
