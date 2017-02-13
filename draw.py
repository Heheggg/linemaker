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
        
