import pygame as pg
from pygame.locals import *
import math
import numpy as np

global WHITE, RED, BLACK
WHITE = pg.Color(255, 255, 255)
RED = pg.Color(255, 0, 0)
BLACK = (0,0,0)
SQUARES=32
grid = np.zeros((SQUARES,SQUARES), dtype=int)

def count_neighbors(cell):
    i = cell[0]
    j = cell[1]
    sub_grid = [[grid[i-1][j-1], grid[i][j-1], grid[i+1][j-1]],
                [grid[i-1][j],   grid[i][j],   grid[i+1][j]],
                [grid[i-1][j+1], grid[i][j+1], grid[i+1][j+1]]]
    sub_grid = np.transpose(np.squeeze(sub_grid))
    print(sub_grid)
    non_zero = np.where(sub_grid.nonzero())
    return non_zero

def calc_game_of_life():
    for i in range(SQUARES):
        for j in range(SQUARES):
            if grid[i][j]:
                neighbors = count_neighbors((i,j))
                if (max(neighbors[1])<2):
                    grid[i][j]=0;
                # print(neighbors[1])
                # if not neighbors:
                #     grid[i][j] = 0

def draw_grid(window, MOUSE):
    w,h = pg.display.get_surface().get_size()
    # square_width
    square_width = int(w/SQUARES)

    # square_hight
    square_hight = int(h/SQUARES)

    if MOUSE != (0,0):
        grid_y = int(MOUSE[0]/square_width)
        grid_x = int(MOUSE[1]/square_hight)
        if grid[grid_x][grid_y]: 
            grid[grid_x][grid_y] = 0
        else:
            grid[grid_x][grid_y] = 1;



    # window.fill(WHITE)
    for i in range(SQUARES):
        for j in range(SQUARES):
            position_x = square_width*(j)+3
            position_y = square_hight*(i)+3
            poistion_y_bef = square_width*(j-1)+3
            poistion_y_bef = square_width*(j-1)+3
            if not grid[i][j]:
                rect = pg.Rect(position_x,position_y,square_width ,square_hight)
                pg.draw.rect(window, WHITE, rect)
            else:
                rect = pg.Rect(position_x,position_y,square_width ,square_hight)
                pg.draw.rect(window, BLACK, rect)
            pg.display.update()

def main_loop():
    MOUSE = (0,0)
    pg.init()
    running = True
    window = pg.display.set_mode((1000, 1000), HWSURFACE|DOUBLEBUF|RESIZABLE)
    window.fill(WHITE)
    filled_rect = pg.Rect(60,60,30,25)
    draw_grid(window, MOUSE)
    while running:
        w,h = pg.display.get_surface().get_size()
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.VIDEORESIZE:
                # print("i see you")
                draw_grid(window, MOUSE)
            elif e.type == pg.MOUSEBUTTONUP:
                MOUSE = pg.mouse.get_pos()
                draw_grid(window, MOUSE)
            elif e.type == pg.KEYDOWN:
                if(e.key==pg.K_RETURN):
                    calc_game_of_life()
                    draw_grid(window, (0,0))



if __name__ == "__main__":
    main_loop()

