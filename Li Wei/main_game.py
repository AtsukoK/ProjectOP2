import pygame
import time
import colors
import images
import functions
from pygame.locals import *
from database import*


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
        functions.button("Main Menu", 0, 0, 100, 50, colors.white, colors.snow, intro)
        functions.button("Next", 700, 550, 100, 50, colors.white, colors.snow, name2)
        functions.text("comicsansms", 50, "Choose player 1 name", screen_width/2, screen_height/4, colors.white)
        functions.text("comicsansms", 50, name1, screen_width/2, screen_height/2, colors.white)
        pygame.display.update()

saved_name2 = ""

def name2():
    stats = download_leaderboads()
    updated = False
    for stat in stats:
        if stat[0] == saved_name1:
            updated = True
            update_leaderboards(saved_name1, stat[1] + 1, stat[2])
            break

    if not updated:
        insert_leaderboards(saved_name1, 1, 0)


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
        functions.button("Main Menu", 0, 0, 100, 50, colors.white, colors.snow, intro)
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
        functions.button("Highscores", 338, 410, 125, 50,  colors.yellow, colors.bright_yellow, highscores)
        functions.button("Exit", 338, 490, 125, 50,  colors.red, colors.bright_red, quit)

        pygame.display.update()

def pause():
    while not functions.game():
        pygame.draw.rect(screen,colors.bright_snow, (220, 120, 20*18, 20*18))
        functions.text("comicsansms", 50, "Paused", (screen_width/2), (screen_height/4), colors.black)
        functions.button("Continue", 340, screen_height*7/20, 120, 40,  colors.green, colors.bright_green, main_game)
        functions.button("Game Rules", 340, screen_height*9/20, 120, 40,  colors.blue, colors.bright_blue, game_rules_1_pause)
        functions.button("Settings", 340, screen_height*11/20, 120, 40,  colors.yellow, colors.bright_yellow, settings_pause)
        functions.button("Exit Game", 340, screen_height*13/20, 120, 40,  colors.red, colors.bright_red, intro)
        pygame.display.flip()

def main_game():
    while not functions.game():
        screen.fill(colors.black)
        board.draw()
        player.turn()
        player.update()
        player.move1()
        player.turn1()
        player.attack1()
        player.move2()
        player.turn2()
        player.attack2()
        player.moveboat()
        player.turnboat()
        player.attackboat()
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

def highscores():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("Main Menu", 0, 0, 100, 50, colors.snow, colors.bright_snow, intro)
        stats = download_leaderboads()

        functions.text("comicsansms", 30, "Name", screen_width*0.20, 100, colors.black)
        functions.text("comicsansms", 30, "Wins", screen_width*0.40, 100, colors.black)
        functions.text("comicsansms", 30, "Losses", screen_width*0.60, 100, colors.black)
        functions.text("comicsansms", 30, "W/L Ratio", screen_width*0.80, 100, colors.black)

        heightstat = 150

        for stat in stats:
            functions.text("comicsansms", 20, str(stat[0]), screen_width*0.20, heightstat, colors.black)
            functions.text("comicsansms", 20, str(stat[1]), screen_width*0.40, heightstat, colors.black)
            functions.text("comicsansms", 20, str(stat[2]), screen_width*0.60, heightstat, colors.black)
            if stat[2] != 0:
                functions.text("comicsansms", 20, str(format((stat[1]/stat[2]), '.2f')), screen_width*0.80, heightstat, colors.black)
            else:
                functions.text("comicsansms", 20, str(stat[1]), screen_width*0.80, heightstat, colors.black)

            heightstat += 40

        pygame.display.flip()

def game_rules_1_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, main_game)
        screen.blit(images.instruction_img_1, (screen_width * 0.25,0))
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_2)
        pygame.display.flip()

def game_rules_2_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, main_game)
        screen.blit(images.instruction_img_2, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_1)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_3)
        pygame.display.flip()

def game_rules_3_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, main_game)
        screen.blit(images.instruction_img_3, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_2)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_4)
        pygame.display.flip()

def game_rules_4_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, main_game)
        screen.blit(images.instruction_img_4, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_3)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_5)
        pygame.display.flip()

def game_rules_5_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, main_game)
        screen.blit(images.instruction_img_5, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_4)
        functions.button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_6)
        pygame.display.flip()

def game_rules_6_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, main_game)
        screen.blit(images.instruction_img_6, (screen_width * 0.25,0))
        functions.button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_5)
        pygame.display.flip()


def settings_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.bright_snow, pause)
        pygame.display.flip()





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

        self.boat1_width_1 = 800
        self.boat1_width_2 = 0
        self.boat2_width_1 = 800
        self.boat2_width_2 = 0
        self.boat3_width_1 = 800
        self.boat3_width_2 = 0
        self.boat4_width_1 = 800
        self.boat4_width_2 = 0
        self.boat5_width_1 = 800
        self.boat5_width_2 = 0
        self.boat6_width_1 = 800
        self.boat6_width_2 = 0


        self.move1_def = False
        self.turn1_def = False
        self.attack1_def = False
        self.move2_def = False
        self.turn2_def = False
        self.attack2_def = False

        self.boat_move = 0
        self.boat_turn = 0
        self.boat_attack = 0

        self.player_attack = 2

        self.thing = 0


