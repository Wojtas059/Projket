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

class Tooltip(Label):
    pass

class SingUpWidget(Screen):
    imie=ObjectProperty(None)
    nazwisko=ObjectProperty(None)
    login=ObjectProperty(None)
    password=ObjectProperty(None)
    c_password=ObjectProperty(None)
    kod=ObjectProperty(None)
    email=ObjectProperty(None)
    
    def on_press(self):
        if self.imie.text == '' or self.nazwisko.text == '' or self.login.text == '' or self.password.text == '' or self.c_password.text == '' or self.email.text == '':
            self.error_pop('', 'Uzupełnij wszytskie pola')

        else:
            if self.login.text == 'wmaj':
                self.error_pop('Login', 'Taki login już istnieje')


        

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