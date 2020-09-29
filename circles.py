from dots import drawDot

def drawSymmetry(center, pt):
    xc = center[0]
    yc = center[1]

    x = pt[0]
    y = pt[1]

    drawDot(xc + x, yc + y)
    drawDot(xc - x, yc + y)
    drawDot(xc + x, yc - y)
    drawDot(xc - x, yc - y)

    drawDot(xc + y, yc + x)
    drawDot(xc - y, yc + x)
    drawDot(xc + y, yc - x)
    drawDot(xc - y, yc - x)


def drawBresCirle(center, radius):
    x = 0
    y = radius
    d = 3 - 2*radius

    while x<=y:

        drawSymmetry(center, (x, y))

        if d>0:
            y -= 1
            d += 4*(x - y) + 10
        else:
            d += 4*x + 6

        x += 1


def drawCircle(center, radius):

    x = 0
    y = radius
    pk = 1 - radius

    while x <= y:

        drawSymmetry(center, (x, y))
        # print(pk, x, y)

        if pk < 0:
            pk += 2*x + 1
        elif pk >= 0:
            pk += 2*(x-y) + 1
            y += -1
        x+=1



if __name__ == "__main__":

    import OpenGL.GL as gl
    from window import init_window
    def display_circle():
        center1 = (200, 250)
        center2 = (310, 250)
        radius = 50

        drawDot(*center1)
        drawCircle(center1, radius)

        drawDot(*center2)
        drawBresCirle(center2, radius)
        gl.glFlush()

    init_window(display_circle, title="Mid point Circle ALGO", point_size=1.0)

