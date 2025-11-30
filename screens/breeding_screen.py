import json
import os
from random import choice

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget

from game_logic.draconid_generator import gen_random_color, baby_color, gen_baby_personality
from game_logic.sprite_generation import assemble_sprite, tint_layer
from game_logic.personality import gen_personality


def load_data(file_name):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


HEX_CODES = load_data("hex_codes.json")


class BreedingScreen(QWidget):
    def __init__(self, parent_stack):
        super(BreedingScreen, self).__init__()
        self.initUI()
        self.parent_stack = parent_stack

        self.mother = {}
        self.father = {}

    def initUI(self):
        self.setWindowTitle("The Draconid Weyr")
        self.setGeometry(100, 100, 1000, 800)

        self.back_button = QPushButton(self)
        self.back_button.setText("Back to title")
        self.back_button.move(50, 50)
        self.back_button.clicked.connect(lambda: self.parent_stack.setCurrentIndex(0))

        self.random_mother = QPushButton(self)
        self.random_mother.setText("Randomize mother")
        self.random_mother.clicked.connect(lambda: self.render_adult("mother"))
        self.random_mother.move(100, 100)

        self.mother_sprite = QLabel(self)
        self.mother_sprite.setFixedSize(200, 200)
        self.mother_sprite.move(100, 150)

        self.mother_personality = QLabel(self)
        self.mother_personality.setFixedSize(200, 20)
        self.mother_personality.move(100, 350)

        self.random_father = QPushButton(self)
        self.random_father.setText("Randomize father")
        self.random_father.clicked.connect(lambda: self.render_adult("father"))
        self.random_father.move(375, 100)

        self.father_sprite = QLabel(self)
        self.father_sprite.setFixedSize(200, 200)
        self.father_sprite.move(375, 150)

        self.father_personality = QLabel(self)
        self.father_personality.setFixedSize(200, 20)
        self.father_personality.move(375, 350)

        self.random_baby = QPushButton(self)
        self.random_baby.setText("Randomize a baby!")
        self.random_baby.clicked.connect(self.render_baby_dragon)
        self.random_baby.move(200, 375)

        self.baby_sprite = QLabel(self)
        self.baby_sprite.setFixedSize(200, 200)
        self.baby_sprite.move(200, 425)

        self.baby_personality = QLabel(self)
        self.baby_personality.setFixedSize(200, 20)
        self.baby_personality.move(200, 625)

    def change_label(self):
        self.label.setText("Get ready!")

    def render_adult(self, which: str):
        parent_color = gen_random_color()
        print(parent_color)

        if which == "mother":
            self.mother["color"] = parent_color
            self.mother["personality"] = gen_personality()
            self.mother_personality.setText(self.mother["personality"]["phenotype"])
            species_sprite = "dragon"
        elif which == "father":
            self.father["color"] = parent_color
            self.father["personality"] = gen_personality()
            self.father_personality.setText(self.father["personality"]["phenotype"])
            species_sprite = "wyvern"

        color = parent_color["phenotype"]
        hex_code = HEX_CODES[color]

        lineart = QPixmap(f'sprites/{species_sprite}_lineart.png')
        base_color = QPixmap(f'sprites/{species_sprite}_base.png')
        tint = QPixmap(f'sprites/{species_sprite}_tint.png')
        horns = QPixmap(f'sprites/{species_sprite}_horns.png')
        eyes = QPixmap(f'sprites/{species_sprite}_eye.png')

        adjusted_tint = tint_layer(tint, QColor(hex_code))

        if color == "silver":
            adjusted_tint.fill(Qt.transparent)

        if which == "mother":
            final_sprite = assemble_sprite(lineart, base_color, adjusted_tint, horns, eyes)
            self.mother_sprite.setPixmap(final_sprite.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        elif which == "father":
            final_sprite = assemble_sprite(lineart, base_color, adjusted_tint, horns, eyes)
            self.father_sprite.setPixmap(final_sprite.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def render_baby_dragon(self):
        baby_phenotype = baby_color(self.mother["color"], self.father["color"])
        baby_personality = gen_baby_personality(self.mother["personality"]["genotype"],
                                                self.father["personality"]["genotype"])
        self.baby_personality.setText(baby_personality["phenotype"])
        hex_code = HEX_CODES[baby_phenotype]

        species_sprite = choice(["wyvern_baby", "dragon_baby"])

        lineart = QPixmap(f'sprites/{species_sprite}_lineart.png')
        base_color = QPixmap(f'sprites/{species_sprite}_base.png')
        tint = QPixmap(f'sprites/{species_sprite}_tint.png')
        horns = QPixmap(f'sprites/{species_sprite}_horns.png')
        eyes = QPixmap(f'sprites/{species_sprite}_eye.png')

        adjusted_tint = tint_layer(tint, QColor(hex_code))

        if baby_phenotype == "silver":
            adjusted_tint.fill(Qt.transparent)

        final_sprite = assemble_sprite(lineart, base_color, adjusted_tint, horns, eyes)
        self.baby_sprite.setPixmap(final_sprite.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
