import OpenGL.GL as gl
from dots import drawDot
from window import init_window, approx

def display():
    drawDDA((300, 100), (200, 400))
    gl.glFlush()

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

init_window(display, title="DDA Line Algorithm")
