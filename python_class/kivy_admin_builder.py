import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.lang import Builder
import os.path
from kivy.resources import resource_add_path

def Upload():
    #Ta klasa odpowiedzialna jest za pliki *.kv odpowiadające za widget odpowiednich
    # podstron
    Builder.load_file('kivy_admin_builder/home_admin_widget.kv')
