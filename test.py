import pygame as pg

pg.init()  # initialize Pygame
screen = pg.display.set_mode((400, 400))
pg.display.set_caption("Test Window")

running = True
while running:
    for e in pg.event.get():  # event loop
        if e.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))  # clear screen
    pg.display.update()

pg.quit()