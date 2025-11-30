from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtCore import Qt


class TitleScreen(QWidget):
    def __init__(self, parent_stack):
        super(TitleScreen, self).__init__()
        self.initUI()
        self.parent_stack = parent_stack

    def initUI(self):
        self.setWindowTitle("The Draconid Weyr")
        self.setGeometry(100, 100, 1000, 800)

        self.label = QLabel(self)
        self.label.setText("Welcome to the Weyr!")
        self.label.adjustSize()
        self.label.move(50, 50)

        self.breeding_button = QPushButton(self)
        self.breeding_button.setText("Go to breeding screen")
        self.breeding_button.clicked.connect(lambda: self.parent_stack.setCurrentIndex(1))
        self.breeding_button.move(200, 200)

        self.choose_button = QPushButton(self)
        self.choose_button.setText("Create your weyr!")
        self.choose_button.clicked.connect(lambda: self.parent_stack.setCurrentIndex(2))
        self.choose_button.move(200, 250)
