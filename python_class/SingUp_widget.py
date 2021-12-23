
from logging import error
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.label import Label
from kivy.uix.button import  Button
from kivy.uix.textinput import  TextInput
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.compat import string_types
from kivy.factory import Factory
from kivy.uix.popup import Popup
from User.user import User
from User.userValidator import UserValidator
from database_handlers.database_handler import DatabaseHandler
from threading import Thread
class Tooltip(Label):
    pass

class SingUpWidget(Screen):
    imie=ObjectProperty(None)
    nazwisko=ObjectProperty(None)
    login=ObjectProperty(None)
    password=ObjectProperty(None)
    u_password=ObjectProperty(None)
    u_pro=ObjectProperty(None)
    email=ObjectProperty(None)
    
    def on_press(self):
        u_pro_ = 0
        if self.u_pro.active:
            u_pro_ = 1


        if self.imie.text == '' or self.nazwisko.text == '' or self.login.text == '' or self.password.text == '' or self.c_password.text == '' or self.email.text == '':
            self.error_pop('', 'Uzupełnij wszytskie pola')

        else:
            if not( self.password.text == self.c_password.text ):
                self.error_pop('', 'Wpisane hasła nie są takie same')
            else:
                self.user = User( self.login.text,self.password.text,self.imie.text,self.nazwisko.text,  self.email.text, u_pro_)
                self.uvalid = UserValidator(self.user)
                data_error = {}
                data_error = self.uvalid.validateRegistration()
                print(data_error)
                licznik = 0
                str_error = ''
                if not data_error.get('NAME') == UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error +="Imie\njest za krotkie, minimum 4 zaki\n"
                if not data_error.get('SURNAME') ==UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error +="Nazwisko\njest za krotkie, minimum 4 zaki\n"
                
                if not data_error.get('PASSWORD') ==UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error +="Hasło\njest za krotkie, minimum 8 zaki\n"
                if not data_error.get('LOGIN') ==UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error +="Login\njest za krotki, minimum 4 zaki\n"
                if not data_error.get('LOGINEXISTENCE') ==UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error +="Login\nTaki login juz istnieje\n"
                if not data_error.get('EMAIL') ==UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error +="Email\njest nie poprawny\n"
                if not data_error.get('EMAILEXISTENCE') == UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error +="Email\nTaki email juz istnieje\n"

                if licznik == 0:
                    databaseHandler=DatabaseHandler()
                    databaseHandler.createUser(self.user)
                    self.error_pop('Rejestracja', 'Rejestracja powowiodła się pomyślnie')
                    return True
                else:
                    self.error_pop('', str_error)
                    return False

        

    def error_pop(self, name, text):
        pop = Popup(title='Invalid Form',
                  content=Label(text=name+'\n'+text),
                  size_hint=(None, None), size=(400, 400))
        pop.open()





class ToolTextInput(TextInput):
    tooltip_txt = StringProperty('')
    tooltip_cls = ObjectProperty(Tooltip)
    
    def __init__(self, **kwargs):
        self._tooltip = None
        super(ToolTextInput, self).__init__(**kwargs)
        fbind = self.fbind
        fbind('tooltip_cls', self._build_tooltip)
        fbind('tooltip_txt', self._update_tooltip)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self._build_tooltip()
    
    def _build_tooltip(self, *largs):
        if self._tooltip:
            self._tooltip = None
        cls = self.tooltip_cls
        if isinstance(cls, string_types):
            cls = Factory.get(cls)
        self._tooltip = cls()
        self._update_tooltip()
    
    def _update_tooltip(self, *largs):
        txt = self.tooltip_txt
        if txt:
            self._tooltip.text = txt
        else:
            self._tooltip.text = ''
    
    def on_spinner_select(self, text):
        print(text)
    
    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        self._tooltip.pos = pos
        Clock.unschedule(self.display_tooltip) # cancel scheduled event since I moved the cursor
        self.close_tooltip() # close if it's opened
        if self.collide_point(*self.to_widget(*pos)):
            Clock.schedule_once(self.display_tooltip, 1)

    def close_tooltip(self, *args):
        Window.remove_widget(self._tooltip)

    def display_tooltip(self, *args):
        Window.add_widget(self._tooltip)

class ToolTipButton(Button):
    tooltip_txt = StringProperty('')
    tooltip_cls = ObjectProperty(Tooltip)
    
    def __init__(self, **kwargs):
        self._tooltip = None
        super(ToolTipButton, self).__init__(**kwargs)
        fbind = self.fbind
        fbind('tooltip_cls', self._build_tooltip)
        fbind('tooltip_txt', self._update_tooltip)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self._build_tooltip()
    
    def _build_tooltip(self, *largs):
        if self._tooltip:
            self._tooltip = None
        cls = self.tooltip_cls
        if isinstance(cls, string_types):
            cls = Factory.get(cls)
        self._tooltip = cls()
        self._update_tooltip()
    
    def _update_tooltip(self, *largs):
        txt = self.tooltip_txt
        if txt:
            self._tooltip.text = txt
        else:
            self._tooltip.text = ''
    
    def on_spinner_select(self, text):
        print(text)
    
    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        self._tooltip.pos = pos
        Clock.unschedule(self.display_tooltip) # cancel scheduled event since I moved the cursor
        self.close_tooltip() # close if it's opened
        if self.collide_point(*self.to_widget(*pos)):
            Clock.schedule_once(self.display_tooltip, 1)

    def close_tooltip(self, *args):
        Window.remove_widget(self._tooltip)

    def display_tooltip(self, *args):
        Window.add_widget(self._tooltip)