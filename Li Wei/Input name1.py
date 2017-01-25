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

board = classes.Board(28, 28, colors.white, colors.snow)


def intro():
    while not functions.game():
        screen.fill(colors.white)
        screen.blit(images.battleport_img, (275, 0))
        functions.button("Start", 338, 250, 125, 50,  colors.green, colors.bright_green, name)
        functions.button("Game Rules", 338, 330, 125, 50,  colors.blue, colors.bright_blue, game_rules_1)
        functions.button("Highscores", 338, 410, 125, 50,  colors.yellow, colors.bright_yellow, quit)
        functions.button("Exit", 338, 490, 125, 50,  colors.red, colors.bright_red, quit)

        pygame.display.update()

def main_game():
    while not functions.game():
        screen.fill(colors.navy_blue)
        board.draw()
        functions.button("Exit Game", 700, 550, 100, 50,  colors.snow, colors.bright_snow, quit)
        functions.button("Pause", 700, 500, 100, 50,  colors.snow, colors.bright_snow, quit)
        pygame.display.flip()

def name():
    while not functions.game():
        screen.fill(colors.black)
        functions.text("Fill in Player 1 name:", "comicsans", 50, 20, 20, colors.white)
        functions.text("Max 5 characters", "comicsans", 50, 20, 70, colors.white)
        pygame.display.flip()

        print("name")

        i = 0
        while i == 0:
                name1 = ""
                for event in events:
                    if event.type == KEYDOWN:
                        if event.unicode.isalpha():
                            name1 += event.unicode
                        elif event.key == K_BACKSPACE:
                            name1 = name1[:-1]
                        elif event.key == K_RETURN:
                            functions.text("Fill in Player 2 name:", "comicsans", 50, 20, 420, colors.white)
                            functions.text("Max 5 characters", "comicsans", 50, 20, 470, colors.white)
                            i = 1
                        elif event.key == K_SPACE:
                            name1 += " "
                    elif event.type == QUIT:
                        pygame.quit()
                        quit()
                functions.text(name1, "comicssans", 50, 500, 20, colors.white)
                pygame.display.flip()

        while i == 1:
                name2 = ""
                for event in events:
                    if event.type == KEYDOWN:
                        if event.unicode.isalpha():
                            name2 += event.unicode
                        elif event.key == K_BACKSPACE:
                            name2 = name2[:-1]
                        elif event.key == K_RETURN:
                            name2 = ""
                            i = 2
                        elif event.key == K_SPACE:
                            name2 += " "
                    elif event.type == QUIT:
                        pygame.quit()
                        quit()
                functions.text(name2, "comicsans", 50, 500, 420, colors.white)
                pygame.display.flip()

        print("test")
        pygame.display.flip()


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
        pygame.display.flip()

def highscores():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        pygame.display.update()




intro()
pygame.quit()
quit()