#    def win(self):
#        if self.boat1.health and self.boat3.health and self.boat5.health and self.boat7.health:
#            self.player2_win = True
#            stats = download_leaderboads()
#            counter = count_rows()
#            for stat in stats:
#                if stat[0] == saved_name1:
#                    update_leaderboards(saved_name1, stat[1] + 1, stat[2])
#                elif stat == counter:
#                    insert_leaderboards(saved_name1, 1, 0)
#
#
#        elif self.boat2.health and self.boat4.health and self.boat6.health and self.boat8.health:
#            self.player1_win = True
#            stats = download_leaderboads()
#            counter = count_rows()
#            for stat in stats:
#                if stat[0] == saved_name1:
#                    update_leaderboards(saved_name1, stat[1] + 1)
#                elif stat == counter:
#                    insert_leaderboards(saved_name1, 1)


    def base_color(self):
        self.boat1.c = colors.red
        self.boat3.c = colors.red
        self.boat5.c = colors.red
        self.boat7.c = colors.red
        self.boat2.c = colors.blue
        self.boat4.c = colors.blue
        self.boat6.c = colors.blue
        self.boat8.c = colors.blue

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
        self.boat1.moves = 3
        self.boat3.moves = 2
        self.boat5.moves = 2
        self.boat7.moves = 1
        self.boat1.attack = 1
        self.boat3.attack = 1
        self.boat5.attack = 1
        self.boat7.attack = 1
        self.boat_move = 0
        self.boat_turn = 0
        self.boat_attack = 0
        self.base_color()
        self.player_attack = 2
        self.thing = 0

    def name2(self):
        self.player2_turn = False
        self.player1_turn = True
        self.boat2.moves = 3
        self.boat4.moves = 2
        self.boat6.moves = 2
        self.boat8.moves = 1
        self.boat2.attack = 1
        self.boat4.attack = 1
        self.boat6.attack = 1
        self.boat8.attack = 1
        self.boat_turn = 0
        self.boat_move = 0
        self.boat_attack = 0
        self.base_color()
        self.player_attack = 2
        self.thing = 0

    def update(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if self.beurt <8:
            if self.player1_turn == True:
                if click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] < self.boat1_width_1 and mouse[0] < self.boat3_width_1 and mouse[0] < self.boat5_width_1 \
                or click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] > self.boat1_width_2 and mouse[0] > self.boat3_width_2 and mouse[0] > self.boat5_width_2 \
                or click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] < self.boat1_width_1 and mouse[0] < self.boat3_width_1 and mouse[0] > self.boat5_width_2 \
                or click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] < self.boat1_width_1 and mouse[0] > self.boat3_width_2 and mouse[0] > self.boat5_width_2 \
                or click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] < self.boat1_width_1 and mouse[0] > self.boat3_width_2 and mouse[0] < self.boat5_width_1 \
                or click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] > self.boat1_width_2 and mouse[0] < self.boat3_width_1 and mouse[0] < self.boat5_width_1 \
                or click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] > self.boat1_width_2 and mouse[0] < self.boat3_width_1 and mouse[0] > self.boat5_width_2 \
                or click[0] and mouse[1] > 480 and mouse[1] < 500 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] > self.boat1_width_2 and mouse[0] > self.boat3_width_2 and mouse[0] < self.boat5_width_1:
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
                if click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] < self.boat2_width_1 and mouse[0] < self.boat4_width_1 and mouse[0] < self.boat6_width_1 \
                or click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] > self.boat2_width_2 and mouse[0] > self.boat4_width_2 and mouse[0] > self.boat6_width_2 \
                or click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] < self.boat2_width_1 and mouse[0] < self.boat4_width_1 and mouse[0] > self.boat6_width_2 \
                or click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] < self.boat2_width_1 and mouse[0] > self.boat4_width_2 and mouse[0] > self.boat6_width_2 \
                or click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] < self.boat2_width_1 and mouse[0] > self.boat4_width_2 and mouse[0] < self.boat6_width_1 \
                or click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] > self.boat2_width_2 and mouse[0] < self.boat4_width_1 and mouse[0] < self.boat6_width_1 \
                or click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] > self.boat2_width_2 and mouse[0] < self.boat4_width_1 and mouse[0] > self.boat6_width_2 \
                or click[0] and mouse[1] > 100 and mouse [1] < 120 and mouse[0] > 200 and mouse [0] < 600 and mouse[0] > self.boat2_width_2 and mouse[0] > self.boat4_width_2 and mouse[0] < self.boat6_width_1:

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
                functions.button("move", 125, 400, 75, 25, colors.green, colors.bright_green, self.move_boat1)
                functions.button("turn", 125, 425, 75, 25, colors.snow, colors.bright_snow, self.turn_boat1)
                functions.button("attack", 125, 450, 75, 25, colors.yellow, colors.bright_yellow, self.attack_boat1)
                functions.button("end turn", 125, 475, 75, 25, colors.red, colors.bright_red, self.name1)
                functions.text("comicsansms", 15, "boat 1 health:" + str(self.boat1.health), 100, 200, colors.bright_red)
                functions.text("comicsansms", 15, "boat 1 moves:" + str(self.boat1.moves), 100, 225, colors.red)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat3.health), 100, 250, colors.bright_red)
                functions.text("comicsansms",20, "boat 2 moves:" + str(self.boat3.moves), 100, 275, colors.red)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat5.health), 100, 300, colors.bright_red)
                functions.text("comicsansms",20, "boat 3 moves:" + str(self.boat5.moves), 100, 325, colors.red)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat7.health), 100, 350, colors.bright_red)
                functions.text("comicsansms",20, "boat 4 moves:" + str(self.boat7.moves), 100, 375, colors.red)
            elif self.player2_turn == True:
                functions.button("move", 600, 400, 75, 25, colors.green, colors.bright_green, self.move_boat2)
                functions.button("turn", 600, 425, 75, 25, colors.snow, colors.bright_snow, self.turn_boat2)
                functions.button("attack", 600, 450, 75, 25, colors.yellow, colors.bright_yellow, self.attack_boat2)
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
                self.boat1_width_1 = self.boat1.x
                self.boat1_width_2 = (self.boat1.x + 20)
        if self.boat2_draw == True:
                self.boat2.draw()
                self.boat2_width_1 = self.boat2.x
                self.boat2_width_2 = (self.boat2.x + 20)
        if self.boat3_draw == True:
                self.boat3.draw()
                self.boat3_width_1 = self.boat3.x
                self.boat3_width_2 = (self.boat3.x + 20)
        if self.boat4_draw == True:
                self.boat4.draw()
                self.boat4_width_1 = self.boat4.x
                self.boat4_width_2 = (self.boat4.x + 20)
        if self.boat5_draw == True:
                self.boat5.draw()
                self.boat5_width_1 = self.boat5.x
                self.boat5_width_2 = (self.boat5.x + 20)
        if self.boat6_draw == True:
                self.boat6.draw()
                self.boat6_width_1 = self.boat6.x
                self.boat6_width_2 = (self.boat6.x + 20)
        if self.boat7_draw == True:
                self.boat7.draw()
        if self.boat8_draw == True:
                self.boat8.draw()

    def move_boat1(self):
        self.thing = 1
        self.boat_move = 0
        self.boat_attack = 0
        self.base_color()

    def turn_boat1(self):
        self.thing = 2
        self.boat_move = 0
        self.boat_attack = 0
        self.base_color()

    def attack_boat1(self):
        self.thing = 3
        self.boat_move = 0
        self.boat_attack = 0
        self.base_color()

    def move1(self):
        if self.thing == 1:
            functions.button("boat 1", 50, 400, 75, 25, colors.green, colors.bright_green, self.movemove1)
            functions.button("boat 2", 50, 425, 75, 25, colors.green, colors.bright_green, self.movemove3)
            functions.button("boat 3", 50, 450, 75, 25, colors.green, colors.bright_green, self.movemove5)
            functions.button("boat 4", 50, 475, 75, 25, colors.green, colors.bright_green, self.movemove7)

    def turn1(self):
        if self.thing == 2:
            functions.button("boat 1", 50, 400, 75, 25, colors.snow, colors.bright_snow, self.turnturn1)
            functions.button("boat 2", 50, 425, 75, 25, colors.snow, colors.bright_snow, self.turnturn3)
            functions.button("boat 3", 50, 450, 75, 25, colors.snow, colors.bright_snow, self.turnturn5)
            functions.button("boat 4", 50, 475, 75, 25, colors.snow, colors.bright_snow, self.turnturn7)

    def attack1(self):
        if self.thing == 3:
            functions.button("boat 1", 50, 400, 75, 25, colors.yellow, colors.bright_yellow, self.attackattack1)
            functions.button("boat 2", 50, 425, 75, 25, colors.yellow, colors.bright_yellow, self.attackattack3)
            functions.button("boat 3", 50, 450, 75, 25, colors.yellow, colors.bright_yellow, self.attackattack5)
            functions.button("boat 4", 50, 475, 75, 25, colors.yellow, colors.bright_yellow, self.attackattack7)

    def move_boat2(self):
        self.thing = 4
        self.boat_move = 0
        self.base_color()

    def turn_boat2(self):
        self.thing = 5
        self.boat_move = 0
        self.base_color()

    def attack_boat2(self):
        self.thing = 6
        self.boat_move = 0
        self.base_color()

    def move2(self):
        if self.thing == 4:
            functions.button("boat 1", 675, 400, 75, 25, colors.green, colors.bright_green, self.movemove2)
            functions.button("boat 2", 675, 425, 75, 25, colors.green, colors.bright_green, self.movemove4)
            functions.button("boat 3", 675, 450, 75, 25, colors.green, colors.bright_green, self.movemove6)
            functions.button("boat 4", 675, 475, 75, 25, colors.green, colors.bright_green, self.movemove8)

    def turn2(self):
        if self.thing == 5:
            functions.button("boat 1", 675, 400, 75, 25, colors.snow, colors.bright_snow, self.turnturn2)
            functions.button("boat 2", 675, 425, 75, 25, colors.snow, colors.bright_snow, self.turnturn4)
            functions.button("boat 3", 675, 450, 75, 25, colors.snow, colors.bright_snow, self.turnturn6)
            functions.button("boat 4", 675, 475, 75, 25, colors.snow, colors.bright_snow, self.turnturn8)

    def attack2(self):
        if self.thing == 6:
            functions.button("boat 1", 675, 400, 75, 25, colors.yellow, colors.bright_yellow, self.attackattack2)
            functions.button("boat 2", 675, 425, 75, 25, colors.yellow, colors.bright_yellow, self.attackattack4)
            functions.button("boat 3", 675, 450, 75, 25, colors.yellow, colors.bright_yellow, self.attackattack6)
            functions.button("boat 4", 675, 475, 75, 25, colors.yellow, colors.bright_yellow, self.attackattack8)

    def movemove1(self):
        self.boat_move = 1
        self.base_color()

    def movemove3(self):
        self.boat_move = 3
        self.base_color()

    def movemove5(self):
        self.boat_move = 5
        self.base_color()

    def movemove7(self):
        self.boat_move = 7
        self.base_color()

    def movemove2(self):
        self.boat_move = 2
        self.base_color()

    def movemove4(self):
        self.boat_move = 4
        self.base_color()

    def movemove6(self):
        self.boat_move = 6
        self.base_color()

    def movemove8(self):
        self.boat_move = 8
        self.base_color()

    def moveboat(self):
        keys = pygame.key.get_pressed()
        if self.boat_move == 1 and self.boat1.defense == False:
            self.boat1.c = colors.bright_red
            if self.boat1.moves != 0:
                if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.boat1.x >= 220:
                    self.boat1.x -= 20
                    self.boat1.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.boat1.x <= 560:
                    self.boat1.x += 20
                    self.boat1.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.boat1.y <= 440:
                    self.boat1.y += 20
                    self.boat1.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.boat1.y >= 120:
                    self.boat1.y -= 20
                    self.boat1.moves -= 1
                    time.sleep(0.2)
        elif self.boat_move == 2 and self.boat2.defense == False:
            self.boat2.c = colors.bright_blue
            if self.boat2.moves != 0:
                if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.boat2.x >= 220:
                    self.boat2.x -= 20
                    self.boat2.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.boat2.x <= 560:
                    self.boat2.x += 20
                    self.boat2.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.boat2.y <= 440:
                    self.boat2.y += 20
                    self.boat2.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.boat2.y >= 120:
                    self.boat2.y -= 20
                    self.boat2.moves -= 1
                    time.sleep(0.2)
        elif self.boat_move == 3 and self.boat3.defense == False:
            self.boat3.c = colors.bright_red
            if self.boat3.moves != 0:
                if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.boat3.x >= 220:
                    self.boat3.x -= 20
                    self.boat3.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.boat3.x <= 560:
                    self.boat3.x += 20
                    self.boat3.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.boat3.y <= 420:
                    self.boat3.y += 20
                    self.boat3.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.boat3.y >= 120:
                    self.boat3.y -= 20
                    self.boat3.moves -= 1
                    time.sleep(0.2)
        elif self.boat_move == 4 and self.boat4.defense == False:
            self.boat4.c = colors.bright_blue
            if self.boat4.moves != 0:
                if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.boat4.x >= 220:
                    self.boat4.x -= 20
                    self.boat4.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.boat4.x <= 560:
                    self.boat4.x += 20
                    self.boat4.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.boat4.y <= 420:
                    self.boat4.y += 20
                    self.boat4.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.boat4.y >= 120:
                    self.boat4.y -= 20
                    self.boat4.moves -= 1
                    time.sleep(0.2)
        elif self.boat_move == 5 and self.boat5.defense == False:
            self.boat5.c = colors.bright_red
            if self.boat5.moves != 0:
                if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.boat5.x >= 220:
                    self.boat5.x -= 20
                    self.boat5.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.boat5.x <= 560:
                    self.boat5.x += 20
                    self.boat5.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.boat5.y <= 420:
                    self.boat5.y += 20
                    self.boat5.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.boat5.y >= 120:
                    self.boat5.y -= 20
                    self.boat5.moves -= 1
                    time.sleep(0.2)
        elif self.boat_move == 6 and self.boat6.defense == False:
            self.boat6.c = colors.bright_blue
            if self.boat6.moves != 0:
                if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.boat6.x >= 220:
                    self.boat6.x -= 20
                    self.boat6.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.boat6.x <= 560:
                    self.boat6.x += 20
                    self.boat6.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.boat6.y <= 420:
                    self.boat6.y += 20
                    self.boat6.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.boat6.y >= 120:
                    self.boat6.y -= 20
                    self.boat6.moves -= 1
                    time.sleep(0.2)
        elif self.boat_move == 7 and self.boat7.defense == False:
            self.boat7.c = colors.bright_red
            if self.boat7.moves != 0:
                if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.boat7.x >= 220:
                    self.boat7.x -= 20
                    self.boat7.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.boat7.x <= 560:
                    self.boat7.x += 20
                    self.boat7.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.boat7.y <= 400:
                    self.boat7.y += 20
                    self.boat7.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.boat7.y >= 120:
                    self.boat7.y -= 20
                    self.boat7.moves -= 1
                    time.sleep(0.2)
        elif self.boat_move == 8 and self.boat8.defense == False:
            self.boat8.c = colors.bright_blue
            if self.boat8.moves != 0:
                if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.boat8.x >= 220:
                    self.boat8.x -= 20
                    self.boat8.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.boat8.x <= 560:
                    self.boat8.x += 20
                    self.boat8.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.boat8.y <= 400:
                    self.boat8.y += 20
                    self.boat8.moves -= 1
                    time.sleep(0.2)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.boat8.y >= 120:
                    self.boat8.y -= 20
                    self.boat8.moves -= 1
                    time.sleep(0.2)

    def turnturn1(self):
        if self.boat1.defense == False:
            self.boat_turn = 1
        else:
            self.boat_turn = 2

    def turnturn2(self):
        if self.boat2.defense == False:
            self.boat_turn = 3
        else:
            self.boat_turn = 4

    def turnturn3(self):
        if self.boat3.defense == False:
            self.boat_turn = 5
        else:
            self.boat_turn = 6

    def turnturn4(self):
        if self.boat4.defense == False:
            self.boat_turn = 7
        else:
            self.boat_turn = 8

    def turnturn5(self):
        if self.boat5.defense == False:
            self.boat_turn = 9
        else:
            self.boat_turn = 10

    def turnturn6(self):
        if self.boat6.defense == False:
            self.boat_turn = 11
        else:
            self.boat_turn = 12

    def turnturn7(self):
        if self.boat7.defense == False:
            self.boat_turn = 13
        else:
            self.boat_turn = 14

    def turnturn8(self):
        if self.boat8.defense == False:
            self.boat_turn = 15
        else:
            self.boat_turn = 16

    def turnboat(self):
        if self.boat_turn == 1:
            if self.boat1.moves != 0 and self.boat1.defense == False:
                self.boat1.w = 40
                self.boat1.h = 19
                self.boat1.moves -=1
                self.boat1.defense = True
        elif self.boat_turn == 2:
            if self.boat1.moves != 0 and self.boat1.defense == True:
                self.boat1.w = 19
                self.boat1.h = 40
                self.boat1.moves -= 1
                self.boat1.defense = False
        elif self.boat_turn == 3:
            if self.boat2.moves != 0 and self.boat2.defense == False:
                self.boat2.w = 40
                self.boat2.h = 19
                self.boat2.y += 20
                self.boat2.moves -=1
                self.boat2.defense = True
        elif self.boat_turn == 4:
            if self.boat2.moves != 0 and self.boat2.defense == True:
                self.boat2.w = 19
                self.boat2.h = 40
                self.boat2.y -= 20
                self.boat2.moves -= 1
                self.boat2.defense = False
        elif self.boat_turn == 5:
            if self.boat3.moves != 0 and self.boat3.defense == False:
                self.boat3.w = 60
                self.boat3.h = 19
                self.boat3.moves -=1
                self.boat3.defense = True
        elif self.boat_turn == 6:
            if self.boat3.moves != 0 and self.boat3.defense == True:
                self.boat3.w = 19
                self.boat3.h = 60
                self.boat3.moves -= 1
                self.boat3.defense = False
        elif self.boat_turn == 7:
            if self.boat4.moves != 0 and self.boat4.defense == False:
                self.boat4.w = 60
                self.boat4.h = 19
                self.boat4.y += 40
                self.boat4.moves -=1
                self.boat4.defense = True
        elif self.boat_turn == 8:
            if self.boat4.moves != 0 and self.boat4.defense == True:
                self.boat4.w = 19
                self.boat4.h = 60
                self.boat4.y -= 40
                self.boat4.moves -= 1
                self.boat4.defense = False
        elif self.boat_turn == 9:
            if self.boat5.moves != 0 and self.boat5.defense == False:
                self.boat5.w = 60
                self.boat5.h = 19
                self.boat5.moves -=1
                self.boat5.defense = True
        elif self.boat_turn == 10:
            if self.boat5.moves != 0 and self.boat5.defense == True:
                self.boat5.w = 19
                self.boat5.h = 60
                self.boat5.moves -= 1
                self.boat5.defense = False
        elif self.boat_turn == 11:
            if self.boat6.moves != 0 and self.boat6.defense == False:
                self.boat6.w = 60
                self.boat6.h = 19
                self.boat6.y += 40
                self.boat6.moves -=1
                self.boat6.defense = True
        elif self.boat_turn == 12:
            if self.boat6.moves != 0 and self.boat6.defense == True:
                self.boat6.w = 19
                self.boat6.h = 60
                self.boat6.y -= 40
                self.boat6.moves -= 1
                self.boat6.defense = False
        elif self.boat_turn == 13:
            if self.boat7.moves != 0 and self.boat7.defense == False:
                self.boat7.w = 80
                self.boat7.h = 19
                self.boat7.moves -=1
                self.boat7.defense = True
        elif self.boat_turn == 14:
            if self.boat7.moves != 0 and self.boat7.defense == True:
                self.boat7.w = 19
                self.boat7.h = 80
                self.boat7.moves -= 1
                self.boat7.defense = False
        elif self.boat_turn == 15:
            if self.boat8.moves != 0 and self.boat8.defense == False:
                self.boat8.w = 80
                self.boat8.h = 19
                self.boat8.y += 60
                self.boat8.moves -=1
                self.boat8.defense = True
        elif self.boat_turn == 16:
            if self.boat8.moves != 0 and self.boat8.defense == True:
                self.boat8.w = 19
                self.boat8.h = 80
                self.boat8.y -= 60
                self.boat8.moves -= 1
                self.boat8.defense = False

    def attackattack1(self):
        if self.boat1.defense == False:
            self.boat_attack = 1
        else:
            self.boat_attack = 2

    def attackattack2(self):
        if self.boat2.defense == False:
            self.boat_attack = 3
        else:
            self.boat_attack = 4

    def attackattack3(self):
        if self.boat3.defense == False:
            self.boat_attack = 5
        else:
            self.boat_attack = 6

    def attackattack4(self):
        if self.boat4.defense == False:
            self.boat_attack = 7
        else:
            self.boat_attack = 8

    def attackattack5(self):
        if self.boat5.defense == False:
            self.boat_attack = 9
        else:
            self.boat_attack = 10

    def attackattack6(self):
        if self.boat6.defense == False:
            self.boat_attack = 11
        else:
            self.boat_attack = 12

    def attackattack7(self):
        if self.boat7.defense == False:
            self.boat_attack = 13
        else:
            self.boat_attack = 14

    def attackattack8(self):
        if self.boat8.defense == False:
            self.boat_attack = 15
        else:
            self.boat_attack = 16

    def attackboat(self):
        if self.boat_attack == 1:
            if self.boat1.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat1.x, (self.boat1.y - 20))
                self.draw_rect(colors.bright_red, self.boat1.x, (self.boat1.y - 40))
                self.draw_rect(colors.bright_red, self.boat1.x, (self.boat1.y + 40))
                self.draw_rect(colors.bright_red, self.boat1.x, (self.boat1.y + 60))
                self.draw_rect(colors.bright_red, (self.boat1.x - 20), self.boat1.y)
                self.draw_rect(colors.bright_red, (self.boat1.x - 40), self.boat1.y)
                self.draw_rect(colors.bright_red, (self.boat1.x - 20), (self.boat1.y + 20))
                self.draw_rect(colors.bright_red, (self.boat1.x - 40), (self.boat1.y + 20))
                self.draw_rect(colors.bright_red, (self.boat1.x + 20), self.boat1.y)
                self.draw_rect(colors.bright_red, (self.boat1.x + 40), self.boat1.y)
                self.draw_rect(colors.bright_red, (self.boat1.x + 20), (self.boat1.y + 20))
                self.draw_rect(colors.bright_red, (self.boat1.x + 40), (self.boat1.y + 20))
        elif self.boat_attack == 2:
            if self.boat1.attack != 0 and self.player_attack!= 0:
                pass
        elif self.boat_attack == 3:
            if self.boat2.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y - 20))
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y - 40))
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y + 40))
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y + 60))
                self.draw_rect(colors.bright_red, (self.boat2.x - 20), self.boat2.y)
                self.draw_rect(colors.bright_red, (self.boat2.x - 40), self.boat2.y)
                self.draw_rect(colors.bright_red, (self.boat2.x - 20), (self.boat2.y + 20))
                self.draw_rect(colors.bright_red, (self.boat2.x - 40), (self.boat2.y + 20))
                self.draw_rect(colors.bright_red, (self.boat2.x + 20), self.boat2.y)
                self.draw_rect(colors.bright_red, (self.boat2.x + 40), self.boat2.y)
                self.draw_rect(colors.bright_red, (self.boat2.x + 20), (self.boat2.y + 20))
                self.draw_rect(colors.bright_red, (self.boat2.x + 40), (self.boat2.y + 20))
        elif self.boat_attack == 4:
            if self.boat2.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y - 20))
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y - 40))
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y - 60))
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y + 20))
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y + 40))
                self.draw_rect(colors.bright_red, self.boat2.x, (self.boat2.y + 60))
                self.draw_rect(colors.bright_red, self.boat2.x + 20, (self.boat2.y - 20))
                self.draw_rect(colors.bright_red, self.boat2.x + 20, (self.boat2.y - 40))
                self.draw_rect(colors.bright_red, self.boat2.x + 20, (self.boat2.y - 60))
                self.draw_rect(colors.bright_red, self.boat2.x + 20, (self.boat2.y + 20))
                self.draw_rect(colors.bright_red, self.boat2.x + 20, (self.boat2.y + 40))
                self.draw_rect(colors.bright_red, self.boat2.x + 20, (self.boat2.y + 60))
        elif self.boat_attack == 5:
            if self.boat3.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y - 20))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y - 40))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y - 60))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y + 60))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y + 80))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y + 100))
                self.draw_rect(colors.bright_red, (self.boat3.x - 20), self.boat3.y)
                self.draw_rect(colors.bright_red, (self.boat3.x - 40), self.boat3.y)
                self.draw_rect(colors.bright_red, (self.boat3.x - 60), self.boat3.y)
                self.draw_rect(colors.bright_red, (self.boat3.x - 20), (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, (self.boat3.x - 40), (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, (self.boat3.x - 60), (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, (self.boat3.x + 20), self.boat3.y)
                self.draw_rect(colors.bright_red, (self.boat3.x + 40), self.boat3.y)
                self.draw_rect(colors.bright_red, (self.boat3.x + 60), self.boat3.y)
                self.draw_rect(colors.bright_red, (self.boat3.x + 20), (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, (self.boat3.x + 40), (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, (self.boat3.x + 60), (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, (self.boat3.x + 20), (self.boat3.y + 40))
                self.draw_rect(colors.bright_red, (self.boat3.x + 40), (self.boat3.y + 40))
                self.draw_rect(colors.bright_red, (self.boat3.x + 60), (self.boat3.y + 40))
                self.draw_rect(colors.bright_red, (self.boat3.x - 20), (self.boat3.y + 40))
                self.draw_rect(colors.bright_red, (self.boat3.x - 40), (self.boat3.y + 40))
                self.draw_rect(colors.bright_red, (self.boat3.x - 60), (self.boat3.y + 40))
        elif self.boat_attack == 6:
            if self.boat3.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y - 20))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y - 40))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y - 60))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y - 80))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y + 40))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y + 60))
                self.draw_rect(colors.bright_red, self.boat3.x, (self.boat3.y + 80))
                self.draw_rect(colors.bright_red, self.boat3.x + 20, (self.boat3.y - 20))
                self.draw_rect(colors.bright_red, self.boat3.x + 20, (self.boat3.y - 40))
                self.draw_rect(colors.bright_red, self.boat3.x + 20, (self.boat3.y - 60))
                self.draw_rect(colors.bright_red, self.boat3.x + 20, (self.boat3.y - 80))
                self.draw_rect(colors.bright_red, self.boat3.x + 20, (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, self.boat3.x + 20, (self.boat3.y + 40))
                self.draw_rect(colors.bright_red, self.boat3.x + 20, (self.boat3.y + 60))
                self.draw_rect(colors.bright_red, self.boat3.x + 20, (self.boat3.y + 80))
                self.draw_rect(colors.bright_red, self.boat3.x + 40, (self.boat3.y - 20))
                self.draw_rect(colors.bright_red, self.boat3.x + 40, (self.boat3.y - 40))
                self.draw_rect(colors.bright_red, self.boat3.x + 40, (self.boat3.y - 60))
                self.draw_rect(colors.bright_red, self.boat3.x + 40, (self.boat3.y - 80))
                self.draw_rect(colors.bright_red, self.boat3.x + 40, (self.boat3.y + 20))
                self.draw_rect(colors.bright_red, self.boat3.x + 40, (self.boat3.y + 40))
                self.draw_rect(colors.bright_red, self.boat3.x + 40, (self.boat3.y + 60))
                self.draw_rect(colors.bright_red, self.boat3.x + 40, (self.boat3.y + 80))
        elif self.boat_attack == 7:
            if self.boat4.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y - 20))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y - 40))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y - 60))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y + 60))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y + 80))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y + 100))
                self.draw_rect(colors.bright_red, (self.boat4.x - 20), self.boat4.y)
                self.draw_rect(colors.bright_red, (self.boat4.x - 40), self.boat4.y)
                self.draw_rect(colors.bright_red, (self.boat4.x - 60), self.boat4.y)
                self.draw_rect(colors.bright_red, (self.boat4.x - 20), (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, (self.boat4.x - 40), (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, (self.boat4.x - 60), (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, (self.boat4.x + 20), self.boat4.y)
                self.draw_rect(colors.bright_red, (self.boat4.x + 40), self.boat4.y)
                self.draw_rect(colors.bright_red, (self.boat4.x + 60), self.boat4.y)
                self.draw_rect(colors.bright_red, (self.boat4.x + 20), (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, (self.boat4.x + 40), (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, (self.boat4.x + 60), (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, (self.boat4.x + 20), (self.boat4.y + 40))
                self.draw_rect(colors.bright_red, (self.boat4.x + 40), (self.boat4.y + 40))
                self.draw_rect(colors.bright_red, (self.boat4.x + 60), (self.boat4.y + 40))
                self.draw_rect(colors.bright_red, (self.boat4.x - 20), (self.boat4.y + 40))
                self.draw_rect(colors.bright_red, (self.boat4.x - 40), (self.boat4.y + 40))
                self.draw_rect(colors.bright_red, (self.boat4.x - 60), (self.boat4.y + 40))
        elif self.boat_attack == 8:
            if self.boat4.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y - 20))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y - 40))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y - 60))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y - 80))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y + 40))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y + 60))
                self.draw_rect(colors.bright_red, self.boat4.x, (self.boat4.y + 80))
                self.draw_rect(colors.bright_red, self.boat4.x + 20, (self.boat4.y - 20))
                self.draw_rect(colors.bright_red, self.boat4.x + 20, (self.boat4.y - 40))
                self.draw_rect(colors.bright_red, self.boat4.x + 20, (self.boat4.y - 60))
                self.draw_rect(colors.bright_red, self.boat4.x + 20, (self.boat4.y - 80))
                self.draw_rect(colors.bright_red, self.boat4.x + 20, (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, self.boat4.x + 20, (self.boat4.y + 40))
                self.draw_rect(colors.bright_red, self.boat4.x + 20, (self.boat4.y + 60))
                self.draw_rect(colors.bright_red, self.boat4.x + 20, (self.boat4.y + 80))
                self.draw_rect(colors.bright_red, self.boat4.x + 40, (self.boat4.y - 20))
                self.draw_rect(colors.bright_red, self.boat4.x + 40, (self.boat4.y - 40))
                self.draw_rect(colors.bright_red, self.boat4.x + 40, (self.boat4.y - 60))
                self.draw_rect(colors.bright_red, self.boat4.x + 40, (self.boat4.y - 80))
                self.draw_rect(colors.bright_red, self.boat4.x + 40, (self.boat4.y + 20))
                self.draw_rect(colors.bright_red, self.boat4.x + 40, (self.boat4.y + 40))
                self.draw_rect(colors.bright_red, self.boat4.x + 40, (self.boat4.y + 60))
                self.draw_rect(colors.bright_red, self.boat4.x + 40, (self.boat4.y + 80))
        elif self.boat_attack == 9:
            if self.boat5.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y - 20))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y - 40))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y - 60))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y + 60))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y + 80))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y + 100))
                self.draw_rect(colors.bright_red, (self.boat5.x - 20), self.boat5.y)
                self.draw_rect(colors.bright_red, (self.boat5.x - 40), self.boat5.y)
                self.draw_rect(colors.bright_red, (self.boat5.x - 60), self.boat5.y)
                self.draw_rect(colors.bright_red, (self.boat5.x - 20), (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, (self.boat5.x - 40), (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, (self.boat5.x - 60), (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, (self.boat5.x + 20), self.boat5.y)
                self.draw_rect(colors.bright_red, (self.boat5.x + 40), self.boat5.y)
                self.draw_rect(colors.bright_red, (self.boat5.x + 60), self.boat5.y)
                self.draw_rect(colors.bright_red, (self.boat5.x + 20), (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, (self.boat5.x + 40), (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, (self.boat5.x + 60), (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, (self.boat5.x + 20), (self.boat5.y + 40))
                self.draw_rect(colors.bright_red, (self.boat5.x + 40), (self.boat5.y + 40))
                self.draw_rect(colors.bright_red, (self.boat5.x + 60), (self.boat5.y + 40))
                self.draw_rect(colors.bright_red, (self.boat5.x - 20), (self.boat5.y + 40))
                self.draw_rect(colors.bright_red, (self.boat5.x - 40), (self.boat5.y + 40))
                self.draw_rect(colors.bright_red, (self.boat5.x - 60), (self.boat5.y + 40))
        elif self.boat_attack == 10:
            if self.boat5.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y - 20))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y - 40))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y - 60))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y - 80))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y + 40))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y + 60))
                self.draw_rect(colors.bright_red, self.boat5.x, (self.boat5.y + 80))
                self.draw_rect(colors.bright_red, self.boat5.x + 20, (self.boat5.y - 20))
                self.draw_rect(colors.bright_red, self.boat5.x + 20, (self.boat5.y - 40))
                self.draw_rect(colors.bright_red, self.boat5.x + 20, (self.boat5.y - 60))
                self.draw_rect(colors.bright_red, self.boat5.x + 20, (self.boat5.y - 80))
                self.draw_rect(colors.bright_red, self.boat5.x + 20, (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, self.boat5.x + 20, (self.boat5.y + 40))
                self.draw_rect(colors.bright_red, self.boat5.x + 20, (self.boat5.y + 60))
                self.draw_rect(colors.bright_red, self.boat5.x + 20, (self.boat5.y + 80))
                self.draw_rect(colors.bright_red, self.boat5.x + 40, (self.boat5.y - 20))
                self.draw_rect(colors.bright_red, self.boat5.x + 40, (self.boat5.y - 40))
                self.draw_rect(colors.bright_red, self.boat5.x + 40, (self.boat5.y - 60))
                self.draw_rect(colors.bright_red, self.boat5.x + 40, (self.boat5.y - 80))
                self.draw_rect(colors.bright_red, self.boat5.x + 40, (self.boat5.y + 20))
                self.draw_rect(colors.bright_red, self.boat5.x + 40, (self.boat5.y + 40))
                self.draw_rect(colors.bright_red, self.boat5.x + 40, (self.boat5.y + 60))
                self.draw_rect(colors.bright_red, self.boat5.x + 40, (self.boat5.y + 80))
        elif self.boat_attack == 11:
            if self.boat6.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y - 20))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y - 40))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y - 60))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y + 60))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y + 80))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y + 100))
                self.draw_rect(colors.bright_red, (self.boat6.x - 20), self.boat6.y)
                self.draw_rect(colors.bright_red, (self.boat6.x - 40), self.boat6.y)
                self.draw_rect(colors.bright_red, (self.boat6.x - 60), self.boat6.y)
                self.draw_rect(colors.bright_red, (self.boat6.x - 20), (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, (self.boat6.x - 40), (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, (self.boat6.x - 60), (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, (self.boat6.x + 20), self.boat6.y)
                self.draw_rect(colors.bright_red, (self.boat6.x + 40), self.boat6.y)
                self.draw_rect(colors.bright_red, (self.boat6.x + 60), self.boat6.y)
                self.draw_rect(colors.bright_red, (self.boat6.x + 20), (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, (self.boat6.x + 40), (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, (self.boat6.x + 60), (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, (self.boat6.x + 20), (self.boat6.y + 40))
                self.draw_rect(colors.bright_red, (self.boat6.x + 40), (self.boat6.y + 40))
                self.draw_rect(colors.bright_red, (self.boat6.x + 60), (self.boat6.y + 40))
                self.draw_rect(colors.bright_red, (self.boat6.x - 20), (self.boat6.y + 40))
                self.draw_rect(colors.bright_red, (self.boat6.x - 40), (self.boat6.y + 40))
                self.draw_rect(colors.bright_red, (self.boat6.x - 60), (self.boat6.y + 40))
        elif self.boat_attack == 12:
            if self.boat6.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y - 20))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y - 40))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y - 60))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y - 80))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y + 40))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y + 60))
                self.draw_rect(colors.bright_red, self.boat6.x, (self.boat6.y + 80))
                self.draw_rect(colors.bright_red, self.boat6.x + 20, (self.boat6.y - 20))
                self.draw_rect(colors.bright_red, self.boat6.x + 20, (self.boat6.y - 40))
                self.draw_rect(colors.bright_red, self.boat6.x + 20, (self.boat6.y - 60))
                self.draw_rect(colors.bright_red, self.boat6.x + 20, (self.boat6.y - 80))
                self.draw_rect(colors.bright_red, self.boat6.x + 20, (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, self.boat6.x + 20, (self.boat6.y + 40))
                self.draw_rect(colors.bright_red, self.boat6.x + 20, (self.boat6.y + 60))
                self.draw_rect(colors.bright_red, self.boat6.x + 20, (self.boat6.y + 80))
                self.draw_rect(colors.bright_red, self.boat6.x + 40, (self.boat6.y - 20))
                self.draw_rect(colors.bright_red, self.boat6.x + 40, (self.boat6.y - 40))
                self.draw_rect(colors.bright_red, self.boat6.x + 40, (self.boat6.y - 60))
                self.draw_rect(colors.bright_red, self.boat6.x + 40, (self.boat6.y - 80))
                self.draw_rect(colors.bright_red, self.boat6.x + 40, (self.boat6.y + 20))
                self.draw_rect(colors.bright_red, self.boat6.x + 40, (self.boat6.y + 40))
                self.draw_rect(colors.bright_red, self.boat6.x + 40, (self.boat6.y + 60))
                self.draw_rect(colors.bright_red, self.boat6.x + 40, (self.boat6.y + 80))
        elif self.boat_attack == 13:
            if self.boat7.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 20))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 40))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 60))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 80))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 80))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 100))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 270))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 315))
                self.draw_rect(colors.bright_red, (self.boat7.x - 20), self.boat7.y)
                self.draw_rect(colors.bright_red, (self.boat7.x - 40), self.boat7.y)
                self.draw_rect(colors.bright_red, (self.boat7.x - 60), self.boat7.y)
                self.draw_rect(colors.bright_red, (self.boat7.x - 80), self.boat7.y)
                self.draw_rect(colors.bright_red, (self.boat7.x - 20), (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, (self.boat7.x - 40), (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, (self.boat7.x - 60), (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, (self.boat7.x - 80), (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, (self.boat7.x + 20), self.boat7.y)
                self.draw_rect(colors.bright_red, (self.boat7.x + 40), self.boat7.y)
                self.draw_rect(colors.bright_red, (self.boat7.x + 60), self.boat7.y)
                self.draw_rect(colors.bright_red, (self.boat7.x + 80), self.boat7.y)
                self.draw_rect(colors.bright_red, (self.boat7.x + 20), (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, (self.boat7.x + 40), (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, (self.boat7.x + 60), (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, (self.boat7.x + 80), (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, (self.boat7.x + 20), (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, (self.boat7.x + 40), (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, (self.boat7.x + 60), (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, (self.boat7.x + 80), (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, (self.boat7.x - 20), (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, (self.boat7.x - 40), (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, (self.boat7.x - 60), (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, (self.boat7.x - 80), (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, (self.boat7.x + 20), (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, (self.boat7.x + 40), (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, (self.boat7.x + 60), (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, (self.boat7.x + 80), (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, (self.boat7.x - 20), (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, (self.boat7.x - 40), (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, (self.boat7.x - 60), (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, (self.boat7.x - 80), (self.boat7.y + 60))
        elif self.boat_attack == 14:
            if self.boat7.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 20))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 40))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 60))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 80))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y - 100))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 80))
                self.draw_rect(colors.bright_red, self.boat7.x, (self.boat7.y + 100))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y - 20))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y - 40))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y - 60))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y - 80))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y - 100))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y + 80))
                self.draw_rect(colors.bright_red, self.boat7.x + 20, (self.boat7.y + 100))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y - 20))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y - 40))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y - 60))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y - 80))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y - 100))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y + 80))
                self.draw_rect(colors.bright_red, self.boat7.x + 40, (self.boat7.y + 100))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y - 20))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y - 40))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y - 60))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y - 80))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y - 100))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y + 20))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y + 40))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y + 60))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y + 80))
                self.draw_rect(colors.bright_red, self.boat7.x + 60, (self.boat7.y + 100))
        elif self.boat_attack == 15:
            if self.boat8.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 20))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 40))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 60))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 80))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 80))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 100))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 270))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 315))
                self.draw_rect(colors.bright_red, (self.boat8.x - 20), self.boat8.y)
                self.draw_rect(colors.bright_red, (self.boat8.x - 40), self.boat8.y)
                self.draw_rect(colors.bright_red, (self.boat8.x - 60), self.boat8.y)
                self.draw_rect(colors.bright_red, (self.boat8.x - 80), self.boat8.y)
                self.draw_rect(colors.bright_red, (self.boat8.x - 20), (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, (self.boat8.x - 40), (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, (self.boat8.x - 60), (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, (self.boat8.x - 80), (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, (self.boat8.x + 20), self.boat8.y)
                self.draw_rect(colors.bright_red, (self.boat8.x + 40), self.boat8.y)
                self.draw_rect(colors.bright_red, (self.boat8.x + 60), self.boat8.y)
                self.draw_rect(colors.bright_red, (self.boat8.x + 80), self.boat8.y)
                self.draw_rect(colors.bright_red, (self.boat8.x + 20), (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, (self.boat8.x + 40), (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, (self.boat8.x + 60), (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, (self.boat8.x + 80), (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, (self.boat8.x + 20), (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, (self.boat8.x + 40), (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, (self.boat8.x + 60), (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, (self.boat8.x + 80), (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, (self.boat8.x - 20), (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, (self.boat8.x - 40), (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, (self.boat8.x - 60), (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, (self.boat8.x - 80), (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, (self.boat8.x + 20), (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, (self.boat8.x + 40), (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, (self.boat8.x + 60), (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, (self.boat8.x + 80), (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, (self.boat8.x - 20), (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, (self.boat8.x - 40), (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, (self.boat8.x - 60), (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, (self.boat8.x - 80), (self.boat8.y + 60))
        elif self.boat_attack == 16:
            if self.boat8.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 20))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 40))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 60))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 80))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y - 100))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 80))
                self.draw_rect(colors.bright_red, self.boat8.x, (self.boat8.y + 100))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y - 20))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y - 40))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y - 60))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y - 80))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y - 100))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y + 80))
                self.draw_rect(colors.bright_red, self.boat8.x + 20, (self.boat8.y + 100))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y - 20))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y - 40))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y - 60))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y - 80))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y - 100))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y + 80))
                self.draw_rect(colors.bright_red, self.boat8.x + 40, (self.boat8.y + 100))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y - 20))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y - 40))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y - 60))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y - 80))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y - 100))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y + 20))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y + 40))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y + 60))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y + 80))
                self.draw_rect(colors.bright_red, self.boat8.x + 60, (self.boat8.y + 100))

    def draw_rect(self, color, x, y):
            if x >= 200  and x < 600 and y >= 100 and y < 500:
                pygame.draw.rect(screen, color,(x, y, 19, 19))

class Boat(Player):
    def __init__(self, c, x, y, w, h, health, moves):
        self.c = c
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = health
        self.moves = moves
        self.attack = 1
        self.defense = False
    def draw(self):
        pygame.draw.ellipse(screen, self.c, (self.x, self.y, self.w, self.h))

    def update(self):
        pass


board = Board()
player = Player()

intro()
pygame.quit()
quit()

