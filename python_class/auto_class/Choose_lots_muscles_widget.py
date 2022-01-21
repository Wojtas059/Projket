from os import listdir
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database_handlers.database_handler import DatabaseHandler


class ChooseLotsMusclesWidget(Screen):
    _mouscular_2 = ObjectProperty(None)
    _mouscular_1 = ObjectProperty(None)
    def on_load(self):
        listData = []
        instance = DatabaseHandler()
        instance.createConnection()
        
        for i in instance.getAllMuscles():
            listData.append(i[-1])
        instance.closeConnection()
        self._mouscular_2.values = listData
        self._mouscular_1.values = listData
        

    def choose_clicked( self, many):
        if int(many) > 1:
            self._mouscular_2.disabled =False
        else:
            self._mouscular_2.disabled =True
        self._mouscular_1.disabled =False
        


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