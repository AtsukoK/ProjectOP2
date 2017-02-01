import pygame
import colors
import images
import functions
import time

click = pygame.mouse.get_pressed()
mouse = pygame.mouse.get_pos()
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
        self.boat_turn = 0
        self.boat_attack = 0

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
                functions.text("comicsansms",20, "boat 1 health:" + str(self.boat1.health), 400, 220, colors.brigth_red)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat1.moves), 400, 270, colors.medium_red)
                functions.text("comicsansms",20, "boat 1 attacks:" + str(self.boat1.attack), 400, 320, colors.red)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat3.health), 400, 370, colors.brigth_red)
                functions.text("comicsansms",20, "boat 2 moves:" + str(self.boat3.moves), 400, 420, colors.medium_red)
                functions.text("comicsansms",20, "boat 2 attacks:" + str(self.boat3.attack), 400, 470, colors.red)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat5.health), 400, 520, colors.brigth_red)
                functions.text("comicsansms",20, "boat 3 moves:" + str(self.boat5.moves), 400, 570, colors.medium_red)
                functions.text("comicsansms",20, "boat 3 attacks:" + str(self.boat5.attack), 400, 620, colors.red)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat7.health), 400, 670, colors.brigth_red)
                functions.text("comicsansms",20, "boat 4 moves:" + str(self.boat7.moves), 400, 720, colors.medium_red)
                functions.text("comicsansms",20, "boat 4 attacks:" + str(self.boat7.attack), 400, 770, colors.red)
                functions.text("comicsansms",20, "attacks left:" + str(self.player_attack), 420, 170, colors.brigth_red)
                functions.text("comicsansms",20, "boat 1 health:" + str(self.boat2.health), 1480, 220, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat4.health), 1480, 270, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat6.health), 1480, 320, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat8.health), 1480, 370, colors.brigth_blue)
            elif self.player2_turn == True:
                functions.button("move", 1400, 800, 150, 50, colors.green, colors.brigth_green, self.move_boat2)
                functions.button("turn", 1400, 850, 150, 50, colors.snow, colors.brigth_snow, self.turn_boat2)
                functions.button("attack", 1400, 900, 150, 50, colors.yellow, colors.brigth_yellow, self.attack_boat2)
                functions.button("end turn", 1400, 950, 150, 50, colors.red, colors.brigth_red, self.name2)
                functions.text("comicsansms",20, "boat 1 health:" + str(self.boat2.health), 1480, 220, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 1 moves:" + str(self.boat2.moves), 1480, 270, colors.medium_blue)
                functions.text("comicsansms",20, "boat 1 attacks:" + str(self.boat2.attack), 1480, 320, colors.blue)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat4.health), 1480, 370, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 2 moves:" + str(self.boat4.moves), 1480, 420, colors.medium_blue)
                functions.text("comicsansms",20, "boat 2 attacks:" + str(self.boat4.attack), 1480, 470, colors.blue)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat6.health), 1480, 520, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 3 moves:" + str(self.boat6.moves), 1480, 570, colors.medium_blue)
                functions.text("comicsansms",20, "boat 3 attacks:" + str(self.boat6.attack), 1480, 620, colors.blue)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat8.health), 1480, 670, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 4 moves:" + str(self.boat8.moves), 1480, 720, colors.medium_blue)
                functions.text("comicsansms",20, "boat 4 attacks:" + str(self.boat8.attack), 1480, 770, colors.blue)
                functions.text("comicsansms",20, "attacks left:" + str(self.player_attack), 1470, 170, colors.brigth_blue)
                functions.text("comicsansms",20, "boat 1 health:" + str(self.boat1.health), 400, 220, colors.brigth_red)
                functions.text("comicsansms",20, "boat 2 health:" + str(self.boat3.health), 400, 270, colors.brigth_red)
                functions.text("comicsansms",20, "boat 3 health:" + str(self.boat5.health), 400, 320, colors.brigth_red)
                functions.text("comicsansms",20, "boat 4 health:" + str(self.boat7.health), 400, 370, colors.brigth_red)

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
            functions.button("boat 1", 200, 800, 150, 50, colors.green, colors.brigth_green, self.movemove1)
            functions.button("boat 2", 200, 850, 150, 50, colors.green, colors.brigth_green, self.movemove3)
            functions.button("boat 3", 200, 900, 150, 50, colors.green, colors.brigth_green, self.movemove5)
            functions.button("boat 4", 200, 950, 150, 50, colors.green, colors.brigth_green, self.movemove7)

    def turn1(self):
        if self.thing == 2:
            functions.button("boat 1", 200, 800, 150, 50, colors.snow, colors.brigth_snow, self.turnturn1)
            functions.button("boat 2", 200, 850, 150, 50, colors.snow, colors.brigth_snow, self.turnturn3)
            functions.button("boat 3", 200, 900, 150, 50, colors.snow, colors.brigth_snow, self.turnturn5)
            functions.button("boat 4", 200, 950, 150, 50, colors.snow, colors.brigth_snow, self.turnturn7)

    def attack1(self):
        if self.thing == 3:
            functions.button("boat 1", 200, 800, 150, 50, colors.yellow, colors.brigth_yellow, self.attackattack1)
            functions.button("boat 2", 200, 850, 150, 50, colors.yellow, colors.brigth_yellow, self.attackattack3)
            functions.button("boat 3", 200, 900, 150, 50, colors.yellow, colors.brigth_yellow, self.attackattack5)
            functions.button("boat 4", 200, 950, 150, 50, colors.yellow, colors.brigth_yellow, self.attackattack7)

    def move_boat2(self):
        self.thing = 4
        self.boat_move = 0
        self.boat_attack = 0
        self.base_color()

    def turn_boat2(self):
        self.thing = 5
        self.boat_move = 0
        self.boat_attack = 0
        self.base_color()

    def attack_boat2(self):
        self.thing = 6
        self.boat_move = 0
        self.boat_attack = 0
        self.base_color()

    def move2(self):
        if self.thing == 4:
            functions.button("boat 1", 1550, 800, 150, 50, colors.green, colors.brigth_green, self.movemove2)
            functions.button("boat 2", 1550, 850, 150, 50, colors.green, colors.brigth_green, self.movemove4)
            functions.button("boat 3", 1550, 900, 150, 50, colors.green, colors.brigth_green, self.movemove6)
            functions.button("boat 4", 1550, 950, 150, 50, colors.green, colors.brigth_green, self.movemove8)

    def turn2(self):
        if self.thing == 5:
            functions.button("boat 1", 1550, 800, 150, 50, colors.snow, colors.brigth_snow, self.turnturn2)
            functions.button("boat 2", 1550, 850, 150, 50, colors.snow, colors.brigth_snow, self.turnturn4)
            functions.button("boat 3", 1550, 900, 150, 50, colors.snow, colors.brigth_snow, self.turnturn6)
            functions.button("boat 4", 1550, 950, 150, 50, colors.snow, colors.brigth_snow, self.turnturn8)

    def attack2(self):
        if self.thing == 6:
            functions.button("boat 1", 1550, 800, 150, 50, colors.yellow, colors.brigth_yellow, self.attackattack2)
            functions.button("boat 2", 1550, 850, 150, 50, colors.yellow, colors.brigth_yellow, self.attackattack4)
            functions.button("boat 3", 1550, 900, 150, 50, colors.yellow, colors.brigth_yellow, self.attackattack6)
            functions.button("boat 4", 1550, 950, 150, 50, colors.yellow, colors.brigth_yellow, self.attackattack8)

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
                self.boat1.w = 90
                self.boat1.h = 44
                self.boat1.moves -=1
                self.boat1.defense = True
        elif self.boat_turn == 2:
            if self.boat1.moves != 0 and self.boat1.defense == True:
                self.boat1.w = 44
                self.boat1.h = 90
                self.boat1.moves -= 1
                self.boat1.defense = False
        elif self.boat_turn == 3:
            if self.boat2.moves != 0 and self.boat2.defense == False:
                self.boat2.w = 90
                self.boat2.h = 44
                self.boat2.moves -=1
                self.boat2.defense = True
        elif self.boat_turn == 4:
            if self.boat2.moves != 0 and self.boat2.defense == True:
                self.boat2.w = 44
                self.boat2.h = 90
                self.boat2.moves -= 1
                self.boat2.defense = False
        elif self.boat_turn == 5:
            if self.boat3.moves != 0 and self.boat3.defense == False:
                self.boat3.w = 135
                self.boat3.h = 44
                self.boat3.moves -=1
                self.boat3.defense = True
        elif self.boat_turn == 6:
            if self.boat3.moves != 0 and self.boat3.defense == True:
                self.boat3.w = 44
                self.boat3.h = 135
                self.boat3.moves -= 1
                self.boat3.defense = False
        elif self.boat_turn == 7:
            if self.boat4.moves != 0 and self.boat4.defense == False:
                self.boat4.w = 135
                self.boat4.h = 44
                self.boat4.moves -=1
                self.boat4.defense = True
        elif self.boat_turn == 8:
            if self.boat4.moves != 0 and self.boat4.defense == True:
                self.boat4.w = 44
                self.boat4.h = 135
                self.boat4.moves -= 1
                self.boat4.defense = False
        elif self.boat_turn == 9:
            if self.boat5.moves != 0 and self.boat5.defense == False:
                self.boat5.w = 135
                self.boat5.h = 44
                self.boat5.moves -=1
                self.boat5.defense = True
        elif self.boat_turn == 10:
            if self.boat5.moves != 0 and self.boat5.defense == True:
                self.boat5.w = 44
                self.boat5.h = 135
                self.boat5.moves -= 1
                self.boat5.defense = False
        elif self.boat_turn == 11:
            if self.boat6.moves != 0 and self.boat6.defense == False:
                self.boat6.w = 135
                self.boat6.h = 44
                self.boat6.moves -=1
                self.boat6.defense = True
        elif self.boat_turn == 12:
            if self.boat6.moves != 0 and self.boat6.defense == True:
                self.boat6.w = 44
                self.boat6.h = 135
                self.boat6.moves -= 1
                self.boat6.defense = False
        elif self.boat_turn == 13:
            if self.boat7.moves != 0 and self.boat7.defense == False:
                self.boat7.w = 180
                self.boat7.h = 44
                self.boat7.moves -=1
                self.boat7.defense = True
        elif self.boat_turn == 14:
            if self.boat7.moves != 0 and self.boat7.defense == True:
                self.boat7.w = 44
                self.boat7.h = 180
                self.boat7.moves -= 1
                self.boat7.defense = False
        elif self.boat_turn == 15:
            if self.boat8.moves != 0 and self.boat8.defense == False:
                self.boat8.w = 180
                self.boat8.h = 44
                self.boat8.moves -=1
                self.boat8.defense = True
        elif self.boat_turn == 16:
            if self.boat8.moves != 0 and self.boat8.defense == True:
                self.boat8.w = 44
                self.boat8.h = 180
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
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y - 45))
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y - 90))
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y + 90))
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat1.x - 45), self.boat1.y)
                self.draw_rect(colors.brigth_red, (self.boat1.x - 90), self.boat1.y)
                self.draw_rect(colors.brigth_red, (self.boat1.x - 45), (self.boat1.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat1.x - 90), (self.boat1.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat1.x + 45), self.boat1.y)
                self.draw_rect(colors.brigth_red, (self.boat1.x + 90), self.boat1.y)
                self.draw_rect(colors.brigth_red, (self.boat1.x + 45), (self.boat1.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat1.x + 90), (self.boat1.y + 45))
        elif self.boat_attack == 2:
            if self.boat1.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y - 45))
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y - 90))
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y - 135))
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y + 45))
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y + 90))
                self.draw_rect(colors.brigth_red, self.boat1.x, (self.boat1.y + 135))
                self.draw_rect(colors.brigth_red, self.boat1.x + 45, (self.boat1.y - 45))
                self.draw_rect(colors.brigth_red, self.boat1.x + 45, (self.boat1.y - 90))
                self.draw_rect(colors.brigth_red, self.boat1.x + 45, (self.boat1.y - 135))
                self.draw_rect(colors.brigth_red, self.boat1.x + 45, (self.boat1.y + 45))
                self.draw_rect(colors.brigth_red, self.boat1.x + 45, (self.boat1.y + 90))
                self.draw_rect(colors.brigth_red, self.boat1.x + 45, (self.boat1.y + 135))
        elif self.boat_attack == 3:
            if self.boat2.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y - 45))
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y - 90))
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y + 90))
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat2.x - 45), self.boat2.y)
                self.draw_rect(colors.brigth_red, (self.boat2.x - 90), self.boat2.y)
                self.draw_rect(colors.brigth_red, (self.boat2.x - 45), (self.boat2.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat2.x - 90), (self.boat2.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat2.x + 45), self.boat2.y)
                self.draw_rect(colors.brigth_red, (self.boat2.x + 90), self.boat2.y)
                self.draw_rect(colors.brigth_red, (self.boat2.x + 45), (self.boat2.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat2.x + 90), (self.boat2.y + 45))
        elif self.boat_attack == 4:
            if self.boat2.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y - 45))
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y - 90))
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y - 135))
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y + 45))
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y + 90))
                self.draw_rect(colors.brigth_red, self.boat2.x, (self.boat2.y + 135))
                self.draw_rect(colors.brigth_red, self.boat2.x + 45, (self.boat2.y - 45))
                self.draw_rect(colors.brigth_red, self.boat2.x + 45, (self.boat2.y - 90))
                self.draw_rect(colors.brigth_red, self.boat2.x + 45, (self.boat2.y - 135))
                self.draw_rect(colors.brigth_red, self.boat2.x + 45, (self.boat2.y + 45))
                self.draw_rect(colors.brigth_red, self.boat2.x + 45, (self.boat2.y + 90))
                self.draw_rect(colors.brigth_red, self.boat2.x + 45, (self.boat2.y + 135))
        elif self.boat_attack == 5:
            if self.boat3.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y - 45))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y - 90))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y - 135))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y + 135))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y + 180))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y + 225))
                self.draw_rect(colors.brigth_red, (self.boat3.x - 45), self.boat3.y)
                self.draw_rect(colors.brigth_red, (self.boat3.x - 90), self.boat3.y)
                self.draw_rect(colors.brigth_red, (self.boat3.x - 135), self.boat3.y)
                self.draw_rect(colors.brigth_red, (self.boat3.x - 45), (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat3.x - 90), (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat3.x - 135), (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat3.x + 45), self.boat3.y)
                self.draw_rect(colors.brigth_red, (self.boat3.x + 90), self.boat3.y)
                self.draw_rect(colors.brigth_red, (self.boat3.x + 135), self.boat3.y)
                self.draw_rect(colors.brigth_red, (self.boat3.x + 45), (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat3.x + 90), (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat3.x + 135), (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat3.x + 45), (self.boat3.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat3.x + 90), (self.boat3.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat3.x + 135), (self.boat3.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat3.x - 45), (self.boat3.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat3.x - 90), (self.boat3.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat3.x - 135), (self.boat3.y + 90))
        elif self.boat_attack == 6:
            if self.boat3.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y - 45))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y - 90))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y - 135))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y - 180))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y + 90))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y + 135))
                self.draw_rect(colors.brigth_red, self.boat3.x, (self.boat3.y + 180))
                self.draw_rect(colors.brigth_red, self.boat3.x + 45, (self.boat3.y - 45))
                self.draw_rect(colors.brigth_red, self.boat3.x + 45, (self.boat3.y - 90))
                self.draw_rect(colors.brigth_red, self.boat3.x + 45, (self.boat3.y - 135))
                self.draw_rect(colors.brigth_red, self.boat3.x + 45, (self.boat3.y - 180))
                self.draw_rect(colors.brigth_red, self.boat3.x + 45, (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, self.boat3.x + 45, (self.boat3.y + 90))
                self.draw_rect(colors.brigth_red, self.boat3.x + 45, (self.boat3.y + 135))
                self.draw_rect(colors.brigth_red, self.boat3.x + 45, (self.boat3.y + 180))
                self.draw_rect(colors.brigth_red, self.boat3.x + 90, (self.boat3.y - 45))
                self.draw_rect(colors.brigth_red, self.boat3.x + 90, (self.boat3.y - 90))
                self.draw_rect(colors.brigth_red, self.boat3.x + 90, (self.boat3.y - 135))
                self.draw_rect(colors.brigth_red, self.boat3.x + 90, (self.boat3.y - 180))
                self.draw_rect(colors.brigth_red, self.boat3.x + 90, (self.boat3.y + 45))
                self.draw_rect(colors.brigth_red, self.boat3.x + 90, (self.boat3.y + 90))
                self.draw_rect(colors.brigth_red, self.boat3.x + 90, (self.boat3.y + 135))
                self.draw_rect(colors.brigth_red, self.boat3.x + 90, (self.boat3.y + 180))
        elif self.boat_attack == 7:
            if self.boat4.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y - 45))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y - 90))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y - 135))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y + 135))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y + 180))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y + 225))
                self.draw_rect(colors.brigth_red, (self.boat4.x - 45), self.boat4.y)
                self.draw_rect(colors.brigth_red, (self.boat4.x - 90), self.boat4.y)
                self.draw_rect(colors.brigth_red, (self.boat4.x - 135), self.boat4.y)
                self.draw_rect(colors.brigth_red, (self.boat4.x - 45), (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat4.x - 90), (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat4.x - 135), (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat4.x + 45), self.boat4.y)
                self.draw_rect(colors.brigth_red, (self.boat4.x + 90), self.boat4.y)
                self.draw_rect(colors.brigth_red, (self.boat4.x + 135), self.boat4.y)
                self.draw_rect(colors.brigth_red, (self.boat4.x + 45), (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat4.x + 90), (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat4.x + 135), (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat4.x + 45), (self.boat4.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat4.x + 90), (self.boat4.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat4.x + 135), (self.boat4.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat4.x - 45), (self.boat4.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat4.x - 90), (self.boat4.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat4.x - 135), (self.boat4.y + 90))
        elif self.boat_attack == 8:
            if self.boat4.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y - 45))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y - 90))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y - 135))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y - 180))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y + 90))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y + 135))
                self.draw_rect(colors.brigth_red, self.boat4.x, (self.boat4.y + 180))
                self.draw_rect(colors.brigth_red, self.boat4.x + 45, (self.boat4.y - 45))
                self.draw_rect(colors.brigth_red, self.boat4.x + 45, (self.boat4.y - 90))
                self.draw_rect(colors.brigth_red, self.boat4.x + 45, (self.boat4.y - 135))
                self.draw_rect(colors.brigth_red, self.boat4.x + 45, (self.boat4.y - 180))
                self.draw_rect(colors.brigth_red, self.boat4.x + 45, (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, self.boat4.x + 45, (self.boat4.y + 90))
                self.draw_rect(colors.brigth_red, self.boat4.x + 45, (self.boat4.y + 135))
                self.draw_rect(colors.brigth_red, self.boat4.x + 45, (self.boat4.y + 180))
                self.draw_rect(colors.brigth_red, self.boat4.x + 90, (self.boat4.y - 45))
                self.draw_rect(colors.brigth_red, self.boat4.x + 90, (self.boat4.y - 90))
                self.draw_rect(colors.brigth_red, self.boat4.x + 90, (self.boat4.y - 135))
                self.draw_rect(colors.brigth_red, self.boat4.x + 90, (self.boat4.y - 180))
                self.draw_rect(colors.brigth_red, self.boat4.x + 90, (self.boat4.y + 45))
                self.draw_rect(colors.brigth_red, self.boat4.x + 90, (self.boat4.y + 90))
                self.draw_rect(colors.brigth_red, self.boat4.x + 90, (self.boat4.y + 135))
                self.draw_rect(colors.brigth_red, self.boat4.x + 90, (self.boat4.y + 180))
        elif self.boat_attack == 9:
            if self.boat5.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y - 45))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y - 90))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y - 135))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y + 135))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y + 180))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y + 225))
                self.draw_rect(colors.brigth_red, (self.boat5.x - 45), self.boat5.y)
                self.draw_rect(colors.brigth_red, (self.boat5.x - 90), self.boat5.y)
                self.draw_rect(colors.brigth_red, (self.boat5.x - 135), self.boat5.y)
                self.draw_rect(colors.brigth_red, (self.boat5.x - 45), (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat5.x - 90), (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat5.x - 135), (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat5.x + 45), self.boat5.y)
                self.draw_rect(colors.brigth_red, (self.boat5.x + 90), self.boat5.y)
                self.draw_rect(colors.brigth_red, (self.boat5.x + 135), self.boat5.y)
                self.draw_rect(colors.brigth_red, (self.boat5.x + 45), (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat5.x + 90), (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat5.x + 135), (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat5.x + 45), (self.boat5.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat5.x + 90), (self.boat5.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat5.x + 135), (self.boat5.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat5.x - 45), (self.boat5.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat5.x - 90), (self.boat5.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat5.x - 135), (self.boat5.y + 90))
        elif self.boat_attack == 10:
            if self.boat5.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y - 45))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y - 90))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y - 135))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y - 180))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y + 90))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y + 135))
                self.draw_rect(colors.brigth_red, self.boat5.x, (self.boat5.y + 180))
                self.draw_rect(colors.brigth_red, self.boat5.x + 45, (self.boat5.y - 45))
                self.draw_rect(colors.brigth_red, self.boat5.x + 45, (self.boat5.y - 90))
                self.draw_rect(colors.brigth_red, self.boat5.x + 45, (self.boat5.y - 135))
                self.draw_rect(colors.brigth_red, self.boat5.x + 45, (self.boat5.y - 180))
                self.draw_rect(colors.brigth_red, self.boat5.x + 45, (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, self.boat5.x + 45, (self.boat5.y + 90))
                self.draw_rect(colors.brigth_red, self.boat5.x + 45, (self.boat5.y + 135))
                self.draw_rect(colors.brigth_red, self.boat5.x + 45, (self.boat5.y + 180))
                self.draw_rect(colors.brigth_red, self.boat5.x + 90, (self.boat5.y - 45))
                self.draw_rect(colors.brigth_red, self.boat5.x + 90, (self.boat5.y - 90))
                self.draw_rect(colors.brigth_red, self.boat5.x + 90, (self.boat5.y - 135))
                self.draw_rect(colors.brigth_red, self.boat5.x + 90, (self.boat5.y - 180))
                self.draw_rect(colors.brigth_red, self.boat5.x + 90, (self.boat5.y + 45))
                self.draw_rect(colors.brigth_red, self.boat5.x + 90, (self.boat5.y + 90))
                self.draw_rect(colors.brigth_red, self.boat5.x + 90, (self.boat5.y + 135))
                self.draw_rect(colors.brigth_red, self.boat5.x + 90, (self.boat5.y + 180))
        elif self.boat_attack == 11:
            if self.boat6.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y - 45))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y - 90))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y - 135))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y + 135))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y + 180))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y + 225))
                self.draw_rect(colors.brigth_red, (self.boat6.x - 45), self.boat6.y)
                self.draw_rect(colors.brigth_red, (self.boat6.x - 90), self.boat6.y)
                self.draw_rect(colors.brigth_red, (self.boat6.x - 135), self.boat6.y)
                self.draw_rect(colors.brigth_red, (self.boat6.x - 45), (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat6.x - 90), (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat6.x - 135), (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat6.x + 45), self.boat6.y)
                self.draw_rect(colors.brigth_red, (self.boat6.x + 90), self.boat6.y)
                self.draw_rect(colors.brigth_red, (self.boat6.x + 135), self.boat6.y)
                self.draw_rect(colors.brigth_red, (self.boat6.x + 45), (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat6.x + 90), (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat6.x + 135), (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat6.x + 45), (self.boat6.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat6.x + 90), (self.boat6.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat6.x + 135), (self.boat6.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat6.x - 45), (self.boat6.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat6.x - 90), (self.boat6.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat6.x - 135), (self.boat6.y + 90))
        elif self.boat_attack == 12:
            if self.boat6.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y - 45))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y - 90))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y - 135))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y - 180))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y + 90))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y + 135))
                self.draw_rect(colors.brigth_red, self.boat6.x, (self.boat6.y + 180))
                self.draw_rect(colors.brigth_red, self.boat6.x + 45, (self.boat6.y - 45))
                self.draw_rect(colors.brigth_red, self.boat6.x + 45, (self.boat6.y - 90))
                self.draw_rect(colors.brigth_red, self.boat6.x + 45, (self.boat6.y - 135))
                self.draw_rect(colors.brigth_red, self.boat6.x + 45, (self.boat6.y - 180))
                self.draw_rect(colors.brigth_red, self.boat6.x + 45, (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, self.boat6.x + 45, (self.boat6.y + 90))
                self.draw_rect(colors.brigth_red, self.boat6.x + 45, (self.boat6.y + 135))
                self.draw_rect(colors.brigth_red, self.boat6.x + 45, (self.boat6.y + 180))
                self.draw_rect(colors.brigth_red, self.boat6.x + 90, (self.boat6.y - 45))
                self.draw_rect(colors.brigth_red, self.boat6.x + 90, (self.boat6.y - 90))
                self.draw_rect(colors.brigth_red, self.boat6.x + 90, (self.boat6.y - 135))
                self.draw_rect(colors.brigth_red, self.boat6.x + 90, (self.boat6.y - 180))
                self.draw_rect(colors.brigth_red, self.boat6.x + 90, (self.boat6.y + 45))
                self.draw_rect(colors.brigth_red, self.boat6.x + 90, (self.boat6.y + 90))
                self.draw_rect(colors.brigth_red, self.boat6.x + 90, (self.boat6.y + 135))
                self.draw_rect(colors.brigth_red, self.boat6.x + 90, (self.boat6.y + 180))
        elif self.boat_attack == 13:
            if self.boat7.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 45))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 90))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 135))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 180))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 180))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 225))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 270))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 315))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 45), self.boat7.y)
                self.draw_rect(colors.brigth_red, (self.boat7.x - 90), self.boat7.y)
                self.draw_rect(colors.brigth_red, (self.boat7.x - 135), self.boat7.y)
                self.draw_rect(colors.brigth_red, (self.boat7.x - 180), self.boat7.y)
                self.draw_rect(colors.brigth_red, (self.boat7.x - 45), (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 90), (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 135), (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 180), (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 45), self.boat7.y)
                self.draw_rect(colors.brigth_red, (self.boat7.x + 90), self.boat7.y)
                self.draw_rect(colors.brigth_red, (self.boat7.x + 135), self.boat7.y)
                self.draw_rect(colors.brigth_red, (self.boat7.x + 180), self.boat7.y)
                self.draw_rect(colors.brigth_red, (self.boat7.x + 45), (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 90), (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 135), (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 180), (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 45), (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 90), (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 135), (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 180), (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 45), (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 90), (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 135), (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 180), (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 45), (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 90), (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 135), (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat7.x + 180), (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 45), (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 90), (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 135), (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat7.x - 180), (self.boat7.y + 135))
        elif self.boat_attack == 14:
            if self.boat7.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 45))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 90))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 135))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 180))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y - 225))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 180))
                self.draw_rect(colors.brigth_red, self.boat7.x, (self.boat7.y + 225))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y - 45))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y - 90))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y - 135))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y - 180))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y - 225))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y + 180))
                self.draw_rect(colors.brigth_red, self.boat7.x + 45, (self.boat7.y + 225))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y - 45))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y - 90))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y - 135))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y - 180))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y - 225))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y + 180))
                self.draw_rect(colors.brigth_red, self.boat7.x + 90, (self.boat7.y + 225))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y - 45))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y - 90))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y - 135))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y - 180))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y - 225))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y + 45))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y + 90))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y + 135))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y + 180))
                self.draw_rect(colors.brigth_red, self.boat7.x + 135, (self.boat7.y + 225))
        elif self.boat_attack == 15:
            if self.boat8.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 45))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 90))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 135))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 180))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 180))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 225))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 270))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 315))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 45), self.boat8.y)
                self.draw_rect(colors.brigth_red, (self.boat8.x - 90), self.boat8.y)
                self.draw_rect(colors.brigth_red, (self.boat8.x - 135), self.boat8.y)
                self.draw_rect(colors.brigth_red, (self.boat8.x - 180), self.boat8.y)
                self.draw_rect(colors.brigth_red, (self.boat8.x - 45), (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 90), (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 135), (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 180), (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 45), self.boat8.y)
                self.draw_rect(colors.brigth_red, (self.boat8.x + 90), self.boat8.y)
                self.draw_rect(colors.brigth_red, (self.boat8.x + 135), self.boat8.y)
                self.draw_rect(colors.brigth_red, (self.boat8.x + 180), self.boat8.y)
                self.draw_rect(colors.brigth_red, (self.boat8.x + 45), (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 90), (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 135), (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 180), (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 45), (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 90), (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 135), (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 180), (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 45), (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 90), (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 135), (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 180), (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 45), (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 90), (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 135), (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat8.x + 180), (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 45), (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 90), (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 135), (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, (self.boat8.x - 180), (self.boat8.y + 135))
        elif self.boat_attack == 16:
            if self.boat8.attack != 0 and self.player_attack!= 0:
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 45))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 90))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 135))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 180))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y - 225))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 180))
                self.draw_rect(colors.brigth_red, self.boat8.x, (self.boat8.y + 225))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y - 45))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y - 90))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y - 135))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y - 180))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y - 225))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y + 180))
                self.draw_rect(colors.brigth_red, self.boat8.x + 45, (self.boat8.y + 225))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y - 45))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y - 90))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y - 135))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y - 180))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y - 225))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y + 180))
                self.draw_rect(colors.brigth_red, self.boat8.x + 90, (self.boat8.y + 225))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y - 45))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y - 90))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y - 135))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y - 180))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y - 225))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y + 45))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y + 90))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y + 135))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y + 180))
                self.draw_rect(colors.brigth_red, self.boat8.x + 135, (self.boat8.y + 225))

    def draw_rect(self, color, x, y):
        if x >= 500 and x < 1400 and y >= 100 and y < 1000:
            pygame.draw.rect(screen, color,(x, y, 44,44))
            if self.boat_attack == 1 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat2.defense == False and self.boat2.health != 0 or self.boat_attack == 2 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat2.defense == False and self.boat2.health != 0:
                if x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 22 > y or x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 67 > y:
                    self.boat2.health -= 1
                    self.boat1.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 1 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat2.defense == True and self.boat2.health != 0 or self.boat_attack == 2 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat2.defense == True and self.boat2.health != 0:
                if x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 22 > y or x+44 > self.boat2.x + 67 > x and y+44 > self.boat2.y > y:
                    self.boat2.health -= 1
                    self.boat1.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 1 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat4.defense == False and self.boat4.health != 0 or self.boat_attack == 2 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat4.defense == False and self.boat4.health != 0:
                if x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 22 > y or x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 67 > y or x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 112 > y:
                    self.boat4.health -= 1
                    self.boat1.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 1 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat4.defense == True and self.boat4.health != 0 or self.boat_attack == 2 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat4.defense == True and self.boat4.health != 0:
                if x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 22 > y or x+44 > self.boat4.x + 67 > x and y+44 > self.boat4.y > y or x+44 > self.boat4.x + 112 > x and y+44 > self.boat4.y > y:
                    self.boat4.health -= 1
                    self.boat1.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 1 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat6.defense == False and self.boat6.health != 0 or self.boat_attack == 2 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat6.defense == False and self.boat6.health != 0:
                if x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 22 > y or x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 67 > y or x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 112 > y:
                    self.boat6.health -= 1
                    self.boat1.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 1 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat6.defense == True and self.boat6.health != 0 or self.boat_attack == 2 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat6.defense == True and self.boat6.health != 0:
                if x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 22 > y or x+44 > self.boat6.x + 67 > x and y+44 > self.boat6.y > y or x+44 > self.boat6.x + 112 > x and y+44 > self.boat6.y > y:
                    self.boat6.health -= 1
                    self.boat1.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 1 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat8.defense == False and self.boat8.health != 0 or self.boat_attack == 2 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat8.defense == False and self.boat8.health != 0:
                if x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 22 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 67 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 112 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 157 > y:
                    self.boat8.health -= 1
                    self.boat1.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 1 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat8.defense == True and self.boat8.health != 0 or self.boat_attack == 2 and self.boat1.attack != 0 and self.player_attack != 0 and self.boat8.defense == True and self.boat8.health != 0:
                if x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 22 > y or x+44 > self.boat8.x + 67 > x and y+44 > self.boat8.y > y or x+44 > self.boat8.x + 112 > x and y+44 > self.boat8.y > y or x+44 > self.boat8.x + 157 > x and y+44 > self.boat8.y > y:
                    self.boat8.health -= 1
                    self.boat1.attack -= 1
                    self.player_attack -= 1    

            elif self.boat_attack == 5 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat2.defense == False and self.boat2.health != 0 or self.boat_attack == 6 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat2.defense == False and self.boat2.health != 0:
                if x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 22 > y or x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 67 > y:
                    self.boat2.health -= 1
                    self.boat3.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 5 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat2.defense == True and self.boat2.health != 0 or self.boat_attack == 6 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat2.defense == True and self.boat2.health != 0:
                if x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 22 > y or x+44 > self.boat2.x + 67 > x and y+44 > self.boat2.y > y:
                    self.boat2.health -= 1
                    self.boat3.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 5 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat4.defense == False and self.boat4.health != 0 or self.boat_attack == 6 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat4.defense == False and self.boat4.health != 0:
                if x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 22 > y or x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 67 > y or x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 112 > y:
                    self.boat4.health -= 1
                    self.boat3.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 5 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat4.defense == True and self.boat4.health != 0 or self.boat_attack == 6 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat4.defense == True and self.boat4.health != 0:
                if x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 22 > y or x+44 > self.boat4.x + 67 > x and y+44 > self.boat4.y > y or x+44 > self.boat4.x + 112 > x and y+44 > self.boat4.y > y:
                    self.boat4.health -= 1
                    self.boat3.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 5 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat6.defense == False and self.boat6.health != 0 or self.boat_attack == 6 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat6.defense == False and self.boat6.health != 0:
                if x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 22 > y or x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 67 > y or x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 112 > y:
                    self.boat6.health -= 1
                    self.boat3.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 5 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat6.defense == True and self.boat6.health != 0 or self.boat_attack == 6 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat6.defense == True and self.boat6.health != 0:
                if x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 22 > y or x+44 > self.boat6.x + 67 > x and y+44 > self.boat6.y > y or x+44 > self.boat6.x + 112 > x and y+44 > self.boat6.y > y:
                    self.boat6.health -= 1
                    self.boat3.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 5 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat8.defense == False and self.boat8.health != 0 or self.boat_attack == 6 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat8.defense == False and self.boat8.health != 0:
                if x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 22 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 67 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 112 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 157 > y:
                    self.boat8.health -= 1
                    self.boat3.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 5 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat8.defense == True and self.boat8.health != 0 or self.boat_attack == 6 and self.boat3.attack != 0 and self.player_attack != 0 and self.boat8.defense == True and self.boat8.health != 0:
                if x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 22 > y or x+44 > self.boat8.x + 67 > x and y+44 > self.boat8.y > y or x+44 > self.boat8.x + 112 > x and y+44 > self.boat8.y > y or x+44 > self.boat8.x + 157 > x and y+44 > self.boat8.y > y:
                    self.boat8.health -= 1
                    self.boat3.attack -= 1
                    self.player_attack -= 1    

            elif self.boat_attack == 9 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat2.defense == False and self.boat2.health != 0 or self.boat_attack == 10 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat2.defense == False and self.boat2.health != 0:
                if x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 22 > y or x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 67 > y:
                    self.boat2.health -= 1
                    self.boat5.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 9 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat2.defense == True and self.boat2.health != 0 or self.boat_attack == 10 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat2.defense == True and self.boat2.health != 0:
                if x+44 > self.boat2.x + 22 > x and y+44 > self.boat2.y + 22 > y or x+44 > self.boat2.x + 67 > x and y+44 > self.boat2.y > y:
                    self.boat2.health -= 1
                    self.boat5.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 9 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat4.defense == False and self.boat4.health != 0 or self.boat_attack == 10 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat4.defense == False and self.boat4.health != 0:
                if x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 22 > y or x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 67 > y or x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 112 > y:
                    self.boat4.health -= 1
                    self.boat5.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 9 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat4.defense == True and self.boat4.health != 0 or self.boat_attack == 10 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat4.defense == True and self.boat4.health != 0:
                if x+44 > self.boat4.x + 22 > x and y+44 > self.boat4.y + 22 > y or x+44 > self.boat4.x + 67 > x and y+44 > self.boat4.y > y or x+44 > self.boat4.x + 112 > x and y+44 > self.boat4.y > y:
                    self.boat4.health -= 1
                    self.boat5.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 9 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat6.defense == False and self.boat6.health != 0 or self.boat_attack == 10 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat6.defense == False and self.boat6.health != 0:
                if x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 22 > y or x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 67 > y or x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 112 > y:
                    self.boat6.health -= 1
                    self.boat5.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 9 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat6.defense == True and self.boat6.health != 0 or self.boat_attack == 10 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat6.defense == True and self.boat6.health != 0:
                if x+44 > self.boat6.x + 22 > x and y+44 > self.boat6.y + 22 > y or x+44 > self.boat6.x + 67 > x and y+44 > self.boat6.y > y or x+44 > self.boat6.x + 112 > x and y+44 > self.boat6.y > y:
                    self.boat6.health -= 1
                    self.boat5.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 9 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat8.defense == False and self.boat8.health != 0 or self.boat_attack == 10 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat8.defense == False and self.boat8.health != 0:
                if x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 22 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 67 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 112 > y or x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 157 > y:
                    self.boat8.health -= 1
                    self.boat5.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 9 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat8.defense == True and self.boat8.health != 0 or self.boat_attack == 10 and self.boat5.attack != 0 and self.player_attack != 0 and self.boat8.defense == True and self.boat8.health != 0:
                if x+44 > self.boat8.x + 22 > x and y+44 > self.boat8.y + 22 > y or x+44 > self.boat8.x + 67 > x and y+44 > self.boat8.y > y or x+44 > self.boat8.x + 112 > x and y+44 > self.boat8.y > y or x+44 > self.boat8.x + 157 > x and y+44 > self.boat8.y > y:
                    self.boat8.health -= 1
                    self.boat5.attack -= 1
                    self.player_attack -= 1    


            elif self.boat_attack == 3 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat1.defense == False and self.boat1.health != 0 or self.boat_attack == 4 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat1.defense == False and self.boat1.health != 0:
                if x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 22 > y or x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 67 > y:
                    self.boat1.health -= 1
                    self.boat2.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 3 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat1.defense == True and self.boat1.health != 0 or self.boat_attack == 4 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat1.defense == True and self.boat1.health != 0:
                if x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 22 > y or x+44 > self.boat1.x + 67 > x and y+44 > self.boat1.y > y:
                    self.boat1.health -= 1
                    self.boat2.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 3 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat3.defense == False and self.boat3.health != 0 or self.boat_attack == 4 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat3.defense == False and self.boat3.health != 0:
                if x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 22 > y or x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 67 > y or x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 112 > y:
                    self.boat3.health -= 1
                    self.boat2.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 3 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat3.defense == True and self.boat3.health != 0 or self.boat_attack == 4 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat3.defense == True and self.boat3.health != 0:
                if x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 22 > y or x+44 > self.boat3.x + 67 > x and y+44 > self.boat3.y > y or x+44 > self.boat3.x + 112 > x and y+44 > self.boat3.y > y:
                    self.boat3.health -= 1
                    self.boat2.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 3 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat5.defense == False and self.boat5.health != 0 or self.boat_attack == 4 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat5.defense == False and self.boat5.health != 0:
                if x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 22 > y or x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 67 > y or x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 112 > y:
                    self.boat5.health -= 1
                    self.boat2.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 3 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat5.defense == True and self.boat5.health != 0 or self.boat_attack == 4 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat5.defense == True and self.boat5.health != 0:
                if x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 22 > y or x+44 > self.boat5.x + 67 > x and y+44 > self.boat5.y > y or x+44 > self.boat5.x + 112 > x and y+44 > self.boat5.y > y:
                    self.boat5.health -= 1
                    self.boat2.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 3 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat7.defense == False and self.boat7.health != 0 or self.boat_attack == 4 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat7.defense == False and self.boat7.health != 0:
                if x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 22 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 67 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 112 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 157 > y:
                    self.boat7.health -= 1
                    self.boat2.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 3 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat7.defense == True and self.boat7.health != 0 or self.boat_attack == 4 and self.boat2.attack != 0 and self.player_attack != 0 and self.boat7.defense == True and self.boat7.health != 0:
                if x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 22 > y or x+44 > self.boat7.x + 67 > x and y+44 > self.boat7.y > y or x+44 > self.boat7.x + 112 > x and y+44 > self.boat7.y > y or x+44 > self.boat7.x + 157 > x and y+44 > self.boat7.y > y:
                    self.boat7.health -= 1
                    self.boat2.attack -= 1
                    self.player_attack -= 1    

            elif self.boat_attack == 7 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat1.defense == False and self.boat1.health != 0 or self.boat_attack == 8 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat1.defense == False and self.boat1.health != 0:
                if x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 22 > y or x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 67 > y:
                    self.boat1.health -= 1
                    self.boat4.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 7 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat1.defense == True and self.boat1.health != 0 or self.boat_attack == 8 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat1.defense == True and self.boat1.health != 0:
                if x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 22 > y or x+44 > self.boat1.x + 67 > x and y+44 > self.boat1.y > y:
                    self.boat1.health -= 1
                    self.boat4.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 7 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat3.defense == False and self.boat3.health != 0 or self.boat_attack == 8 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat3.defense == False and self.boat3.health != 0:
                if x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 22 > y or x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 67 > y or x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 112 > y:
                    self.boat3.health -= 1
                    self.boat4.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 7 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat3.defense == True and self.boat3.health != 0 or self.boat_attack == 8 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat3.defense == True and self.boat3.health != 0:
                if x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 22 > y or x+44 > self.boat3.x + 67 > x and y+44 > self.boat3.y > y or x+44 > self.boat3.x + 112 > x and y+44 > self.boat3.y > y:
                    self.boat3.health -= 1
                    self.boat4.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 7 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat5.defense == False and self.boat5.health != 0 or self.boat_attack == 8 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat5.defense == False and self.boat5.health != 0:
                if x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 22 > y or x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 67 > y or x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 112 > y:
                    self.boat5.health -= 1
                    self.boat4.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 7 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat5.defense == True and self.boat5.health != 0 or self.boat_attack == 8 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat5.defense == True and self.boat5.health != 0:
                if x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 22 > y or x+44 > self.boat5.x + 67 > x and y+44 > self.boat5.y > y or x+44 > self.boat5.x + 112 > x and y+44 > self.boat5.y > y:
                    self.boat5.health -= 1
                    self.boat4.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 7 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat7.defense == False and self.boat7.health != 0 or self.boat_attack == 8 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat7.defense == False and self.boat7.health != 0:
                if x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 22 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 67 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 112 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 157 > y:
                    self.boat7.health -= 1
                    self.boat4.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 7 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat7.defense == True and self.boat7.health != 0 or self.boat_attack == 8 and self.boat4.attack != 0 and self.player_attack != 0 and self.boat7.defense == True and self.boat7.health != 0:
                if x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 22 > y or x+44 > self.boat7.x + 67 > x and y+44 > self.boat7.y > y or x+44 > self.boat7.x + 112 > x and y+44 > self.boat7.y > y or x+44 > self.boat7.x + 157 > x and y+44 > self.boat7.y > y:
                    self.boat7.health -= 1
                    self.boat4.attack -= 1
                    self.player_attack -= 1    

            elif self.boat_attack == 11 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat1.defense == False and self.boat1.health != 0 or self.boat_attack == 12 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat1.defense == False and self.boat1.health != 0:
                if x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 22 > y or x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 67 > y:
                    self.boat1.health -= 1
                    self.boat6.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 11 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat1.defense == True and self.boat1.health != 0 or self.boat_attack == 12 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat1.defense == True and self.boat1.health != 0:
                if x+44 > self.boat1.x + 22 > x and y+44 > self.boat1.y + 22 > y or x+44 > self.boat1.x + 67 > x and y+44 > self.boat1.y > y:
                    self.boat1.health -= 1
                    self.boat6.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 11 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat3.defense == False and self.boat3.health != 0 or self.boat_attack == 12 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat3.defense == False and self.boat3.health != 0:
                if x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 22 > y or x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 67 > y or x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 112 > y:
                    self.boat3.health -= 1
                    self.boat6.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 11 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat3.defense == True and self.boat3.health != 0 or self.boat_attack == 12 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat3.defense == True and self.boat3.health != 0:
                if x+44 > self.boat3.x + 22 > x and y+44 > self.boat3.y + 22 > y or x+44 > self.boat3.x + 67 > x and y+44 > self.boat3.y > y or x+44 > self.boat3.x + 112 > x and y+44 > self.boat3.y > y:
                    self.boat3.health -= 1
                    self.boat6.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 11 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat5.defense == False and self.boat5.health != 0 or self.boat_attack == 12 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat5.defense == False and self.boat5.health != 0:
                if x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 22 > y or x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 67 > y or x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 112 > y:
                    self.boat5.health -= 1
                    self.boat6.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 11 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat5.defense == True and self.boat5.health != 0 or self.boat_attack == 12 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat5.defense == True and self.boat5.health != 0:
                if x+44 > self.boat5.x + 22 > x and y+44 > self.boat5.y + 22 > y or x+44 > self.boat5.x + 67 > x and y+44 > self.boat5.y > y or x+44 > self.boat5.x + 112 > x and y+44 > self.boat5.y > y:
                    self.boat5.health -= 1
                    self.boat6.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 11 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat7.defense == False and self.boat7.health != 0 or self.boat_attack == 12 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat7.defense == False and self.boat7.health != 0:
                if x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 22 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 67 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 112 > y or x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 157 > y:
                    self.boat7.health -= 1
                    self.boat6.attack -= 1
                    self.player_attack -= 1
            elif self.boat_attack == 11 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat7.defense == True and self.boat7.health != 0 or self.boat_attack == 12 and self.boat6.attack != 0 and self.player_attack != 0 and self.boat7.defense == True and self.boat7.health != 0:
                if x+44 > self.boat7.x + 22 > x and y+44 > self.boat7.y + 22 > y or x+44 > self.boat7.x + 67 > x and y+44 > self.boat7.y > y or x+44 > self.boat7.x + 112 > x and y+44 > self.boat7.y > y or x+44 > self.boat7.x + 157 > x and y+44 > self.boat7.y > y:
                    self.boat7.health -= 1
                    self.boat6.attack -= 1
                    self.player_attack -= 1    


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