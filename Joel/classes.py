import pygame
import colors
import images
import functions

click = pygame.mouse.get_pressed()
screen_width = 1920
screen_heigt = 1080
size = (screen_width, screen_heigt)
screen = pygame.display.set_mode(size)

class Board():
    def __init__(self):
        self.board = []
        self.w = 44
        self.h = 44
        self.c = colors.white
        
    def draw(self):
        for y in range(100,1000,45):
            for x in range(500,1400, 45):
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
            functions.text("comicsansms", 20, "Player1", 420, 120, colors.white)
        elif self.player1_turn == True:
            functions.text("comicsansms", 20, "Player1", 420, 120, colors.brigth_red)
        if self.player2_turn == False:
            functions.text("comicsansms", 20, "Player2", 1470, 120, colors.white)
        elif self.player2_turn == True:
            functions.text("comicsansms", 20, "Player2", 1470, 120, colors.brigth_blue)

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
                if click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400:
                    self.beurt += 1
                    self.player1_turn = False
                    self.player2_turn = True
                    if self.beurt == 1:                    
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat1 = Boat(colors.brigth_red, x, 910, 44, 90, 2, 3)
                        self.boat1_draw = True                        
                    elif self.beurt == 3:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat3 = Boat(colors.brigth_red, x, 865, 44, 135, 3, 2)
                        self.boat3_draw = True
                    elif self.beurt == 5:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat5 = Boat(colors.brigth_red, x, 865, 44, 135, 3, 2)
                        self.boat5_draw = True
                    elif self.beurt == 7:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat7 = Boat(colors.brigth_red, x, 820, 44, 180, 4, 1)
                        self.boat7_draw = True
            elif self.player2_turn == True:
                if click[0] and mouse[1] > 100 and mouse [1] < 145 and mouse[0] > 500 and mouse [0] < 1400:
                    self.beurt += 1
                    self.player2_turn = False
                    self.player1_turn = True
                    if self.beurt == 2:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat2 = Boat(colors.brigth_blue, x, 100, 44, 90, 2, 3)
                        self.boat2_draw = True
                    elif self.beurt == 4:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat4 = Boat(colors.brigth_blue, x, 100, 44, 135, 3, 2)
                        self.boat4_draw = True
                    elif self.beurt == 6:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat6 = Boat(colors.brigth_blue, x, 100, 44, 135, 3, 2)
                        self.boat6_draw = True
                    elif self.beurt == 8:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat8 = Boat(colors.brigth_blue, x, 100, 44, 180, 4, 1)
                        self.boat8_draw = True
        else:
            if self.player1_turn == True:
                functions.button("move", 350, 800, 150, 50, colors.green, colors.brigth_green, None)
                functions.button("turn", 350, 850, 150, 50, colors.snow, colors.brigth_snow, None)
                functions.button("attack", 350, 900, 150, 50, colors.yellow, colors.brigth_yellow, None)
                functions.button("end turn", 350, 950, 150, 50, colors.red, colors.brigth_red, self.name1)
                functions.text("comicsansms",20, "boat 1 health:" + str(self.boat1.health), 400, 400, colors.brigth_red)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat1.moves), 400, 450, colors.red)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat3.health), 400, 500, colors.brigth_red)
                functions.text("comicsansms",20, "boat 2 moves:" + str(self.boat3.moves), 400, 550, colors.red)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat5.health), 400, 600, colors.brigth_red)
                functions.text("comicsansms",20, "boat 3 moves:" + str(self.boat5.moves), 400, 650, colors.red)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat7.health), 400, 700, colors.brigth_red)
                functions.text("comicsansms",20, "boat 4 moves:" + str(self.boat7.moves), 400, 750, colors.red)
            elif self.player2_turn == True:
                functions.button("move", 1400, 800, 150, 50, colors.green, colors.brigth_green, None)
                functions.button("turn", 1400, 850, 150, 50, colors.snow, colors.brigth_snow, None)
                functions.button("attack", 1400, 900, 150, 50, colors.yellow, colors.brigth_yellow, None)
                functions.button("end turn", 1400, 950, 150, 50, colors.red, colors.brigth_red, self.name2)
                functions.text("comicsansms",20, "boat 1 health:" + str(self.boat2.health), 1480, 400, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat2.moves), 1480, 450, colors.blue)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat4.health), 1480, 500, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat4.moves), 1480, 550, colors.blue)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat6.health), 1480, 600, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat6.moves), 1480, 650, colors.blue)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat8.health), 1480, 700, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 4 moves:" + str(self.boat8.moves), 1480, 750, colors.blue)

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