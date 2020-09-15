import time
from views.graphics import Rectangle, Point, color_rgb

class Draw:
    def __init__(self, length, width, stick_length, space_sticks, white_color, black_color, array, delay):
        self.length = length
        self.width = width
        self.stick_length = stick_length
        self.space_sticks = space_sticks
        self.white_color = white_color
        self.black_color = black_color
        self.array = array
        self.rectangles = []
        self.delay = delay

    def stick(self, value, pos):
        return Rectangle(Point(pos * (self.stick_length + self.space_sticks), self.length),
                         Point(pos * (self.stick_length + self.space_sticks) + self.stick_length, self.length - value))

    def creating_retangles(self):

        if (len(self.rectangles) != 0):
            for i in range(len(self.rectangles)):
                self.rectangles[i].setFill(self.black_color)
            self.rectangles = []

        for i in range(len(self.array)):
            self.rectangles.append(self.stick(self.array[i], i))

        for i in range(len(self.rectangles)):
            self.rectangles[i].setFill(self.white_color)
            self.rectangles[i].draw(self.canvas)

    def complete(self):
        for i in range(len(self.rectangles)):
            time.sleep(0.0010)
            self.rectangles[i].setFill(color_rgb(0, 255, 0))

    def view_windowize_swap(self, x, y):
        time.sleep(self.delay)
        self.rectangles[x].setFill(self.black_color)
        self.rectangles[y].setFill(self.black_color)
        self.array[x], self.array[y] = self.array[y], self.array[x]
        self.rectangles[x] = self.stick(self.array[x], x)
        self.rectangles[y] = self.stick(self.array[y], y)
        self.rectangles[x].setFill(self.white_color)
        self.rectangles[y].setFill(self.white_color)
        self.rectangles[x].draw(self.canvas)
        self.rectangles[y].draw(self.canvas)