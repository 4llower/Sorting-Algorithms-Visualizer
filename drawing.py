import time
from graphics import *
class Draw:
    def __init__(self, Length, Width, Stick_length, Diff_length, white_color, black_color, canvas, array):
        self.Length = Length
        self.Width = Width
        self.Stick_length = Stick_length
        self.Diff_length = Diff_length
        self.white_color = white_color
        self.black_color = black_color
        self.canvas = canvas
        self.array = array
        self.rectangles = []

    def Stick(self, value, pos):
        return Rectangle(Point(pos * (self.Stick_length + self.Diff_length), self.Length),
                         Point(pos * (self.Stick_length + self.Diff_length) + self.Stick_length, self.Length - value))

    def creating_retangles(self):

        if (len(self.rectangles) != 0):
            for i in range(len(self.rectangles)):
                self.rectangles[i].setFill(black_color)
            self.rectangles = []

        for i in range(len(self.array)):
            self.rectangles.append(self.Stick(self.array[i], i))

        for i in range(len(self.rectangles)):
            self.rectangles[i].setFill(self.white_color)
            self.rectangles[i].draw(self.canvas)

    def visualize_swap(self, x, y):
        time.sleep(0.025)
        self.rectangles[x].setFill(self.black_color)
        self.rectangles[y].setFill(self.black_color)
        self.array[x], self.array[y] = self.array[y], self.array[x]
        self.rectangles[x] = self.Stick(self.array[x], x)
        self.rectangles[y] = self.Stick(self.array[y], y)
        self.rectangles[x].setFill(self.white_color)
        self.rectangles[y].setFill(self.white_color)
        self.rectangles[x].draw(self.canvas)
        self.rectangles[y].draw(self.canvas)