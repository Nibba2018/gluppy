from dots import drawDot
from lines import drawDDA
import OpenGL.GL as gl
from sklearn.linear_model import LinearRegression

def regPlot(points, line_color=(1, 0, 0), point_color=(0, 0, 1),
            axes_color=(0, 1, 0), final_x=500):

    # Draw axes
    gl.glColor3f(*axes_color)
    drawDDA((0, 0), (0, 500))
    drawDDA((0, 0), (500, 0))

    # build regression model
    reg_model = LinearRegression().fit(points[:][0].reshape(-1, 1),
                                       points[:][1])
    slope = reg_model.coef_[0]
    intercept = reg_model.intercept_
    initial_y = int(intercept)
    final_y = int(slope * final_x + intercept)

    print(initial_y, final_y)

    # Draw regression line
    gl.glColor3f(*line_color)
    drawDDA((0, initial_y), (final_x, final_y))

    #Draw Points
    gl.glColor3f(*point_color)
    for point in points:
        drawDot(*point)


if __name__ == "__main__":
    import numpy as np
    from window import init_window

    def display_plot():
        points = np.random.rand(50, 2) * 500
        regPlot(points.astype(int))
        gl.glFlush()

    init_window(display_plot, title="Regression Plot", point_size=4.0,
                bg_color=(1, 1, 0, 1))
