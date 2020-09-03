import OpenGL.GL as gl
from dots import drawDot
from window import init_window, approx

def drawDDA(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    step = max(abs(dx), abs(dy))

    x_inc = dx/step
    y_inc = dy/step

    x, y = p1

    for _ in range(step):
        drawDot(approx(x), approx(y))
        x += x_inc
        y += y_inc


def drawBressenham(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    if abs(dy) < abs(dx):

        if p2[0] - p1[0] < 0:
            p1, p2 = p2, p1

        x = p1[0]
        y = p1[1]

        p = 2*dy - dx

        while(x < p2[0]):
            drawDot(x, y)
            x += 1
            if p<0:
                p += 2*dy
            else:
                p += 2*(dy-dx)
                y += 1


    else:

        if p2[1] - p1[1] < 0:
            p1, p2 = p2, p1

        x = p1[0]
        y = p1[1]

        p = 2*dx - dy

        while(y < p2[1]):
            drawDot(x, y)
            y += 1
            if p<0:
                p += 2*dx
            else:
                p += 2*(dx-dy)
                x += 1

if __name__ == "__main__":

    def display_DDA():

        # Square
        # Origin: 200, 200
        # Size: 100, 100
        drawDDA((200+100, 200+100), (200-100, 200+100))
        drawDDA((200-100, 200+100), (200-100, 200-100))
        drawDDA((200-100, 200-100), (200+100, 200-100))
        drawDDA((200+100, 200-100), (200+100, 200+100))

        #Diagonals
        drawDDA((200+100, 200-100), (200-100, 200+100))
        drawDDA((200-100, 200-100), (200+100, 200+100))

        gl.glFlush()


    def display_Bres():

        # Square
        # Origin: 200, 200
        # Size: 100, 100
        drawBressenham((200+100, 200+100), (200-100, 200+100))
        drawBressenham((200-100, 200+100), (200-100, 200-100))
        drawBressenham((200-100, 200-100), (200+100, 200-100))
        drawBressenham((200+100, 200-100), (200+100, 200+100))

        #Diagonals
        drawBressenham((200+100, 200-100), (200-100, 200+100))
        drawBressenham((200-100, 200-100), (200+100, 200+100))

        gl.glFlush()

    init_window(display_DDA, title="DDA Line Algorithms")
    # init_window(display_Bres, title="Bressenham Line Algorithms")
