import pygame, time
from colors import *
from pygame import gfxdraw
import math

def createPage(size = (640, 480), color = WHITE, tracer = 0):
    global scrnColor, scrnSize, frame, frameSkip, page
    scrnSize, scrnColor = size, color
    frame = 0
    if isinstance(tracer, int) and tracer >= 0:
        frameSkip = tracer
    else:
        frameSkip = 0
    pygame.display.init()
    pygame.font.init()
    page = pygame.display.set_mode(scrnSize)
    page.fill(scrnColor)
    pygame.display.set_caption('Euclid')
    pygame.display.flip()

def loadPage(name, tracer = 0):
    global scrnSize, frame, frameSkip, page
    if isinstance(tracer, int) and tracer >= 0:
        frameSkip = tracer
    else:
        frameSkip = 0
    pygame.display.init()
    pygame.font.init()
    scrap = pygame.image.load(name)
    scrnSize = scrap.get_size()
    page = pygame.display.set_mode(scrnSize)
    pygame.display.set_caption('Euclid')
    page.blit(scrap, (0, 0))
    pygame.display.flip()

def setTracer(n = 0):
    global frameSkip
    frameSkip = n

def getScreenSize():
    return scrnSize

def clear(color = None):
    global scrnColor, srap, final
    if color is not None:
        scrnColor = color
    # scrap.fill(scrnColor)
    # final.blit(scrap, (0, 0))
    page.fill(scrnColor)
    pygame.display.flip()

def savePage(name):
    # Append file type, e.g. "fry.jpg"
    pygame.image.save(page, name)

def finish():
    pygame.display.flip()

def wait(seconds = None):
    # Keep window open
    if seconds is not None:
        time.sleep(seconds)
    else:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()

class Pen():

    def __init__(self, color = BLACK, position = (0, 0), direction = 0, delay = 0, draw = True):
        self.color = color
        self.position = position
        self.direction = direction * math.pi / 180  # Store as radians
        self.delay = delay / 96
        self.draw = draw
        # fill and vertices are used only within Pen class
        self.fill = False
        self.vertices = []

    def render():
        global final, frame, frameSkip
        if frameSkip > 0:
            frame += 1
            if frame >= frameSkip:
                pygame.display.flip()
                frame = 0
        else:
            pygame.display.flip()

    def distanceTo(self, x2, y2):
        x1, y1 = self.getX(), self.getY()
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def getX(self):
        return self.position[0]
    
    def getY(self):
        return self.position[1]

    def getDir(self):
        return self.direction * 180 / math.pi  # Convert back to degrees

    def getColor(self):
        return self.color

    def isDown(self):
        return self.draw

    def line(self, start, stop):
        global frame, frameSkip, scrap
        # aaline(surface, color, startpos, endpos, blend=1) -> Rect
        pygame.draw.aaline(page, self.color, start, stop)
        Pen.render()

    def goto(self, x, y):
        # No translation of coordinates necessary - handled by line method
        start = self.position
        stop = (x, y)
        if self.fill:
            self.vertices.append(stop)
        elif self.isDown():
            Pen.line(self, start, stop)
        self.position = stop
        time.sleep(self.delay)

    def forward(self, dist):
        start = self.position
        theta = self.direction
        # -1 * since for image coordinates direction of y increase is down
        delta_x, delta_y = dist * math.cos(theta), -1 * dist * math.sin(theta)
        stop = round(start[0] + delta_x), round(start[1] + delta_y)
        if self.fill:
            self.vertices.append(stop)
            Pen.line(self, start, stop)
        elif self.isDown():
            Pen.line(self, start, stop)
        self.position = stop
        time.sleep(self.delay)

    def setDir(self, dir):
        self.direction = dir * math.pi / 180

    def turn(self, delta):
        self.direction = (self.direction + delta * math.pi / 180) % (2 * math.pi)

    def setColor(self, clr):
        self.color = clr

    def up(self):
        self.draw = False

    def down(self):
        self.draw = True

    def setDelay(self, d):
        self.delay = d

    def point(self):
        page.set_at(self.position, self.color)
        Pen.render()
        time.sleep(self.delay)

    def polygon(self):
        for i in range(0, len(self.vertices) - 1):
            Pen.line(self, self.vertices[i], self.vertices[i + 1])
        time.sleep(self.delay)

    def region(self):
        # filled_polygon(surface, points, color) -> None
        pygame.gfxdraw.filled_polygon(page, self.vertices, self.fillColor)
        Pen.render()
        time.sleep(self.delay)

    def beginRegion(self, color = None):
        # If  no color is passed, fillColor is current pen color.
        self.fill = True
        if color is None:
            self.fillColor = self.color
        else:
            self.fillColor = color
        self.vertices.append(self.position)

    def endRegion(self):
        Pen.region(self)
        Pen.polygon(self)
        self.vertices = []
        self.fill = False

    def circle(self, radius):
        # aacircle(surface, x, y, r, color) -> None
        pygame.gfxdraw.aacircle(page, *self.position, radius, self.color)
        Pen.render()
        time.sleep(self.delay)
    
    def disc(self, radius, fillColor = None):
        # filled_circle(surface, x, y, r, color) -> None
        if fillColor is not None:
            pygame.gfxdraw.filled_circle(page, *self.position, radius, fillColor)
            Pen.circle(self, radius)
        else:
            pygame.gfxdraw.filled_circle(page, *self.position, radius, self.color)
        Pen.render()
        time.sleep(self.delay)

    def ellipse(self):
        pass

    def arc(self):
        pass

    def write(self, text, fontName = 'Arial', fontSize = 30):
        textFont = pygame.font.SysFont(fontName, fontSize)
        # render(text, antialias, color, background=None) -> Surface
        scrap = textFont.render(text, True, self.color)
        page.blit(scrap, self.position)
        Pen.render()
        time.sleep(self.delay)