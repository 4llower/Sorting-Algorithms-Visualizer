from sortings import *
from views import GraphicsError, color_rgb, GraphWin
import math
import random

from PyQt5 import QtCore, QtGui, QtWidgets

white_color = color_rgb(255, 255, 255)
black_color = color_rgb(0, 0, 0)
length = 600
width = 1200

class App(object):
    def buttons_events_init(self):
        self.quickSortButton.clicked.connect(self.make_quick_sort)
        self.mergeSortButton.clicked.connect(self.make_merge_sort)
        self.bubbleSortButton.clicked.connect(self.make_bubble_sort)
        self.countSortButton.clicked.connect(self.make_count_sort)
        self.LSDSortButton.clicked.connect(self.make_LSD_sort)
    
    def ui_init(self, Window):
        Window.setObjectName("Window")
        Window.resize(567, 427)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 90, 106, 190))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mergeSortButton = QtWidgets.QPushButton(self.widget)
        self.mergeSortButton.setObjectName("mergeSortButton")
        self.gridLayout.addWidget(self.mergeSortButton, 2, 0, 1, 1)
        self.LSDSortButton = QtWidgets.QPushButton(self.widget)
        self.LSDSortButton.setObjectName("LSDSortButton")
        self.gridLayout.addWidget(self.LSDSortButton, 6, 0, 1, 1)
        self.countSortButton = QtWidgets.QPushButton(self.widget)
        self.countSortButton.setObjectName("countSortButton")
        self.gridLayout.addWidget(self.countSortButton, 4, 0, 1, 1)
        self.bubbleSortButton = QtWidgets.QPushButton(self.widget)
        self.bubbleSortButton.setObjectName("bubbleSortButton")
        self.gridLayout.addWidget(self.bubbleSortButton, 5, 0, 1, 1)
        self.quickSortButton = QtWidgets.QPushButton(self.widget)
        self.quickSortButton.setObjectName("quickSortButton")
        self.gridLayout.addWidget(self.quickSortButton, 3, 0, 1, 1)
        Window.setCentralWidget(self.centralwidget)

    def setup_ui(self, Window, Visual):
        self.Visual = Visual
        self.ui_init(Window)
        self.buttons_events_init()
        self.retranslate_ui(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslate_ui(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Sort Visualizer"))
        self.mergeSortButton.setText(_translate("Window", "Merge sort"))
        self.LSDSortButton.setText(_translate("Window", "LSD Sort"))
        self.countSortButton.setText(_translate("Window", "Count sort"))
        self.bubbleSortButton.setText(_translate("Window", "Bubble sort"))
        self.quickSortButton.setText(_translate("Window", "Quick sort"))

    def create_window(self):
        self.Visual.canvas = GraphWin("Sort visualize", width, length)
        self.Visual.canvas.setBackground(black_color)

    def shuffling(self):
        random.shuffle(self.Visual.array)
        self.Visual.creating_retangles()

    def end_sorting(self):
        self.Visual.complete()
        self.Visual.canvas.close()

    def make_merge_sort(self):
        self.Visual.delay = 0
        self.create_window()
        self.shuffling()
        try:
            mergeSorting(self.Visual, 0, len(self.Visual.array) - 1)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_quick_sort(self):
        self.Visual.delay = 0.01
        self.create_window()
        self.shuffling()
        try:
            quickSorting(self.Visual, 0, len(self.Visual.array) - 1)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_count_sort(self):
        self.Visual.delay = 0.01
        self.create_window()
        self.shuffling()
        try:
            countSorting(self.Visual)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_bubble_sort(self):
        self.Visual.delay = 0
        self.create_window()
        self.shuffling()
        try:
            bubbleSorting(self.Visual)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_LSD_sort(self):
        self.Visual.delay = 0
        self.create_window()
        self.shuffling()
        try:
            LSDsorting(self.Visual, 0, len(self.Visual.array) - 1, 10 ** int(math.log10(max(self.Visual.array))))
        except GraphicsError:
            pass

        self.end_sorting()

