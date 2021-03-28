import pygame as pg
from random import *
import time as t

def main_loop():
    pg.init()
    running = True
    pxl_x = 400
    pxl_y = 300
    window = pg.display.set_mode((pxl_x, pxl_y))
    window.fill((255, 255, 255))
    width = 5
    space_y = pxl_y/width
    space_x = pxl_x/width
    s_count_total = randint(0, space_y * space_x)
    s_count_y = randint(0, space_y)
    s_count_x = randint(0, space_x)
    colour = (0,0,0)
    start_count= 10
    #keep below 1k!!!
    init = 1
    while running:

        while init > 0:
            s_count_y = randint(0, space_y)
            base_y = []
            base_y.append(s_count_y)
            s_count_x = randint(0, space_x)
            base_x = []
            base_x.append(s_count_x)
            pg.draw.rect(window, colour, pg.Rect(s_count_x * width, s_count_y * width, width, width))
            shuffel = 0
            while shuffel < 500:
                shuffel = shuffel + 1
                s_count_y_new = randint(0, space_y)
                s_count_x_new = randint(0, space_x)
                pg.draw.rect(window, colour, pg.Rect(s_count_x_new * width , s_count_y_new * width, width, width))
                s_count_y = s_count_y_new
                base_y.append(s_count_y)
                s_count_x = s_count_x_new
                base_x.append(s_count_x)
                print(base_x)
                print(base_y)
            t.sleep(0.5)
            init = 0


        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        pg.display.update()


if __name__ == "__main__":
    main_loop()
