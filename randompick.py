# -*- coding: utf-8 -*-
import pygame as pg
import sys
from . import constants as c
from . import gui

from pg.locals import *


pg.init()


def text_objects(text, font):
    textSurface = font.render(text, True, c.BLACK)
    return textSurface, textSurface.get_rect()



def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(screen, ic, (x, y, w, h))

    smallText = pg.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def crash():
    largeText = pg.font.SysFont("comicsansms", 115)
    textsurf, textrect = text_objects("You Crashed", largeText)
    textrect.center = ((c.SCREEN_WIDTH/2), (c.SCREEN_HEIGHT/2))

    while True:
        largeText = pg.font.SysFont("comicsansms", 115)
        textsurf, textrect = text_objects("You Crashed", largeText)
        textrect.center = ((c.SCREEN_WIDTH / 2), (c.SCREEN_HEIGHT / 2))
        print("im in crash")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()



a = pg.image.load('heim.png')

pg.display.set_caption("랜덤 뽑기")
pg.display.set_icon(a)
screen = pg.display.set_mode(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)


fontObj = pg.font.Font("Cyberbit.ttf", 32)

textSurfaceObj = fontObj.render('한글黒澤', True, c.GREEN, c.BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300, 300)

i = 10
chnArr = ['苹果', '香蕉', '西瓜', '草莓', '葡萄']

pos_x = 200
pos_y = 200

clock = pg.time.Clock()

buttons = [gui.Button("한글", 100, 200, 100, 50, c.GREEN, c.CYAN, screen, crash), gui.Button("English", 300, 200, 100, 50, c.GREEN, c.CYAN, screen, crash)]

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    key_event = pg.key.get_pressed()
    if key_event[pg.K_LEFT]:
        pos_x -= 1

    if key_event[pg.K_RIGHT]:
        pos_x += 1

    if key_event[pg.K_UP]:
        pos_y -= 1

    if key_event[pg.K_DOWN]:
        pos_y += 1
        i = i + 1

    screen.fill(c.WHITE)
    pg.draw.circle(screen, c.BLUE, (pos_x, pos_y), 20)

    textSurfaceObj = fontObj.render(chnArr[i%5], True, c.BLUE, c.RED)
    screen.blit(textSurfaceObj, textRectObj)

    for button in buttons:
        button.update()

    pg.display.update()

    clock.tick(60)