import glob
from logging import log
from pathlib import Path

import kivy
from kivy.lang import Builder
from kivy.resources import resource_add_path

from static.static_config import KIVY_ADMIN_DIR

kivy.require("1.0.6")  # replace with your current kivy version !


def Upload():
    # Ta klasa odpowiedzialna jest za pliki *.kv odpowiadające za widget odpowiednich
    # podstron

    current_path = Path(KIVY_ADMIN_DIR)
    for file_path in current_path.glob("**/*.kv"):
        Builder.load_file(str(file_path))
