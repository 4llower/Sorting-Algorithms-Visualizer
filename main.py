from graphics import *
from mergeSort import mergeSorting
from bubbleSort import bubbleSorting
from quickSort import quickSorting
from drawing import Draw
from LSDsort import LSDsorting
from countSort import countSorting
import random

# constants
Length = 600
Width = 1200
Stick_length = 2
ValueOfSicks = 600
white_color = color_rgb(255, 255, 255)
black_color = color_rgb(0, 0, 0)
# constants

def createWindow(Visual):
    Visual.canvas = GraphWin("Sort visualize", Width, Length)
    Visual.canvas.setBackground(black_color)

def shuffling(Visual):
    random.shuffle(Visual.array)
    Visual.creating_retangles()

def end_sorting(Visual):
    Visual.complete()
    Visual.canvas.close()

def make_merge_sort(Visual):
    Visual.delay = 0
    createWindow(Visual)
    shuffling(Visual)
    mergeSorting(Visual, 0, len(Visual.array) - 1)
    end_sorting(Visual)

def make_quick_sort(Visual):
    Visual.delay = 0.01
    createWindow(Visual)
    shuffling(Visual)
    quickSorting(Visual, 0, len(Visual.array) - 1)
    end_sorting(Visual)
def make_count_sort(Visual):
    Visual.delay = 0.01
    createWindow(Visual)
    shuffling(Visual)
    countSorting(Visual)
    end_sorting(Visual)
def make_bubble_sort(Visual):
    Visual.delay = 0
    createWindow(Visual)
    shuffling(Visual)
    bubbleSorting(Visual)
    end_sorting(Visual)

def main():

    need_to_sort = [i for i in range(1, ValueOfSicks)]

    try:

        Visual = Draw(Length, Width, Stick_length, 0, white_color, black_color, need_to_sort, 0)

        #merge sort
        make_merge_sort(Visual)
        #quick sort
        make_quick_sort(Visual)
        #count sort
        make_count_sort(Visual)
        #bubble sort
        make_bubble_sort(Visual)

    except GraphicsError:
        print("Success")


if (__name__ == "__main__"):
    main()