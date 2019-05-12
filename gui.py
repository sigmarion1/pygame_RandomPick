import pygame as pg
from . import constants as c


class Button:

    def __init__(self, msg, x, y, w, h, ic, ac, scr, action=None):
        self.scr = scr
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.action = action

    def update(self):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pg.draw.rect(self.scr, self.ac, (self.x, self.y, self.w, self.h))

            if click[0] == 1 and self.action is not None:
                self.action()
            else:
                pg.draw.rect(self.scr, self.ic, (self.x, self.y, self.w, self.h))

            small_text = pg.font.SysFont("comicsansms", 20)
            text_surf, text_rect = self.text_objects(self.msg, small_text)
            text_rect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
            self.scr.blit(text_surf, text_rect)

    @staticmethod
    def text_objects(text, font):
        text_surf = font.render(text, True, c.BLACK)
        return text_surf, text_surf.get_rect()
