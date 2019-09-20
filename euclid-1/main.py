import euclid
from colors import *

# create a page on which to draw
# give tracer a positive value to increase animation speed
euclid.createPage(size = (640, 480), color = ORANGE, tracer = 0)

w, h = euclid.getScreenSize()
xc, yc = w//2, h//2  # coordinates of center

# the higher the value of delay, the slower the animation
logos = euclid.Pen(color = BLUE, position = (xc, yc), direction = 0, delay = 8)

def square(s, x, y):

    logos1 = euclid.Pen(color=BLUE, position=(x, y), direction=0, delay=8)
    for i in range(4):
        logos1.turn(90)
        logos1.forward(s)
#square(32, 280, 280)


def row_squares(n, s, x, y):
    logos1 = euclid.Pen(color=BLUE, position=(x, y), direction=0, delay=8)
    for i in range(n):
        x = x + 50
        square(s, x, y)


#row_squares(3, 32, 160, 160)


def grid_squares(m, n, s, x, y):
    B = x
    for i in range(m):
        row_squares(n, s, x, y)
        y = y + 50
grid_squares(4, 7, 40, 210, 270)

def spiral(x, y, r):
    n = 5
    m = 15
    logos1 = euclid.Pen(color=BLUE, position=(x, y), direction=0, delay=8)
    for i in range(r * 8):
        logos1.forward(m)
        logos1.turn(n)
        n = n - 1


#spiral(60, 70, 10)




# euclid.finish()  # uncomment if tracer is nonzero
euclid.wait()  # keep window open