import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class SingInWidget(Screen):
    login=ObjectProperty(None)
    password=ObjectProperty(None)
    
    def on_press(self):
        if  self.login.text == '' or self.password.text == '':
            self.error_pop('', 'Uzupełnij wszytskie pola')

    def error_pop(self, name, text):
        pop = Popup(title='Invalid Form',
                  content=Label(text=name+'\n'+text),
                  size_hint=(None, None), size=(400, 400))
        pop.open()