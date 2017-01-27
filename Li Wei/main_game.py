import pygame
import time
import colors
import images
import functions
from pygame.locals import *
import psycopg2

pygame.init()
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleport")

events = pygame.event.get()





saved_name1 = ""
def name1():
    global saved_name1
    name1 = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name1 += evt.unicode
                    saved_name1 = name1
                elif evt.key == K_BACKSPACE:
                    name1 = name1[:-1]
                    saved_name1 = name1
                elif evt.key == K_SPACE:
                    name1 += " "
                    saved_name1 = name1
            elif evt.type == QUIT:
                pygame.quit()
                quit()

        screen.fill((colors.black))
        functions.button("Next", 700, 550, 100, 50, colors.white, colors.snow, name2)
        functions.text("comicsansms", 50, "Choose player 1 name", screen_width/2, screen_height/4, colors.white)
        functions.text("comicsansms", 50, name1, screen_width/2, screen_height/2, colors.white)
        pygame.display.update()

saved_name2 = ""
def name2():
    global saved_name2
    name2 = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name2 += evt.unicode
                    saved_name2 = name2
                elif evt.key == K_BACKSPACE:
                    name2 = name2[:-1]
                    saved_name2 = name2
                elif evt.key == K_SPACE:
                    name2 += " "
                    saved_name2 = name2
            elif evt.type == QUIT:
                pygame.quit()
                quit()

        screen.fill((colors.black))
        functions.button("Next", 700, 550, 100, 50, colors.white, colors.snow, main_game)
        functions.button("previous", 0, 550, 100, 50, colors.white, colors.snow, name1)
        functions.text("comicsansms", 50, "Choose player 2 name", screen_width/2, screen_height/4, colors.white)
        functions.text("comicsansms", 50, name2, screen_width/2, screen_height/2, colors.white)

        pygame.display.update()

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
        pygame.draw.rect(screen,colors.bright_snow, (220, 120, 20*18, 20*18))
        functions.text("comicsansms", 50, "Paused", (screen_width/2), (screen_height/4), colors.black)
        functions.button("Continue", 340, screen_height*7/20, 120, 40,  colors.green, colors.bright_green, main_game)
        functions.button("Game Rules", 340, screen_height*9/20, 120, 40,  colors.blue, colors.bright_blue, game_rules_1_pause)
        functions.button("Settings", 340, screen_height*11/20, 120, 40,  colors.yellow, colors.bright_yellow, settings_pause)
        functions.button("Quit", 340, screen_height*13/20, 120, 40,  colors.red, colors.bright_red, intro)
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
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.bright_snow, pause)
        pygame.display.flip()

def highscores():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        pygame.display.update()





class Board():
    def __init__(self):
        self.board = []
        self.w = 19
        self.h = 19
        self.c = colors.white

    def draw(self):
        for y in range(100, 500, 20):
            for x in range(200, 600, 20):
                self.board.append(pygame.draw.rect(screen, self.c,(x, y, self.w, self.h)))
        return self.board


class Card():
    pass

