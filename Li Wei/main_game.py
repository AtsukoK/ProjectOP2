import pygame
import time
import colors
import images
import functions
import classes
from pygame.locals import *

pygame.init()
screen_width = 800
screen_heigt = 600
size = (screen_width, screen_heigt)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleport")

events = pygame.event.get()

board = classes.Board()
player = classes.Player()


def intro():
    while not functions.game():
        screen.fill(colors.white)
        screen.blit(images.battleport_img, (275, 0))
        functions.button("Start", 338, 250, 125, 50,  colors.green, colors.bright_green, name1)
        functions.button("Game Rules", 338, 330, 125, 50,  colors.blue, colors.bright_blue, game_rules_1)
        functions.button("Highscores", 338, 410, 125, 50,  colors.yellow, colors.bright_yellow, quit)
        functions.button("Exit", 338, 490, 125, 50,  colors.red, colors.bright_red, quit)

        pygame.display.update()

def pause():
    while not functions.game():
        pygame.draw.rect(screen,colors.bright_snow, (200,150,400,300))
        functions.text("comicsansms", 150, "Paused", (screen_width/2), (screen_heigt/4), colors.black)
        functions.button("Continue", 650, 600, 150, 50,  colors.green, colors.bright_green, main_game)
        functions.button("Game Rules", 850, 600, 150, 50,  colors.blue, colors.bright_blue, game_rules_1_pause)
        functions.button("Settings", 1050, 600, 150, 50,  colors.yellow, colors.bright_yellow, settings_pause)
        functions.button("Quit", 1250, 600, 150, 50,  colors.red, colors.bright_red, intro)
        pygame.display.flip()

def main_game():
    while not functions.game():
        screen.fill(colors.black)
        board.draw()
        player.turn()
        player.update()
        player.draw()
        functions.button("pause", 0, 0, 150, 50,  colors.snow, colors.bright_snow, pause)
        pygame.display.flip()

def name1():
    name1 = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name1 += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name1 = name1[:-1]
                elif evt.key == K_SPACE:
                    name1 += " "
                elif evt.key == K_RETURN:
                    print(name1)
            elif evt.type == QUIT:
                pygame.quit()
                quit()

        screen.fill((colors.black))
        functions.button("Next", 700, 550, 100, 50, colors.white, colors.snow, name2)
        functions.text("comicsansms", 50, "Choose player 1 name", screen_width/2, screen_heigt/4, colors.white)
        functions.text("comicsansms", 50, name1, screen_width/2, screen_heigt/2, colors.white)
        pygame.display.update()

def name2():
    name2 = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name2 += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name2 = name2[:-1]
                elif evt.key == K_SPACE:
                    name2 += " "
                elif evt.key == K_RETURN:
                    print(name2)
            elif evt.type == QUIT:
                pygame.quit()
                quit()

        screen.fill((colors.black))
        functions.button("Next", 700, 550, 100, 50, colors.white, colors.snow, main_game)
        functions.button("previous", 0, 550, 100, 50, colors.white, colors.snow, name1)
        functions.text("comicsansms", 50, "Choose player 2 name", screen_width/2, screen_heigt/4, colors.white)
        functions.text("comicsansms", 50, name2, screen_width/2, screen_heigt/2, colors.white)

        pygame.display.update()

def game_rules_1():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_1, (screen_width * 0.25,0))
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_2)
        pygame.display.flip()

def game_rules_2():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_2, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_1)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_3)
        pygame.display.flip()

def game_rules_3():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_3, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_2)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_4)
        pygame.display.flip()

def game_rules_4():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_4, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_3)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_5)
        pygame.display.flip()

def game_rules_5():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_5, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_4)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_6)
        pygame.display.flip()

def game_rules_6():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_6, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_5)
        pygame.display.flip()

def game_rules_1_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_1, (screen_width * 0.25,0))
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_2)
        pygame.display.flip()

def game_rules_2_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_2, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_1)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_3)
        pygame.display.flip()

def game_rules_3_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_3, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_2)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_4)
        pygame.display.flip()

def game_rules_4_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_4, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_3)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_5)
        pygame.display.flip()

def game_rules_5_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_5, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_4)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_6)
        pygame.display.flip()

def game_rules_6_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_6, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_5)
        pygame.display.flip()


def settings_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, pause)
        pygame.display.flip()

def highscores():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        pygame.display.update()




intro()
pygame.quit()
quit()
