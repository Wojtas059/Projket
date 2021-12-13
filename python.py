# kivy_venv\Scripts\activate
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('box.kv')
Builder.load_file('box1.kv')

class MyGrid(Screen):
    pass

class SingIn(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyGrid(name="mygrid"))
        sm.add_widget(SingIn(name="singin"))

        return sm
        #return MyGrid()


if __name__ == '__main__':
    MyApp().run()