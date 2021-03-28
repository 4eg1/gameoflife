import pygame as pg
from pygame.locals import *
import math
WHITE = pg.Color(255, 255, 255)
RED = pg.Color(255, 0, 0)
BLACK = (0,0,0)
MOUSE = (0,0)

def draw_grid(window, nbr_of_squares):
    w,h = pg.display.get_surface().get_size()
    count_w = int(w/16)
    count_h = int(h/16)
    window.fill(WHITE)
    for i in range(nbr_of_squares):
        for j in range(nbr_of_squares):
            sq_w = count_w*(i)+3
            sq_h = count_h*(j)+3

            rect = pg.Rect(sq_w,sq_h,count_w ,count_h)
            pg.draw.rect(window, BLACK, rect, 3)
            pg.display.update()

def main_loop():
    pg.init()
    running = True
    window = pg.display.set_mode((1000, 1000), HWSURFACE|DOUBLEBUF|RESIZABLE)
    window.fill(WHITE)
    filled_rect = pg.Rect(60,60,30,25)
    window.fill(WHITE)
    draw_grid(window, 16)
    while running:
        # filled_rect = pg.Rect(60,60,25,25)
        mouse = (0, 0)
        w,h = pg.display.get_surface().get_size()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.VIDEORESIZE:
                # print("i see you")
                draw_grid(window, 16)
            elif e.type == pg.MOUSEBUTTONUP:
                MOUSE = pg.mouse.get_pos()

if __name__ == "__main__":
    main_loop()

