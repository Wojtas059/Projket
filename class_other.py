import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.uix.dropdown  import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

    
class CustomDropDown(DropDown):
    port = ''
    def change(self, port_):
        self.port=port_

    def get_port(self):
        return self.port