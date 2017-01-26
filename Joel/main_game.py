""" Battleport
Copyright 2017, Bush did Harambe Studios
"""

import pygame
import colors
import images
import functions
import classes
import time

pygame.init()
screen_width = 1920
screen_heigt = 1080
size = (screen_width, screen_heigt)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleport")
clock = pygame.time.Clock()

board = classes.Board()
player = classes.Player()


def intro():
    while not functions.game():
        screen.fill(colors.white)
        screen.blit(images.battleport_img, (screen_width * 0.4,0))
        functions.button("Start", 925, 500, 150, 50,  colors.green, colors.brigth_green, main_game)
        functions.button("Game Rules", 925, 600, 150, 50,  colors.blue, colors.brigth_blue, game_rules_1)   
        functions.button("Highscores", 925, 700, 150, 50, colors.snow , colors.brigth_snow, highscores)
        functions.button("Settings", 925, 800, 150, 50, colors.yellow , colors.brigth_yellow, settings)
        functions.button("Exit", 925, 900, 150, 50,  colors.red, colors.brigth_red, functions.quitgame)

        pygame.display.flip()

def pause():
    while not functions.game():
        pygame.draw.rect(screen,colors.brigth_snow, (500,200,960,540))
        functions.text("comicsansms", 150, "Paused", (screen_width/2), (screen_heigt/4), colors.black)
        functions.button("Continue", 650, 600, 150, 50,  colors.green, colors.brigth_green, main_game)
        functions.button("Game Rules", 850, 600, 150, 50,  colors.blue, colors.brigth_blue, game_rules_1_pause)
        functions.button("Settings", 1050, 600, 150, 50,  colors.yellow, colors.brigth_yellow, settings_pause)
        functions.button("Quit", 1250, 600, 150, 50,  colors.red, colors.brigth_red, intro)
        pygame.display.flip()

def ask_name():
    while not functions.game():
        screen.fill(colors.black)
        functions.get_key()
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        pygame.display.flip()

def main_game():
    while not functions.game():
        screen.fill(colors.black)
        board.draw()
        player.turn()
        player.update()
        player.draw()
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
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_6)
        pygame.display.flip()

def game_rules_6():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        screen.blit(images.instruction_img_6, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_5)
        pygame.display.flip()

def game_rules_1_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, pause)
        screen.blit(images.instruction_img_1, (screen_width * 0.25,0))
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_2_pause)
        pygame.display.flip()

def game_rules_2_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50, colors.snow, colors.brigth_snow, pause)
        screen.blit(images.instruction_img_2, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_1_pause)
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_3_pause)
        pygame.display.flip()

def game_rules_3_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, pause)
        screen.blit(images.instruction_img_3, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_2_pause)
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_4_pause)
        pygame.display.flip()

def game_rules_4_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, pause)
        screen.blit(images.instruction_img_4, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_3_pause)
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_5_pause)
        pygame.display.flip()

def game_rules_5_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, pause)
        screen.blit(images.instruction_img_5, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_4_pause)
        functions.button("next", 1700, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_6_pause)
        pygame.display.flip()

def game_rules_6_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, pause)
        screen.blit(images.instruction_img_6, (screen_width * 0.25,0))
        functions.button("previous", 0, 1000, 150, 50, colors.snow, colors.brigth_snow, game_rules_5_pause)
        pygame.display.flip()

def settings():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        pygame.display.flip()

def settings_pause():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, pause)
        pygame.display.flip()

def highscores():
    while not functions.game():
        screen.fill(colors.white)
        functions.button("back", 0, 0, 150, 50,colors.snow, colors.brigth_snow, intro)
        pygame.display.flip()

intro()
pygame.quit()
quit()
    
