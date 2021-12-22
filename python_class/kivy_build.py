import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.lang import Builder
import os.path
from kivy.resources import resource_add_path

def Upload():
    #Ta klasa odpowiedzialna jest za pliki *.kv odpowiadające za widget odpowiednich
    # podstron
    Builder.load_file('kivy_bulider/home_widget.kv')
    Builder.load_file('kivy_bulider/singin_widget.kv')
    Builder.load_file('kivy_bulider/help_widget.kv')
    Builder.load_file('kivy_bulider/user_basic_w.kv')
    Builder.load_file('kivy_bulider/user_pro_w.kv')
    Builder.load_file('kivy_bulider/users_see_widget.kv')
    Builder.load_file('kivy_bulider/singup_widget.kv')
