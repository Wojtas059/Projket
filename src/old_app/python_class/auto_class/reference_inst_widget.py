import kivy
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

kivy.require("1.0.6")  # replace with your current kivy version !


class ReferenceInstWidget(Screen):
    def on_load(self):
        self.parent.restart_widget()
