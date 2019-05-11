# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *

pygame.init()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def crash():
    largeText = pygame.font.SysFont("comicsansms", 115)
    textsurf, textrect = text_objects("You Crashed", largeText)
    textrect.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    while True:
        print("im in crash")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()




SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
bright_green = (64, 255, 64)
bright_red = (255, 64, 64)

a = pygame.image.load('heim.png')

pygame.display.set_caption("랜덤 뽑기")
pygame.display.set_icon(a)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


fontObj = pygame.font.Font("Cyberbit.ttf", 32)

textSurfaceObj = fontObj.render('한글黒澤', True, green, blue)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300, 300)

i = 10
chnArr = ['苹果', '香蕉', '西瓜', '草莓', '葡萄']

pos_x = 200
pos_y = 200

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 1

    if key_event[pygame.K_RIGHT]:
        pos_x += 1

    if key_event[pygame.K_UP]:
        pos_y -= 1

    if key_event[pygame.K_DOWN]:
        pos_y += 1
        i = i + 1

    screen.fill(white)
    pygame.draw.circle(screen, black, (pos_x, pos_y), 20)

    textSurfaceObj = fontObj.render(chnArr[i%5], True, green, blue)
    screen.blit(textSurfaceObj, textRectObj)

    button("GO!", 150, 450, 100, 50, green, bright_green, crash)
    button("Quit", 550, 450, 100, 50, red, bright_red, crash)

    pygame.display.update()

    clock.tick(60)