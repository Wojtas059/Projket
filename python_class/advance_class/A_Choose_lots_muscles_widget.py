import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label



class AChooseLotsMusclesWidget(Screen):
    _mouscular_2 = ObjectProperty(None)
    _mouscular_1 = ObjectProperty(None)

    def choose_clicked( self, many):
        if int(many) > 1:
            self._mouscular_2.disabled =False
        else:
            self._mouscular_2.disabled =True
        self._mouscular_1.disabled =False

    def on_save(self, many):
        self.parent.get_parametrs(int(many))

    def on_click(self, many):
        try:
            self.parent.set_many(int(many))
            return True
        except ValueError:
            self.error_pop("Error", "Aby przejść dalej musisz wybrać ilość mięśni,\n a także jakie to będą mieśnie")
            return False

    def error_pop(self, name, text):
        pop = Popup(title='Invalid Form',
                  content=Label(text=name+'\n'+text),
                  size_hint=(None, None), size=(400, 400))
        pop.open()