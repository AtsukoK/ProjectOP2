import pygame
import time
import colors
import images
from pygame.locals import *
import functions

pygame.init()
screen_width = 800
screen_heigt = 600
size = (screen_width, screen_heigt)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleport")



def name():
    while not functions.game():
        name = ""
        functions.text("Fill in Player 1 name:", "comicsans", 50, 100, 100, colors.white)
        functions.text("Max 5 characteres", "comicsans", 50, 250, 150, colors.white)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.unicode.isalpha():
                        name += event.unicode
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    elif event.key == K_RETURN:
                        name = ""
                    elif event.key == K_SPACE:
                        name += " "
                elif event.type == QUIT:
                    pygame.quit()
                    quit()
            screen.fill((0, 0, 0))
            functions.text(name, "comicsans", 50, 100, 100, colors.white)
            pygame.display.update()



def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, colors.black)
    return textSurface, textSurface.get_rect()

def intro():
    while not game():
        screen.fill(colors.white)
        screen.blit(images.battleport_img, (275, 0))
        button("Start", 338, 250, 125, 50,  colors.green, colors.bright_green, name)
        button("Game Rules", 338, 330, 125, 50,  colors.blue, colors.bright_blue, game_rules_1)
        button("Highscores", 338, 410, 125, 50,  colors.yellow, colors.bright_yellow, quit)
        button("Exit", 338, 490, 125, 50,  colors.red, colors.bright_red, quitgame)
        pygame.display.flip()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x, y, w, h))

        if click[0] == 1 and action != None:
            time.sleep(0.15)
            action()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def game_rules_1():
    while not game():
        screen.fill(colors.white)
        button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_1, (screen_width * 0.25,0))
        button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_2)
        pygame.display.flip()

def game_rules_2():
    while not game():
        screen.fill(colors.white)
        button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_2, (screen_width * 0.25,0))
        button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_1)
        button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_3)
        pygame.display.flip()

def game_rules_3():
    while not game():
        screen.fill(colors.white)
        button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_3, (screen_width * 0.25,0))
        button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_2)
        button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_4)
        pygame.display.flip()

def game_rules_4():
    while not game():
        screen.fill(colors.white)
        button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_4, (screen_width * 0.25,0))
        button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_3)
        button("next", 650, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_5)
        pygame.display.flip()

def game_rules_5():
    while not game():
        screen.fill(colors.white)
        button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        screen.blit(images.instruction_img_5, (screen_width * 0.25,0))
        button("previous", 0, 550, 150, 50, colors.snow, colors.bright_snow, game_rules_4)
        pygame.display.flip()

def highscores():
    while not game():
        screen.fill(colors.white)
        button("back", 0, 0, 150, 50, colors.snow, colors.bright_snow, intro)
        pygame.display.flip()

def playing_board():
    rectw = 30
    rectx, recty = 100, 0
    for row in range(0, 20):
        for col in range (0, 20):
            pygame.draw.rect(screen, colors.white, (rectx, recty, rectw, rectw))
            rectx = rectx + rectw
        recty = recty + rectw
        rectx = 100
    horizontalposx = 100
    horizontalposy = 0
    horizontalwidth = 700
    horizontalheight = 0
    for horizontal in range(0, 21):
        pygame.draw.line(screen, colors.black, (horizontalposx, horizontalposy), (horizontalwidth, horizontalheight))
        horizontalposy += 30
        horizontalheight += 30
    verticalposx = 100
    verticalposy = 0
    verticalwidth = 100
    verticalheight = 600
    for vertical in range(0, 21):
        pygame.draw.line(screen, colors.black, (verticalposx, verticalposy), (verticalwidth, verticalheight))
        verticalposx += 30
        verticalwidth += 30

    button("Exit Game", 700, 550, 100, 50, colors.blue, colors.bright_blue, quit)
    button("Main menu", 700, 500, 100, 50, colors.blue, colors.bright_blue, intro)

def main_game():
    while not game():
        screen.fill(colors.navy_blue)
        playing_board()
        pygame.display.flip()

def game():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

intro()
pygame.quit()
quit()
