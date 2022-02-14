import kivy
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

kivy.require("1.0.6")  # replace with your current kivy version !


class ManagmentSensorsWidget(Screen):
    sensor_1 = ObjectProperty(None)

    def on_load(self):
        self.sensor_1.disabled = False
        if self.parent.get_many() > 1:
            self.sensor_2.disabled = False
        else:
            self.sensor_2.disabled = True
