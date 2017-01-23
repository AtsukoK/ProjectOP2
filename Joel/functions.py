import pygame
import colors
import time

screen_width = 1920
screen_heigt = 1080
size = (screen_width, screen_heigt)
screen = pygame.display.set_mode(size)

def text_objects(text, font):
    textSurface = font.render(text, True, colors.black)
    return textSurface, textSurface.get_rect()

def text(font,size, word, x, y,):
    smallText = pygame.font.SysFont(font,size)
    textSurf, textRect = text_objects(word, smallText)
    textRect.center = (x), (y)
    screen.blit(textSurf, textRect)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            time.sleep(0.2)
            action()    
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def quitgame():
    pygame.quit()
    quit()