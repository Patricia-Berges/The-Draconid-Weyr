from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from game_logic.draconid_generator import gen_random_color
from game_logic.sprite_generation import render_sprite
from screens.create_weyr_screen import CreateWeyrScreen


class ChooseScreen(QWidget):
    def __init__(self, parent_stack):
        super(ChooseScreen, self).__init__()
        self.initUI()
        self.parent_stack = parent_stack

        self.selected_species = ""

    def initUI(self):
        self.setWindowTitle("The Draconid Weyr")
        self.setGeometry(100, 100, 1000, 800)

        self.back_button = QPushButton(self)
        self.back_button.setText("Back to title")
        self.back_button.move(50, 50)
        self.back_button.clicked.connect(lambda: self.parent_stack.setCurrentIndex(0))

        self.choose_dragon = QPushButton(self)
        self.choose_dragon.setText("Dragon")
        self.choose_dragon.move(50, 100)
        self.choose_dragon.clicked.connect(lambda: self.set_species("dragon"))

        self.choose_wyvern = QPushButton(self)
        self.choose_wyvern.setText("Wyvern")
        self.choose_wyvern.move(50, 150)
        self.choose_wyvern.clicked.connect(lambda: self.set_species("wyvern"))

        self.species_text = QLabel(self)
        self.species_text.setText(f'')
        self.species_text.move(150, 350)
        self.species_text.setFixedSize(200, 50)

        self.chosen_sprite = QLabel(self)
        self.chosen_sprite.setFixedSize(300, 300)
        self.chosen_sprite.move(150, 50)

        self.create_weyr = QPushButton(self)
        self.create_weyr.hide()
        self.create_weyr.setFixedSize(200, 25)
        self.create_weyr.move(150, 400)
        self.create_weyr.clicked.connect(lambda: self.create_weyr_screen(self.selected_species))

    def set_species(self, species):
        self.selected_species = species
        self.species_text.setText(f"Selected species: {self.selected_species}")
        self.generate_draconid(self.selected_species)
        self.create_weyr.setText(f'Create a {self.selected_species} weyr')
        self.create_weyr.show()

    def generate_draconid(self, species):
        color = gen_random_color()
        sprite = render_sprite(species, 20, color["phenotype"])
        self.chosen_sprite.setPixmap(sprite.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def create_weyr_screen(self, species):
        screen = self.parent_stack.widget(3)
        screen.load_selected_species(species)
        self.parent_stack.setCurrentIndex(3)
