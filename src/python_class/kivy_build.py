import kivy

kivy.require("1.0.6")  # replace with your current kivy version !
import glob
import os.path
from pathlib import Path

from kivy.lang import Builder
from kivy.resources import resource_add_path

from static.static_config import KIVY_CLIENT_DIR


def Upload():
    # Ta klasa odpowiedzialna jest za pliki *.kv odpowiadające za widget odpowiednich
    # podstron

    # INFO USED WIDGET HAVE TO BE IN GOOD FOLDER, UNUSED ONLY IN RIGHT FOLDER IN STATIC
    current_path = Path(KIVY_CLIENT_DIR)
    for current_file in current_path.glob("**/*.kv"):
        Builder.load_file(str(current_file))


#   Builder.load_file(str(KIVY_CLIENT_DIR/"home_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"singin_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"help_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"user_basic_w.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"user_pro_w.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"users_see_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"singup_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/choose_users_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/start_guest_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/choose_method_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/choose_lots_muscles_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/managment_sensors_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/start_reference_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/reference_instr_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/observation_ref_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/finish_ref_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/observation_exp_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"auto_widget/pauze_exp_widget.kv"))
#
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_choose_users_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_start_guest_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_choose_method_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_choose_lots_muscles_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_managment_sensors_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_start_reference_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_reference_instr_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_observation_ref_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_finish_ref_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_observation_exp_widget.kv"))
#   Builder.load_file(str(KIVY_CLIENT_DIR/"advance_widget/a_pauze_exp_widget.kv"))
