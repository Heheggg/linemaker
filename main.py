from random import randint
import math

from display import *
from draw import *

screen = new_screen()
green = [0, 255, 0]
blue = [0, 0, 255]
red = [255, 0, 0]
color = [red, green, blue]

# draw_line(randint(0, 100), 100, randint(200, 300), 200, screen, color[randint(0, 2)])
# draw_line(randint(0, 100), 100, randint(200, 300), 120, screen, color[randint(0, 2)])
# draw_line(randint(200, 300), 105, randint(0, 100), 100, screen, color[randint(0, 2)])

###DEMO CODE###
draw_line(250,250,250,500,screen,color[1])
draw_line(250,250,500,250,screen,color[1])
draw_line(250,250,0,250,screen,color[1])
draw_line(250,250,250,0,screen,color[1])

draw_line(250,250,500,300,screen,color[0])
draw_line(250,250,300,500,screen,color[0])
draw_line(250,250,500,200,screen,color[0])
draw_line(250,250,300,0,screen,color[0])
draw_line(250,250,0,200,screen,color[0])
draw_line(250,250,200,0,screen,color[0])
draw_line(250,250,0,300,screen,color[0])
draw_line(250,250,200,500,screen,color[0])

draw_line(250,250,500,500,screen,color[2])
draw_line(250,250,500,0,screen,color[2])
draw_line(250,250,0,500,screen,color[2])
draw_line(250,250,0,0,screen,color[2])


#GALLERY IMAGE GEN
# counter = 53; 
# alpha = [250, 250]
# beta = [250, 250]
# state = 1
# length = 10
# degree = -180;
# for i in range(counter):
#     if state == 0:
#         alpha[0] = beta[0]+int(length*math.cos(degree/60*math.pi/3))
#         alpha[1] = beta[1]+int(length*math.sin(degree/60*math.pi/3))
#         draw_line(alpha[0],alpha[1],beta[0],beta[1],screen,color[i%3])
#         state = 1;
#         degree += 240;
#         length += 8;
#     else:
#         beta[0] = alpha[0]+int(length*math.cos(degree/60*math.pi/3))
#         beta[1] = alpha[1]+int(length*math.sin(degree/60*math.pi/3))
#         draw_line(alpha[0],alpha[1],beta[0],beta[1],screen,color[i%3])
#         state = 0;
#         degree += 240;
#         length += 8;
        
display(screen)
save_extension(screen, 'img.png')
