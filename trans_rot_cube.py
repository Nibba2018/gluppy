from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#rotation
X_rot = 0.0
Y_rot = 0.0
Z_rot = 0.0

#translation
X_pos = 0.0
Y_pos = 0.0
Z_pos = -6.0

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    global X_rot,Y_rot,Z_rot

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(X_pos,Y_pos,Z_pos)

    glRotatef(X_rot,1.0,0.0,0.0)
    glRotatef(Y_rot,0.0,1.0,0.0)
    glRotatef(Z_rot,0.0,0.0,1.0)

    # Draw Cube (multiple quads)
    glBegin(GL_QUADS)

    glColor3f(1.0,0.0,0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)

    glColor3f(0.0,1.0,0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0)

    glColor3f(0.0,0.0,1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)

    glColor3f(1.0,1.0,0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)

    glColor3f(0.0,1.0,1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)

    glColor3f(1.0,0.0,1.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)

    glEnd()

    glutSwapBuffers()


def mouse_clicks(button, button_state, cursor_x, cursor_y):
    global X_rot, Y_rot, Z_rot
    if button == GLUT_LEFT_BUTTON and button_state == GLUT_DOWN:
        X_rot += 25
    elif button == GLUT_RIGHT_BUTTON and button_state == GLUT_DOWN:
        Y_rot += 25
    elif button == GLUT_MIDDLE_BUTTON and button_state == GLUT_DOWN:
        Z_rot += 25


def key_presses(key, x, y):
    global X_pos, Y_pos, Z_pos
    if key == GLUT_KEY_LEFT:
        X_pos -= 0.2
    elif key == GLUT_KEY_RIGHT:
        X_pos += 0.2
    elif key == GLUT_KEY_DOWN:
        Y_pos -= 0.2
    elif key == GLUT_KEY_UP:
        Y_pos += 0.2
    elif key == GLUT_KEY_PAGE_UP:
        Z_pos += 0.2
    elif key == GLUT_KEY_PAGE_DOWN:
        Z_pos -= 0.2


if __name__ == "__main__":

    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(200,200)

    glutCreateWindow('Cube Translation & Rotation')

    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutMouseFunc(mouse_clicks)
    glutSpecialFunc(key_presses)
    InitGL(640, 480)
    glutMainLoop()
