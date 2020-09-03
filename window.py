import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def init_window(display_callback, position=(200, 200), size=(500, 500),
                bg_color=(0, 0, 0, 1), draw_color=(1, 1, 1), point_size=4,
                ortho=(0, 500, 0, 500), title="pyOpenGL Window"):

    # Initialize GLUT
    glut.glutInit()
    # set Display mode
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(*size)
    glut.glutInitWindowPosition(*position)
    glut.glutCreateWindow(title)
    gl.glClearColor(*bg_color)        # Color to be filled after clearing.

    gl.glColor3f(*draw_color)         #  set the drawing color(white)
    gl.glPointSize(point_size)        # a 'dot' is 4 by 4 pixels
    glu.gluOrtho2D(*ortho)

    glut.glutDisplayFunc(display_callback)  # Set display Callback
    glut.glutMainLoop()


def approx(num):
    if num % 1 < 0.5:
        return int(num/1)
    else:
        return int(num/1) + 1


if __name__ == "__main__":

    def display():
        """ Display callback function. To be called at each event loop.
        """
        # Remove everything from screen
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glFlush(); # Commit changes

    init_window(display, title="Init Window")
