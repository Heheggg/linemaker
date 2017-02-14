from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    if(x0 > x1):
        draw_line(x1, y1, x0, y0, screen, color)

    else:
        A = y1 - y0
        B = - (x1 - x0)
        distance = 2 * A + B

        x = x0
        y = y0
        while x < x1:
            plot(screen, color, x, y)
            if distance > 0:
                y += 1
                distance += 2 * B
            x += 1
            distance += 2 * A

        return screen
        

def draw_quad2():


def draw_quadVII():


def draw_quadVIII():
#II
#<x+0.5, y-1>
#d = A + 2B
#while y < y1
#   plot(x,y);
#   if d < 0
#     x++
#     d+= 2A
#   y++
#   d += 2b
#

#VII
#<x+0.5, y-1)
#d = A - 2B
#while (y > y1)
#   plot(x,y)
#   if d > 0
#     x++
#     d += 2a
#   y--
#   d -= 2B

#VIII
#<x+1,y-0.5>
#d = 2A - B 
#while (x < x1)
#   plot(x,y)
#   if(d < 0)
#     y--
#     d-=2B
#   x++
#   d+= 2A 
