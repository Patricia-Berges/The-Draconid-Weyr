import json
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor, QImage


def load_data(file_name):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


HEX_CODES = load_data("hex_codes.json")


def assemble_sprite(lineart, base_color, tint, horns, eyes):
    final_sprite = QPixmap(lineart.size())
    final_sprite.fill(Qt.transparent)

    painter = QPainter(final_sprite)
    painter.drawPixmap(0, 0, base_color)
    painter.drawPixmap(0, 0, tint)
    painter.drawPixmap(0, 0, horns)
    painter.drawPixmap(0, 0, eyes)
    painter.drawPixmap(0, 0, lineart)
    painter.end()

    return final_sprite


def tint_layer(layer, color):
    base = layer.toImage().convertToFormat(QImage.Format_ARGB32)
    tinted = QImage(base.size(), QImage.Format_ARGB32)
    tinted.fill(Qt.GlobalColor.transparent)  # Keep transparent background

    painter = QPainter(tinted)
    painter.drawImage(0, 0, base)

    # Apply color overlay
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(tinted.rect(), color)

    painter.end()
    return QPixmap.fromImage(tinted)


def render_sprite(species, age, color):
    """
    Accepted color as PHENOTYPE
    """
    species_sprite = species
    if age <= 10:
        species_sprite = f'{species}_baby'

    hex_code = HEX_CODES[color]

    lineart = QPixmap(f'sprites/{species_sprite}_lineart.png')
    base_color = QPixmap(f'sprites/{species_sprite}_base.png')
    tint = QPixmap(f'sprites/{species_sprite}_tint.png')
    horns = QPixmap(f'sprites/{species_sprite}_horns.png')
    eyes = QPixmap(f'sprites/{species_sprite}_eye.png')

    adjusted_tint = tint_layer(tint, QColor(hex_code))
    if color == "silver":
        adjusted_tint.fill(Qt.transparent)

    final_sprite = assemble_sprite(lineart, base_color, adjusted_tint, horns, eyes)

    return final_sprite


