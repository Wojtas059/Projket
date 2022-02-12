import kivy

kivy.require("1.0.6")  # replace with your current kivy version !
import os.path

from kivy.lang import Builder
from pathlib import Path
from kivy.resources import resource_add_path
from static.static_config import KIVY_CSV_DIR

def Upload():
    # KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './kivy_bulider/___my.kv'))
    # resource_add_path(KV_PATH)
    current_path = Path(KIVY_CSV_DIR)
    for current_file in current_path.glob("**/*.kv"):
        Builder.load_file(str(current_file))
    