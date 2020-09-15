import sys
import math
import random
from application import App
from views import Draw, color_rgb
from PyQt5 import QtCore, QtGui, QtWidgets

# constants
length = 600
width = 1200
stick_length = 2
number_sticks = 600
white_color = color_rgb(255, 255, 255)
black_color = color_rgb(0, 0, 0)
# constants

def main():
    temp = [i for i in range(1, number_sticks)]
    visual = Draw(length, width, stick_length, 0, white_color, black_color, temp, 0)

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = App()
    ui.setup_ui(Window, visual)
    Window.show()
    sys.exit(app.exec_())


if (__name__ == "__main__"):
    main()
