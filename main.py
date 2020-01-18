from graphics import *
from mergeSort import mergeSorting
from bubbleSort import bubbleSorting
from drawing import Draw
import random

# constants
Length = 600
Width = 1200
Stick_length = 3
Diff_length = 2
white_color = color_rgb(255, 255, 255)
black_color = color_rgb(0, 0, 0)
# constants

def main():
    rectangles = []

    need_to_sort = [i for i in range(1, 241)]

    canvas = GraphWin("Sort visualize", Width, Length)
    canvas.setBackground(black_color)

    try:

        Visual = Draw(Length, Width, Stick_length, Diff_length, white_color, black_color, canvas, need_to_sort, 0.01)

        #merge sort
        random.shuffle(Visual.array)
        Visual.creating_retangles()
        mergeSorting(Visual, 0, len(Visual.array) - 1)

        #bubble sort
        Visual.delay = 0
        random.shuffle(Visual.array)
        Visual.creating_retangles()
        bubbleSorting(Visual)


        Visual.canvas.getMouse()

    except GraphicsError:
        print("Success")



if (__name__ == "__main__"):
    main()