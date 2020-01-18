import time
from graphics import *
from mergeSort import mergeSorting
import random

#constants

Length = 900
Width = 500
white_color = color_rgb(255, 255, 255)
black_color = color_rgb(0, 0, 0)

#constants


canvas = GraphWin("Sort visualize", Length, Width)
canvas.setBackground(black_color)

def main():
    need_to_sort = [i for i in range(1, 201)]
    random.shuffle(need_to_sort)
    visualize(need_to_sort)
    canvas.getMouse()

def visualize(array):
    rectangle = Rectangle(Point(500, 250), Point(Length, Width))
    rectangle.setFill(white_color)
    rectangle.draw(canvas)


if (__name__ == "__main__"):
    main()