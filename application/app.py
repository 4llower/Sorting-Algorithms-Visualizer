import math
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from sortings import *
from views import GraphicsError, color_rgb, GraphWin

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
    
    def ui_init(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(567, 427)
        self.centralwidget = QtWidgets.QWidget(main_window)
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
        main_window.setCentralWidget(self.centralwidget)

    def setup_ui(self, main_window, view_window):
        self.view_window = view_window
        self.ui_init(main_window)
        self.buttons_events_init()
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Sorting visualizer"))
        self.mergeSortButton.setText(_translate("main_window", "Merge sort"))
        self.LSDSortButton.setText(_translate("main_window", "LSD Sort"))
        self.countSortButton.setText(_translate("main_window", "Count sort"))
        self.bubbleSortButton.setText(_translate("main_window", "Bubble sort"))
        self.quickSortButton.setText(_translate("main_window", "Quick sort"))

    def create_window(self):
        self.view_window.canvas = GraphWin("Sorting visualizer", width, length)
        self.view_window.canvas.setBackground(black_color)

    def shuffling(self):
        random.shuffle(self.view_window.array)
        self.view_window.creating_retangles()

    def end_sorting(self):
        self.view_window.complete()
        self.view_window.canvas.close()

    def make_merge_sort(self):
        self.view_window.delay = 0
        self.create_window()
        self.shuffling()
        try:
            mergeSorting(self.view_window, 0, len(self.view_window.array) - 1)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_quick_sort(self):
        self.view_window.delay = 0.01
        self.create_window()
        self.shuffling()
        try:
            quickSorting(self.view_window, 0, len(self.view_window.array) - 1)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_count_sort(self):
        self.view_window.delay = 0.01
        self.create_window()
        self.shuffling()
        try:
            countSorting(self.view_window)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_bubble_sort(self):
        self.view_window.delay = 0
        self.create_window()
        self.shuffling()
        try:
            bubbleSorting(self.view_window)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_LSD_sort(self):
        self.view_window.delay = 0
        self.create_window()
        self.shuffling()
        try:
            LSDsorting(self.view_window, 0, len(self.view_window.array) - 1, 10 ** int(math.log10(max(self.view_window.array))))
        except GraphicsError:
            pass

        self.end_sorting()

