import kivy
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

kivy.require("1.0.6")  # replace with your current kivy version !


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
