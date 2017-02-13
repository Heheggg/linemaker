from random import randint

from display import *
from draw import *

screen = new_screen()
green = [0, 255, 0]
blue = [0, 0, 255]
red = [255, 0, 0]
color = [red, green, blue]

draw_line(randint(0, 100), 100, randint(200, 300), 200, screen, color[randint(0, 2)])
draw_line(randint(0, 100), 100, randint(200, 300), 120, screen, color[randint(0, 3)])
draw_line(randint(200, 300), 105, randint(0, 100), 100, screen, color[randint(0, 3)])

display(screen)
save_extension(screen, 'img.png')
