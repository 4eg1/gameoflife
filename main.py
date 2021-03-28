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
    colour_w = (255,255,255)
    window.fill(colour_w)
    colour = (0, 0, 0)
    space_y = pxl_y // width
    space_x = pxl_x // width
    s_count_total = randint(0, space_y * space_x)
    s_count_y = randint(0, space_y-1)
    s_count_x = randint(0, space_x-1)
    #Creating empty Board
    Brett = np.zeros((space_y, space_x), dtype=int)
    init = 1
    while running and init > 0:
        # Get a start situation:
        s_count_y = randint(0, space_y-1)
        base_y = []
        base_y.append(s_count_y)
        s_count_x = randint(0, space_x-1)
        base_x = []
        base_x.append(s_count_x)
        pg.draw.rect(window, colour, pg.Rect(s_count_x * width, s_count_y * width, width, width))
        shuffel = 0
        while shuffel < start_count:
            s_count_y_new = randint(0, space_y-1)
            s_count_x_new = randint(0, space_x-1)
            pg.draw.rect(window, colour, pg.Rect(s_count_x_new * width, s_count_y_new * width, width, width))
            s_count_y = s_count_y_new
            base_y.append(s_count_y)
            s_count_x = s_count_x_new
            base_x.append(s_count_x)
            # Create Binary Matrix
            Brett[s_count_y][s_count_x] = 1
            shuffel = shuffel + 1
        t.sleep(0.5)
        init = -1
        print("init done")
        print("x:", base_x)
        print("y:", base_y)
        print(Brett)
        pg.display.update()
        t.sleep(1)
        # Start situation randomly intialized
    while running and init < 0:
        print("Step1")
        # Getting Step n+1
        #Prepaare Board acess
        base_y=len(Brett)
        base_x=len(Brett[0])
        # Copy Board
        Brett_neu = Brett
        # define neighbours for each board tile and for each neighbour check the game condition
        #       up       right   down    left     upleft   upright downright downleft
        nbs = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
        for b_y in range(base_y):
            #print("b_y:",b_y)
            for b_x in range(base_x):
                #print("b_x:",b_x)
                l_nbs = 0
                for nb in nbs:
                    y = b_y + nb[1]
                    x = b_x + nb[0]
                    #print("n_y:", y)
                    #print("n_x:", x)
                    #Vergleich ob Nachbarn bereits existieren
                    if (y < b_y and y >= 0 ) and (x < b_x and x >= 0) and (Brett_neu[y][x] == 1):
                        l_nbs += 1
                        print ("l_nbs:",l_nbs)
                if Brett_neu[b_y][b_x] == 1 and (l_nbs < 2 or l_nbs >3):
                    pg.draw.rect(window, colour_w,pg.Rect(b_x * width, b_y * width, width, width))
                    Brett[b_y][b_x] = 0
                if Brett_neu[b_y][b_x] == 0 and l_nbs == 3:
                    pg.draw.rect(window, colour, pg.Rect(b_x * width, b_y * width, width, width))
                    Brett[b_y][b_x] = 1
        print(Brett)
        pg.display.update()
        t.sleep(1)
        break

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
    #pg.display.update()
    init = 0



if __name__ == "__main__":
    main_loop()