# Import Modules
import os
import pygame as pg

def clear_screen(screen, bg_color=(170, 238, 187)):
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(bg_color)
    screen.blit(background, (0, 0))
    pg.display.flip()

def init(width=1280, height=480, bg_color=(170, 238, 187), box_width=5, box_height=5):
    pg.init()
    screen = pg.display.set_mode((width, height), pg.SCALED)
    
    pg.display.flip()

    boxes_x = width  // box_width
    boxes_y = height // box_height

    clock = pg.time.Clock()
    return screen, boxes_x, boxes_y, clock

def draw_point(screen, box_width, box_height, x, y):
    sx = x * box_width
    sy = y * box_height
    rect = pg.Rect(sx, sy, box_width, box_height)
    pg.draw.rect(screen, (255,0,0), rect)
    pg.display.flip()


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    screen, boxes_x, boxes_y, clock = init()
    x = y = 10
    n = 0
    while True:
        clear_screen(screen, (0,0,0))
        box_width = box_height = 5
        y = n//boxes_x
        x = (n) % boxes_x
        n+= 1
        draw_point(screen, box_width, box_height, x, y)
        clock.tick(60)