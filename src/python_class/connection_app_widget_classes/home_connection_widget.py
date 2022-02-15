import kivy
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
# isort: split

kivy.require("1.0.6")  # replace with your current kivy version !


class HomeConnectionWidget(Screen):
    status_field = StringProperty(None)
   
    def message_connect_with_stm(self):
        self.ids.status_field.text="Łączenie z STM"
    def message_disconnect_with_stm(self):
        self.ids.status_field.text="Rozłączenie z STM"
    def message_disconnected_with_stm(self):
        self.ids.status_field.text="Rozłączono z STM"
    def message_connected_with_stm(self):
        self.ids.status_field.text="Połączono z STM"
    def message_connect_with_base_station(self):
        self.ids.status_field.text="Łączenie z stacją bazową"
    def message_disconnect_with_base_station(self):
        self.ids.status_field.text="Rozłączenie z stacją bazową"
    def message_disconnected_with_base_station(self):
        self.ids.status_field.text="Rozłączono z stacją bazową"
    def message_connected_with_base_station(self):
        self.ids.status_field.text="Połączono z stacją bazową"
    