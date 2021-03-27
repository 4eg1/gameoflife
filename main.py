import pygame as pg

def main_loop():
    pg.init()
    clock = pg.time.Clock()
    running = True
    window = pg.display.set_mode((640, 480))
    window.fill((255, 255, 255))
    while running:
        window.fill((255, 255, 255))
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        pg.display.flip()


if __name__ == "__main__":
    main_loop()

