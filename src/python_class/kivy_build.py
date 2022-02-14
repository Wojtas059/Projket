from pathlib import Path

import kivy
from kivy.lang import Builder

# isort: split
from static.static_config import KIVY_CLIENT_DIR

kivy.require("1.0.6")  # replace with your current kivy version !


def Upload():
    # Ta klasa odpowiedzialna jest za pliki *.kv odpowiadające za widget odpowiednich
    # podstron

    # INFO USED WIDGET HAVE TO BE IN GOOD FOLDER, UNUSED ONLY IN RIGHT FOLDER IN STATIC
    current_path = Path(KIVY_CLIENT_DIR)
    for current_file in current_path.glob("**/*.kv"):
        Builder.load_file(str(current_file))
