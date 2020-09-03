from dots import drawDot
from lines import drawDDA
import OpenGL.GL as gl
from sklearn.linear_model import LinearRegression

def regPlot(x_points, y_points, line_color=(1, 0, 0), point_color=(0, 0, 1),
            axes_color=(0, 1, 0), final_x=500, plot_points=False):

    # Draw axes
    gl.glColor3f(*axes_color)
    drawDDA((0, 0), (0, 500))
    drawDDA((0, 0), (500, 0))

    # build regression model
    reg_model = LinearRegression().fit(x_points.reshape(-1, 1),
                                       y_points)
    slope = reg_model.coef_[0]
    intercept = reg_model.intercept_
    initial_y = int(intercept)
    final_y = int(slope * final_x + intercept)

    # Draw regression line
    gl.glColor3f(*line_color)
    drawDDA((0, initial_y), (final_x, final_y))

    if plot_points:
        #Draw Points
        gl.glColor3f(*point_color)
        for x, y in zip(x_points, y_points):
            drawDot(x, y)


if __name__ == "__main__":
    import numpy as np
    from window import init_window
    import OpenGL.GLUT as glut

    point_color=(0, 0, 1)
    x_points = np.random.rand(50) * 500
    y_points = 200 + np.random.rand(50) * (500 - 200)

    clicked = False

    def mouseClicked(button, button_state, cursor_x, cursor_y):
        if (button == glut.GLUT_LEFT_BUTTON and
            button_state == glut.GLUT_DOWN):
            global clicked
            if not clicked:
                #Draw Points
                gl.glColor3f(*point_color)
                for x, y in zip(x_points.astype(int), y_points.astype(int)):
                    drawDot(x, y)
                clicked = True
                gl.glFlush()

    def display_plot():
        regPlot(x_points.astype(int), y_points.astype(int))
        gl.glFlush()

    init_window(display_plot, title="Regression Plot", point_size=4.0,
                bg_color=(1, 1, 0, 1), mouse_callback=mouseClicked)
