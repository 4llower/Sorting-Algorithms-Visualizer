import sys
import math
import random
from application import App
from views import Draw, color_rgb
from PyQt5 import QtCore, QtGui, QtWidgets

length = 600
width = 1200
stick_length = 2
number_sticks = 600
white_color = color_rgb(255, 255, 255)
black_color = color_rgb(0, 0, 0)

def main():
    temp = [i for i in range(1, number_sticks)]
    view_window = Draw(length, width, stick_length, 0, white_color, black_color, temp, 0)

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    ui = App()
    ui.setup_ui(main_window, view_window)
    
    main_window.show()
    sys.exit(app.exec_())


if (__name__ == "__main__"):
    main()
