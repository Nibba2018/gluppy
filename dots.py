import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def drawDot(x, y):
    gl.glBegin(gl.GL_POINTS)
    gl.glVertex2i(x, y)
    gl.glEnd()

if __name__ == "__main__":
    from window import init_window

    def display():
        drawDot(100, 80)
        gl.glFlush()

    init_window(display)