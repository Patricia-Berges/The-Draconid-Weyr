from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget


class CreateWeyrScreen(QWidget):
    def __init__(self, parent_stack):
        super(CreateWeyrScreen, self).__init__()
        self.current_species = None
        self.initUI()
        self.parent_stack = parent_stack

    def initUI(self):
        self.current_species = ""
        self.setWindowTitle("The Draconid Weyr")
        self.setGeometry(100, 100, 1000, 800)

        self.title = QLabel(self)
        self.title.move(20, 20)

    def load_selected_species(self, species):
        self.current_species = species
        self.title.setText(f'Creating a {self.current_species} weyr')

