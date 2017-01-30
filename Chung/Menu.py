import pygame
pygame.init()
screen_width = 800
screen_heigt = 600
size = (screen_width, screen_heigt)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleport")
battleport_img= pygame.image.load("Battleport.jpg")
instruction_img_1= pygame.image.load("instruction_1.png")
instruction_img_2= pygame.image.load("instruction_2.png")
instruction_img_3= pygame.image.load("instruction_3.png")
instruction_img_4= pygame.image.load("instruction_4.png")
instruction_img_5= pygame.image.load("instruction_5.png")

white = (255, 255, 255)
silver = (192, 192, 192)
black = (0, 0, 0)
bright_yellow = (255, 255, 0)
yellow = (155, 155, 0)
brigth_red = (255, 0, 0)
red = (155, 0, 0)
brigth_green = (0, 255, 0)
green = (0, 155, 0)
brigth_blue = (0, 0, 255)
blue = (0, 0, 155)
snow = (205, 201, 201)
brigth_snow = (139, 137, 137)



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
def intro():
    while not game():
        screen.fill(white)
        screen.blit(battleport_img, (275, 0))
        button("Start", 338, 250, 125, 50,  green, brigth_green, None)
        button("Game Rules", 338, 330, 125, 50,  blue, brigth_blue, game_rules_1)
        button("Highscores", 338, 410, 125, 50,  yellow, bright_yellow, highscores)
        button("Exit", 338, 490, 125, 50,  red, brigth_red, quitgame)

        pygame.display.flip()

def game_rules_1():
    while not game():
        screen.fill(white)
        button("back", 0, 0, 150, 50,snow, brigth_snow, intro)
        screen.blit(instruction_img_1, (screen_width * 0.25,0))
        button("next", 650, 550, 150, 50, snow, brigth_snow, game_rules_2)
        pygame.display.flip()

def game_rules_2():
    while not game():
        screen.fill(white)
        button("back", 0, 0, 150, 50,snow, brigth_snow, intro)
        screen.blit(instruction_img_2, (screen_width * 0.25,0))
        button("previous", 0, 550, 150, 50, snow, brigth_snow, game_rules_1)
        button("next", 650, 550, 150, 50, snow, brigth_snow, game_rules_3)
        pygame.display.flip()

def game_rules_3():
    while not game():
        screen.fill(white)
        button("back", 0, 0, 150, 50,snow, brigth_snow, intro)
        screen.blit(instruction_img_3, (screen_width * 0.25,0))
        button("previous", 0, 550, 150, 50, snow, brigth_snow, game_rules_2)
        button("next", 650, 550, 150, 50, snow, brigth_snow, game_rules_4)
        pygame.display.flip()

def game_rules_4():
    while not game():
        screen.fill(white)
        button("back", 0, 0, 150, 50,snow, brigth_snow, intro)
        screen.blit(instruction_img_4, (screen_width * 0.25,0))
        button("previous", 0, 550, 150, 50, snow, brigth_snow, game_rules_3)
        button("next", 650, 550, 150, 50, snow, brigth_snow, game_rules_5)
        pygame.display.flip()
def game_rules_5():
    while not game():
        screen.fill(white)
        button("back", 0, 0, 150, 50,snow, brigth_snow, intro)
        screen.blit(instruction_img_5, (screen_width * 0.25,0))
        button("previous", 0, 550, 150, 50, snow, brigth_snow, game_rules_4)
        pygame.display.flip()

def highscores():
    while not game():
        screen.fill(white)
        button("back", 0, 0, 150, 50,snow, brigth_snow, intro)
        pygame.display.flip()

intro()
pygame.quit()
quit()
