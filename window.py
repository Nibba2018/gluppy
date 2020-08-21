import OpenGL.GL as gl
import OpenGL.GLUT as glut


def init_window(display_callback, position=(0, 200), size=(540, 480),
                bg_color=(0, 0, 0, 1), title="pyOpenGL Window"):

    # Initialize GLUT
    glut.glutInit()
    # set Display mode
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(*size)
    glut.glutInitWindowPosition(*position)
    glut.glutCreateWindow(title)
    gl.glClearColor(*bg_color) # Color to be filled after clearing.
    glut.glutDisplayFunc(display_callback)  # Set display Callback
    glut.glutMainLoop()


if __name__ == "__main__":

    def display():
        """ Display callback function. To be called at each event loop.
        """
        # Remove everything from screen
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glFlush(); # Commit changes

    init_window(display, position=(0, 200), size=(540, 480),
               bg_color=(0, 0, 0, 1), title="Init Window")
