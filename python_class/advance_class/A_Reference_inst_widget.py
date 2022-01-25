import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen



class AReferenceInstWidget(Screen):
    def on_load(self):
        self.parent.A_restart_widget()