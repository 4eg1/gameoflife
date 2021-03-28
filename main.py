import pygame as pg
from random import *
import time as t
import numpy as np


def main_loop():
    pg.init()
    running = True
    # Options:
    # Winows Size
    pxl_x = 400
    pxl_y = 300
    # Seed-Number (start shuffel loops)
    start_count = 10
    # keep below 1k!!!
    # Width of each cell
    width = 50
    window = pg.display.set_mode((pxl_x, pxl_y))
    # Colours
    window.fill((255, 255, 255))
    colour = (0, 0, 0)
    space_y = pxl_y // width
    space_x = pxl_x // width
    s_count_total = randint(0, space_y * space_x)
    s_count_y = randint(0, space_y)
    s_count_x = randint(0, space_x)
    init = 1
    while running:
        while init > 0:
            # Get a start situation:
            s_count_y = randint(0, space_y)
            base_y = []
            base_y.append(s_count_y)
            s_count_x = randint(0, space_x)
            base_x = []
            base_x.append(s_count_x)
            pg.draw.rect(window, colour, pg.Rect(s_count_x * width, s_count_y * width, width, width))
            shuffel = 0
            while shuffel < start_count:
                shuffel = shuffel + 1
                s_count_y_new = randint(0, space_y)
                s_count_x_new = randint(0, space_x)
                pg.draw.rect(window, colour, pg.Rect(s_count_x_new * width, s_count_y_new * width, width, width))
                s_count_y = s_count_y_new
                base_y.append(s_count_y)
                s_count_x = s_count_x_new
                base_x.append(s_count_x)
                print("x:", base_x)
                print("y:", base_y)
            t.sleep(0.5)
            init = -1
            print("init done")
                # Start situation randomly intialized
        while init < 0:
            print("Step1")
            # Getting Step n+1
            # Create Binary Matrix
            Brett = np.zeros((space_x,space_y), dtype=int)

            print(Brett)
            # define neighbours for each board tile and for each neighbour check the game condition
            #       up       right   down    left     upleft   upright downright downleft
            nbs = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
            # old cells
            c_base_y = base_y
            c_base_x = base_x
            for b_y in base_y:
                print("b_y:",b_y)
                for b_x in base_x:
                    print("b_x:",b_x)
                    l_nbs = 0
                    for nb in nbs:
                        y = b_y + nb[1]
                        x = b_x + nb[0]
                        print("n_y:", y)
                        print("n_x:", x)
                        #Vergleich ob Nachbarn bereits existieren
                        #if (y in base_y[1] and x in base_x[1]):
                        #    l_nbs += 1
                        #    print ("l_nbs",l_nbs)
                        t.sleep(0.001)

            break

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        pg.display.update()
        init = 0



if __name__ == "__main__":
    main_loop()
