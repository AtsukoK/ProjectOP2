import pygame
import colors
import images
import functions
import time

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

        self.boat1_width_1 = 1920
        self.boat1_width_2 = 0
        self.boat2_width_1 = 1920
        self.boat2_width_2 = 0
        self.boat3_width_1 = 1920
        self.boat3_width_2 = 0
        self.boat4_width_1 = 1920
        self.boat4_width_2 = 0
        self.boat5_width_1 = 1920
        self.boat5_width_2 = 0
        self.boat6_width_1 = 1920
        self.boat6_width_2 = 0

        self.move1_def = False
        self.turn1_def = False
        self.attack1_def = False
        self.move2_def = False
        self.turn2_def = False
        self.attack2_def = False

        self.boat_move = 0

        self.player_attack = 2

        self.thing = 0

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
        self.boat1.moves = 3
        self.boat3.moves = 2
        self.boat5.moves = 2
        self.boat7.moves = 1
        self.boat1.attack = 1
        self.boat3.attack = 1
        self.boat5.attack = 1
        self.boat7.attack = 1
        self.boat_move = 0
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
        self.boat_move = 0
        self.base_color()
        self.player_attack = 2
        self.thing = 0

    def update(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if self.beurt <8:
            if self.player1_turn == True:
                if click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] < self.boat1_width_1 and mouse[0] < self.boat3_width_1 and mouse[0] < self.boat5_width_1 \
                or click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] > self.boat1_width_2 and mouse[0] > self.boat3_width_2 and mouse[0] > self.boat5_width_2 \
                or click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] < self.boat1_width_1 and mouse[0] < self.boat3_width_1 and mouse[0] > self.boat5_width_2 \
                or click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] < self.boat1_width_1 and mouse[0] > self.boat3_width_2 and mouse[0] > self.boat5_width_2 \
                or click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] < self.boat1_width_1 and mouse[0] > self.boat3_width_2 and mouse[0] < self.boat5_width_1 \
                or click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] > self.boat1_width_2 and mouse[0] < self.boat3_width_1 and mouse[0] < self.boat5_width_1 \
                or click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] > self.boat1_width_2 and mouse[0] < self.boat3_width_1 and mouse[0] > self.boat5_width_2 \
                or click[0] and mouse[1] > 955 and mouse[1] < 1000 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] > self.boat1_width_2 and mouse[0] > self.boat3_width_2 and mouse[0] < self.boat5_width_1:

                    self.beurt += 1
                    self.player1_turn = False
                    self.player2_turn = True
                    if self.beurt == 1:                    
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat1 = Boat(colors.red, x, 910, 44, 90, 2, 3)
                        self.boat1_draw = True                        
                    elif self.beurt == 3:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat3 = Boat(colors.red, x, 865, 44, 135, 3, 2)
                        self.boat3_draw = True
                    elif self.beurt == 5:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat5 = Boat(colors.red, x, 865, 44, 135, 3, 2)
                        self.boat5_draw = True
                    elif self.beurt == 7:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat7 = Boat(colors.red, x, 820, 44, 180, 4, 1)
                        self.boat7_draw = True
            elif self.player2_turn == True:
                if click[0] and mouse[1] > 100 and mouse[1] < 145 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] < self.boat2_width_1 and mouse[0] < self.boat4_width_1 and mouse[0] < self.boat6_width_1 \
                or click[0] and mouse[1] > 100 and mouse[1] < 145 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] > self.boat2_width_2 and mouse[0] > self.boat4_width_2 and mouse[0] > self.boat6_width_2 \
                or click[0] and mouse[1] > 100 and mouse[1] < 145 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] < self.boat2_width_1 and mouse[0] < self.boat4_width_1 and mouse[0] > self.boat6_width_2 \
                or click[0] and mouse[1] > 100 and mouse[1] < 145 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] < self.boat2_width_1 and mouse[0] > self.boat4_width_2 and mouse[0] > self.boat6_width_2 \
                or click[0] and mouse[1] > 100 and mouse[1] < 145 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] < self.boat2_width_1 and mouse[0] > self.boat4_width_2 and mouse[0] < self.boat6_width_1 \
                or click[0] and mouse[1] > 100 and mouse[1] < 145 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] > self.boat2_width_2 and mouse[0] < self.boat4_width_1 and mouse[0] < self.boat6_width_1 \
                or click[0] and mouse[1] > 100 and mouse[1] < 145 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] > self.boat2_width_2 and mouse[0] < self.boat4_width_1 and mouse[0] > self.boat6_width_2 \
                or click[0] and mouse[1] > 100 and mouse[1] < 145 and mouse[0] > 500 and mouse [0] < 1400 and mouse[0] > self.boat2_width_2 and mouse[0] > self.boat4_width_2 and mouse[0] < self.boat6_width_1:
                    self.beurt += 1
                    self.player2_turn = False
                    self.player1_turn = True
                    if self.beurt == 2:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat2 = Boat(colors.blue, x, 100, 44, 90, 2, 3)
                        self.boat2_draw = True
                    elif self.beurt == 4:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat4 = Boat(colors.blue, x, 100, 44, 135, 3, 2)
                        self.boat4_draw = True
                    elif self.beurt == 6:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat6 = Boat(colors.blue, x, 100, 44, 135, 3, 2)
                        self.boat6_draw = True
                    elif self.beurt == 8:
                        x = mouse[0]
                        while (x - 455) % 45 != 0:
                            x -=1 
                        self.boat8 = Boat(colors.blue, x, 100, 44, 180, 4, 1)
                        self.boat8_draw = True
        else:
            if self.player1_turn == True:
                functions.button("move", 350, 800, 150, 50, colors.green, colors.brigth_green, self.move_boat1)
                functions.button("turn", 350, 850, 150, 50, colors.snow, colors.brigth_snow, self.turn_boat1)
                functions.button("attack", 350, 900, 150, 50, colors.yellow, colors.brigth_yellow, self.attack_boat1)
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
                functions.button("move", 1400, 800, 150, 50, colors.green, colors.brigth_green, self.move_boat2)
                functions.button("turn", 1400, 850, 150, 50, colors.snow, colors.brigth_snow, self.turn_boat2)
                functions.button("attack", 1400, 900, 150, 50, colors.yellow, colors.brigth_yellow, self.attack_boat2)
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
            self.boat1_width_1 = self.boat1.x
            self.boat1_width_2 = (self.boat1.x + 45)
        if self.boat2_draw == True:
            self.boat2.draw()
            self.boat2_width_1 = self.boat2.x
            self.boat2_width_2 = (self.boat2.x + 45)
        if self.boat3_draw == True:
            self.boat3.draw()
            self.boat3_width_1 = self.boat3.x
            self.boat3_width_2 = (self.boat3.x + 45)
        if self.boat4_draw == True:
            self.boat4.draw()
            self.boat4_width_1 = self.boat4.x
            self.boat4_width_2 = (self.boat4.x + 45)
        if self.boat5_draw == True:
            self.boat5.draw()
            self.boat5_width_1 = self.boat5.x
            self.boat5_width_2 = (self.boat5.x + 45)
        if self.boat6_draw == True:
            self.boat6.draw()
            self.boat6_width_1 = self.boat6.x
            self.boat6_width_2 = (self.boat6.x + 45)
        if self.boat7_draw == True:
            self.boat7.draw()
        if self.boat8_draw == True:
            self.boat8.draw()

    def move_boat1(self):
        self.thing = 1
        self.boat_move = 0
        self.base_color()

    def turn_boat1(self):
        self.thing = 2
        self.boat_move = 0
        self.base_color()

    def attack_boat1(self):
        self.thing = 3
        self.boat_move = 0
        self.base_color()

    def move1(self):
        if self.thing == 1:
            functions.button("boat 1", 200, 800, 150, 50, colors.green, colors.brigth_green, self.movemove1)
            functions.button("boat 2", 200, 850, 150, 50, colors.green, colors.brigth_green, self.movemove3)
            functions.button("boat 3", 200, 900, 150, 50, colors.green, colors.brigth_green, self.movemove5)
            functions.button("boat 4", 200, 950, 150, 50, colors.green, colors.brigth_green, self.movemove7)

    def turn1(self):
        if self.thing == 2:
            functions.button("boat 1", 200, 800, 150, 50, colors.snow, colors.brigth_snow, None)
            functions.button("boat 2", 200, 850, 150, 50, colors.snow, colors.brigth_snow, None)
            functions.button("boat 3", 200, 900, 150, 50, colors.snow, colors.brigth_snow, None)
            functions.button("boat 4", 200, 950, 150, 50, colors.snow, colors.brigth_snow, None)

    def attack1(self):
        if self.thing == 3:
            functions.button("boat 1", 200, 800, 150, 50, colors.yellow, colors.brigth_yellow, None)
            functions.button("boat 2", 200, 850, 150, 50, colors.yellow, colors.brigth_yellow, None)
            functions.button("boat 3", 200, 900, 150, 50, colors.yellow, colors.brigth_yellow, None)
            functions.button("boat 4", 200, 950, 150, 50, colors.yellow, colors.brigth_yellow, None)

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
            functions.button("boat 1", 1550, 800, 150, 50, colors.green, colors.brigth_green, self.movemove2)
            functions.button("boat 2", 1550, 850, 150, 50, colors.green, colors.brigth_green, self.movemove4)
            functions.button("boat 3", 1550, 900, 150, 50, colors.green, colors.brigth_green, self.movemove6)
            functions.button("boat 4", 1550, 950, 150, 50, colors.green, colors.brigth_green, self.movemove8)

    def turn2(self):
        if self.thing == 5:
            functions.button("boat 1", 1550, 800, 150, 50, colors.snow, colors.brigth_snow, None)
            functions.button("boat 2", 1550, 850, 150, 50, colors.snow, colors.brigth_snow, None)
            functions.button("boat 3", 1550, 900, 150, 50, colors.snow, colors.brigth_snow, None)
            functions.button("boat 4", 1550, 950, 150, 50, colors.snow, colors.brigth_snow, None)

    def attack2(self):
        if self.thing == 6:
            functions.button("boat 1", 1550, 800, 150, 50, colors.yellow, colors.brigth_yellow, None)
            functions.button("boat 2", 1550, 850, 150, 50, colors.yellow, colors.brigth_yellow, None)
            functions.button("boat 3", 1550, 900, 150, 50, colors.yellow, colors.brigth_yellow, None)
            functions.button("boat 4", 1550, 950, 150, 50, colors.yellow, colors.brigth_yellow, None)

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
        if self.boat_move == 1 and self.boat1.defense == False:
            self.boat1.c = colors.brigth_red
            if self.boat1.moves != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.boat1.x -= 45
                    self.boat1.moves -= 1
                    if self.boat1.x < 500:
                        self.boat1.x += 45
                        self.boat1.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.boat1.x += 45
                    self.boat1.moves -= 1
                    if self.boat1.x > 1356:
                        self.boat1.x -= 45
                        self.boat1.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.boat1.y += 45
                    self.boat1.moves -= 1
                    if self.boat1.y > 910:
                        self.boat1.y -= 45
                        self.boat1.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.boat1.y -= 45
                    self.boat1.moves -= 1
                    if self.boat1.y < 100:
                        self.boat1.y += 45
                        self.boat1.moves +=1
                    time.sleep(0.2)
        elif self.boat_move == 2 and self.boat2.defense == False:
            self.boat2.c = colors.brigth_blue
            if self.boat2.moves != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.boat2.x -= 45
                    self.boat2.moves -= 1
                    if self.boat2.x < 500:
                        self.boat2.x += 45
                        self.boat2.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.boat2.x += 45
                    self.boat2.moves -= 1
                    if self.boat2.x > 1356:
                        self.boat2.x -= 45
                        self.boat2.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.boat2.y += 45
                    self.boat2.moves -= 1
                    if self.boat2.y > 910:
                        self.boat2.y -= 45
                        self.boat2.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.boat2.y -= 45
                    self.boat2.moves -= 1
                    if self.boat2.y < 100:
                        self.boat2.y += 45
                        self.boat2.moves +=1
                    time.sleep(0.2)
        elif self.boat_move == 3 and self.boat3.defense == False:
            self.boat3.c = colors.brigth_red
            if self.boat3.moves != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.boat3.x -= 45
                    self.boat3.moves -= 1
                    if self.boat3.x < 500:
                        self.boat3.x += 45
                        self.boat3.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.boat3.x += 45
                    self.boat3.moves -= 1
                    if self.boat3.x > 1356:
                        self.boat3.x -= 45
                        self.boat3.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.boat3.y += 45
                    self.boat3.moves -= 1
                    if self.boat3.y > 865:
                        self.boat3.y -= 45
                        self.boat3.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.boat3.y -= 45
                    self.boat3.moves -= 1
                    if self.boat3.y < 100:
                        self.boat3.y += 45
                        self.boat3.moves +=1
                    time.sleep(0.2)
        elif self.boat_move == 4 and self.boat4.defense == False:
            self.boat4.c = colors.brigth_blue
            if self.boat4.moves != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.boat4.x -= 45
                    self.boat4.moves -= 1
                    if self.boat4.x < 500:
                        self.boat4.x += 45
                        self.boat4.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.boat4.x += 45
                    self.boat4.moves -= 1
                    if self.boat4.x > 1356:
                        self.boat4.x -= 45
                        self.boat4.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.boat4.y += 45
                    self.boat4.moves -= 1
                    if self.boat4.y > 865:
                        self.boat4.y -= 45
                        self.boat4.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.boat4.y -= 45
                    self.boat4.moves -= 1
                    if self.boat4.y < 100:
                        self.boat4.y += 45
                        self.boat4.moves +=1
                    time.sleep(0.2)
        elif self.boat_move == 5 and self.boat5.defense == False:
            self.boat5.c = colors.brigth_red
            if self.boat5.moves != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.boat5.x -= 45
                    self.boat5.moves -= 1
                    if self.boat5.x < 500:
                        self.boat5.x += 45
                        self.boat5.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.boat5.x += 45
                    self.boat5.moves -= 1
                    if self.boat5.x > 1356:
                        self.boat5.x -= 45
                        self.boat5.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.boat5.y += 45
                    self.boat5.moves -= 1
                    if self.boat5.y > 865:
                        self.boat5.y -= 45
                        self.boat5.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.boat5.y -= 45
                    self.boat5.moves -= 1
                    if self.boat5.y < 100:
                        self.boat5.y += 45
                        self.boat5.moves +=1
                    time.sleep(0.2)
        elif self.boat_move == 6 and self.boat6.defense == False:
            self.boat6.c = colors.brigth_blue
            if self.boat6.moves != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.boat6.x -= 45
                    self.boat6.moves -= 1
                    if self.boat6.x < 500:
                        self.boat6.x += 45
                        self.boat6.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.boat6.x += 45
                    self.boat6.moves -= 1
                    if self.boat6.x > 1356:
                        self.boat6.x -= 45
                        self.boat6.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.boat6.y += 45
                    self.boat6.moves -= 1
                    if self.boat6.y > 865:
                        self.boat6.y -= 45
                        self.boat6.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.boat6.y -= 45
                    self.boat6.moves -= 1
                    if self.boat6.y < 100:
                        self.boat6.y += 45
                        self.boat6.moves +=1
                    time.sleep(0.2)
        elif self.boat_move == 7 and self.boat7.defense == False:
            self.boat7.c = colors.brigth_red
            if self.boat7.moves != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.boat7.x -= 45
                    self.boat7.moves -= 1
                    if self.boat7.x < 500:
                        self.boat7.x += 45
                        self.boat7.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.boat7.x += 45
                    self.boat7.moves -= 1
                    if self.boat7.x > 1356:
                        self.boat7.x -= 45
                        self.boat7.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.boat7.y += 45
                    self.boat7.moves -= 1
                    if self.boat7.y > 820:
                        self.boat7.y -= 45
                        self.boat7.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.boat7.y -= 45
                    self.boat7.moves -= 1
                    if self.boat7.y < 100:
                        self.boat7.y += 45
                        self.boat7.moves +=1
                    time.sleep(0.2)
        elif self.boat_move == 8 and self.boat8.defense == False:
            self.boat8.c = colors.brigth_blue
            if self.boat8.moves != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.boat8.x -= 45
                    self.boat8.moves -= 1
                    if self.boat8.x < 500:
                        self.boat8.x += 45
                        self.boat8.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.boat8.x += 45
                    self.boat8.moves -= 1
                    if self.boat8.x > 1356:
                        self.boat8.x -= 45
                        self.boat8.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.boat8.y += 45
                    self.boat8.moves -= 1
                    if self.boat8.y > 820:
                        self.boat8.y -= 45
                        self.boat8.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.boat8.y -= 45
                    self.boat8.moves -= 1
                    if self.boat8.y < 100:
                        self.boat8.y += 45
                        self.boat8.moves +=1
                    time.sleep(0.2)


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