class Player():
    def __init__(self):
        self.player1_win = False
        self.player2_win = False
        self.player1_turn = True
        self.player2_turn = False
        self.beurt = 0
        self.boat1_draw = False
        self.boat2_draw = False
        self.boat3_draw = False
        self.boat4_draw = False
        self.boat5_draw = False
        self.boat6_draw = False
        self.boat7_draw = False
        self.boat8_draw = False

    def turn(self):
        if self.player1_turn == False:
            functions.text("comicsansms", 20, saved_name1, 100, 100, colors.white)
        elif self.player1_turn == True:
            functions.text("comicsansms", 20, saved_name1, 100, 100, colors.bright_red)
        if self.player2_turn == False:
            functions.text("comicsansms", 20, saved_name2, 700, 100, colors.white)
        elif self.player2_turn == True:
            functions.text("comicsansms", 20, saved_name2, 700, 100, colors.bright_blue)

    def name1(self):
        self.player1_turn = False
        self.player2_turn = True

    def name2(self):
        self.player2_turn = False
        self.player1_turn = True

    def update(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if self.beurt <8:
            if self.player1_turn == True:
                if click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600:
                    self.beurt += 1
                    self.player1_turn = False
                    self.player2_turn = True
                    if self.beurt == 1:
                        x = mouse[0]
                        while x % 20 != 0:
                            x -=1
                        self.boat1 = Boat(colors.bright_red, x, 460, 19, 40, 2, 3)
                        self.boat1_draw = True
                    elif self.beurt == 3:
                        x = mouse[0]
                        while x % 20 != 0:
                            x -=1
                        self.boat3 = Boat(colors.bright_red, x, 440, 19, 60, 3, 2)
                        self.boat3_draw = True
                    elif self.beurt == 5:
                        x = mouse[0]
                        while x % 20 != 0:
                            x -=1
                        self.boat5 = Boat(colors.bright_red, x, 440, 19, 60, 3, 2)
                        self.boat5_draw = True
                    elif self.beurt == 7:
                        x = mouse[0]
                        while x % 20 != 0:
                            x -=1
                        self.boat7 = Boat(colors.bright_red, x, 420, 19, 80, 4, 1)
                        self.boat7_draw = True
            elif self.player2_turn == True:
                if click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600:
                    self.beurt += 1
                    self.player2_turn = False
                    self.player1_turn = True
                    if self.beurt == 2:
                        x = mouse[0]
                        while x % 20 != 0:
                            x -=1
                        self.boat2 = Boat(colors.bright_blue, x, 100, 19, 40, 2, 3)
                        self.boat2_draw = True
                    elif self.beurt == 4:
                        x = mouse[0]
                        while x % 20 != 0:
                            x -=1
                        self.boat4 = Boat(colors.bright_blue, x, 100, 19, 60, 3, 2)
                        self.boat4_draw = True
                    elif self.beurt == 6:
                        x = mouse[0]
                        while x % 20 != 0:
                            x -=1
                        self.boat6 = Boat(colors.bright_blue, x, 100, 19, 60, 3, 2)
                        self.boat6_draw = True
                    elif self.beurt == 8:
                        x = mouse[0]
                        while x % 20 != 0:
                            x -=1
                        self.boat8 = Boat(colors.bright_blue, x, 100, 19, 80, 4, 1)
                        self.boat8_draw = True
        else:
            if self.player1_turn == True:
                functions.button("move", 125, 400, 75, 25, colors.green, colors.bright_green, None)
                functions.button("turn", 125, 425, 75, 25, colors.snow, colors.bright_snow, None)
                functions.button("attack", 125, 450, 75, 25, colors.yellow, colors.bright_yellow, None)
                functions.button("end turn", 125, 475, 75, 25, colors.red, colors.bright_red, self.name1)
                functions.text("comicsansms",20, "boat 1 health:" + str(self.boat1.health), 100, 200, colors.bright_red)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat1.moves), 100, 225, colors.red)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat3.health), 100, 250, colors.bright_red)
                functions.text("comicsansms",20, "boat 2 moves:" + str(self.boat3.moves), 100, 275, colors.red)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat5.health), 100, 300, colors.bright_red)
                functions.text("comicsansms",20, "boat 3 moves:" + str(self.boat5.moves), 100, 325, colors.red)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat7.health), 100, 350, colors.bright_red)
                functions.text("comicsansms",20, "boat 4 moves:" + str(self.boat7.moves), 100, 375, colors.red)
            elif self.player2_turn == True:
                functions.button("move", 600, 400, 75, 25, colors.green, colors.bright_green, None)
                functions.button("turn", 600, 425, 75, 25, colors.snow, colors.bright_snow, None)
                functions.button("attack", 600, 450, 75, 25, colors.yellow, colors.bright_yellow, None)
                functions.button("end turn", 600, 475, 75, 25, colors.red, colors.bright_red, self.name2)
                functions.text("comicsansms",20, "boat 1 health:" + str(self.boat2.health), 700, 200, colors.bright_blue)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat2.moves), 700, 225, colors.blue)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat4.health), 700, 250, colors.bright_blue)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat4.moves), 700, 275, colors.blue)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat6.health), 700, 300, colors.bright_blue)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat6.moves), 700, 325, colors.blue)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat8.health), 700, 350, colors.bright_blue)
                functions.text("comicsansms",20, "boat 4 moves:" + str(self.boat8.moves), 700, 375, colors.blue)

    def draw(self):
        if self.boat1_draw == True:
            self.boat1.draw()
        if self.boat2_draw == True:
            self.boat2.draw()
        if self.boat3_draw == True:
            self.boat3.draw()
        if self.boat4_draw == True:
            self.boat4.draw()
        if self.boat5_draw == True:
            self.boat5.draw()
        if self.boat6_draw == True:
            self.boat6.draw()
        if self.boat7_draw == True:
            self.boat7.draw()
        if self.boat8_draw == True:
            self.boat8.draw()

    def rotate(self):
        pass

class Boat(Player):
    def __init__(self, c, x, y, w, h, health, moves):
        self.c = c
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = health
        self.moves = moves

    def draw(self):
        pygame.draw.ellipse(screen, self.c, (self.x, self.y, self.w, self.h))

    def update(self):
        pass


board = Board()
player = Player()



















intro()
pygame.quit()
quit()
