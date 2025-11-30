import json
import os

from PyQt5.QtCore import Qt
from screens.breeding_screen import BreedingScreen
from screens.title_screen import TitleScreen
from screens.choose_screen import ChooseScreen
from screens.create_weyr_screen import CreateWeyrScreen
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QPushButton


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.initUI()

        self.stack = QStackedWidget()

        self.title_screen = TitleScreen(self.stack)
        self.stack.addWidget(self.title_screen)  # index 0

        self.breeding_screen = BreedingScreen(self.stack)
        self.stack.addWidget(self.breeding_screen)  # index 1

        self.choose_screen = ChooseScreen(self.stack)
        self.stack.addWidget(self.choose_screen)  # index 2

        self.create_weyr_screen = CreateWeyrScreen(self.stack)
        self.stack.addWidget(self.create_weyr_screen)  #index 3

        self.setCentralWidget(self.stack)

    def initUI(self):
        self.setWindowTitle("The Draconid Weyr")
        self.setGeometry(100, 100, 1000, 800)


