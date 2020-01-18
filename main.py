import time
from graphics import *
from mergeSort import mergeSorting
import random

# constants

Length = 600
Width = 1200
Stick_length = 3
Diff_length = 2
white_color = color_rgb(255, 255, 255)
black_color = color_rgb(0, 0, 0)

# constants


canvas = GraphWin("Sort visualize", Width, Length)
canvas.setBackground(black_color)


def main():
    rectangles = []

    need_to_sort = [i for i in range(1, 241)]
    #random.shuffle(need_to_sort)


    creating_retangles(rectangles, need_to_sort)
    time.sleep(1)
    visualize_swap(need_to_sort, rectangles, 5, 100)

    try:
        canvas.getMouse()
    except GraphicsError:
        print("Program has been ended.")


def creating_retangles(rectangles, array):

    if (len(rectangles) != 0):
        for i in range(rectangles):
            rectangles[i].setFill(black_color)
        rectangles = []

    for i in range(len(array)):
        rectangles.append(Stick(array[i], i))

    for i in range(len(rectangles)):
        rectangles[i].setFill(white_color)
        rectangles[i].draw(canvas)

def Stick(value, pos):
    return Rectangle(Point(pos * (Stick_length + Diff_length), Length),
                     Point(pos * (Stick_length + Diff_length) + Stick_length, Length - value))

def visualize_swap(array, rectangles, x, y):
    rectangles[x].setFill(black_color)
    rectangles[y].setFill(black_color)
    array[x], array[y] = array[y], array[x]
    rectangles[x] = Stick(array[x], x)
    rectangles[y] = Stick(array[y], y)
    rectangles[x].setFill(white_color)
    rectangles[y].setFill(white_color)
    rectangles[x].draw(canvas)
    rectangles[y].draw(canvas)

if (__name__ == "__main__"):
    main()