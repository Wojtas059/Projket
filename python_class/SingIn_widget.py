import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from User.user import User
from User.userValidator import UserValidator
from database_handlers.database_handler import DatabaseHandler

class SingInWidget(Screen):
    login=ObjectProperty(None)
    password=ObjectProperty(None)
    
    def on_press(self):
        if  self.login.text == '' or self.password.text == '':
            self.error_pop('', 'Uzupełnij wszytskie pola')
        else:
            self.user = User()
            self.uvaild = UserValidator(self.user)
            data_error = {}
            data_error = self.uvaild.validateLogin()
        if data_error.get("USERLOGIN") == UserValidator.Flags.CORRECTFIELD and data_error.get("USERPASSWORD") == UserValidator.Flags.CORRECTFIELD :
            pass
        else:
            self.error_pop('', 'Nie poprawy email lub haslo')


    def error_pop(self, name, text):
        pop = Popup(title='Invalid Form',
                  content=Label(text=name+'\n'+text),
                  size_hint=(None, None), size=(400, 400))
        pop.open()