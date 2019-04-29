# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *



SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()
a = pygame.image.load('heim.png')

pygame.display.set_caption("랜덤 뽑기")
pygame.display.set_icon(a)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#fontObj = pygame.font.Font("TmonTium.ttf", 32)
#fontObj = pygame.font.Font(None, 32)
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
    clock.tick(60)
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

    pygame.display.update()