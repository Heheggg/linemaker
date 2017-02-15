from _future_ import division
from display import *


def draw_line(x0, y0, x1, y1, screen, color):
    if(x0 > x1):
        draw_line(x1, y1, x0, y0, screen, color)
        
    else:
        slope = (y1 - y0)/(x1 - x0)
            
        if slope > 1:
            return draw_quad2(x0, y0, x1, y1, screen, color)
        elif slope > 0:
            return draw_quad1(x0, y0, x1, y1, screen, color)
        elif slope > -1:
            return draw_quad8(x0, y0, x1, y1, screen, color)
        else:
            return draw_quad7(x0, y0, x1, y1, screen, color)

    
def draw_quad1(x0, y0, x1, y1, screen, color):
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
        
    
def draw_quad2(x0, y0, x1, y1, screen, color):
        A = y1 - y0
        B = - (x1 - x0)
        d = A + 2* B
    
        x = x0
        y = y0
        while y < y1
            plot(x,y);
            if d < 0
                x += 1
                d+= 2 * A
            y += 1
            d += 2 * b

        return screen
        

def draw_quad7(x0, y0, x1, y1, screen, color):
        A = y1 - y0
        B = - (x1 - x0)

        x = x0
        y = y0
        d = A - 2 * B
        while (y > y1)
            plot(x,y)
            if d > 0
                x += 1
                d += 2 * a
            y -= 1
            d -= 2 * B

        return screen
        

def draw_quad8(x0, y0, x1, y1, screen, color):
        A = y1 - y0
        B = - (x1 - x0)

        x = x0
        y = y0

        d = 2 * A - B 
        while (x < x1)
            plot(x,y)
            if(d < 0)
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A

        return screen

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
