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
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from threading import Thread 
import _thread
from kivy.properties import NumericProperty
from kivy.clock import Clock, mainthread
import asyncio
from kivy.loader import Loader
import asynckivy as ak
from kivy.uix.dropdown  import DropDown
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import os
import ctypes
import tkinter as tk
from tkinter import filedialog

#Builder.load_file('dupa.kv')

    #def build(self):
    #    #return ScreenManagement()
    #    threading.Thread(target=self.manager.get_screen('mygrid').build).start()
class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

    
class CustomDropDown(DropDown):
    pass

class MyGrid(Widget):
    com = ObjectProperty(None)
    mainbutton = ObjectProperty(None)

    def __init__(self, **var_args):
        super(MyGrid, self).__init__(**var_args)
        self.dropdown = CustomDropDown()
        self.mainbutton.bind(on_release=self.dropdown.open)
        # Added button to FloatLayout so inherits this class 
        self.dropdown.bind(on_select = lambda\
                           instance, x: setattr(self.mainbutton, 'text', x))    


    
    trump =False

    def on_press(self):
        self.trump = True
        file = open("scope_126.csv")
        dataArray1 = []
        for lin in file:
            dataArray1 = lin.split(',')
            self.save_file(dataArray1)
            if not (self.trump):
                break
        

    def start_thread(self):
        if not(self.trump):
            self.com.text = "Rozpozęto pomiar"
            Thread(target = self.on_press).start()
            
        else:
            Thread(target = self.error_win("Już uruchomiłeś pomiar")).start()

    def error_win(self, error_txt):
        ctypes.windll.user32.MessageBoxW(None, "Już uruchomiłeś pomiar", "Error", 0)

    async def on_press_false(self):
        self.com.text += "Pomiar Zastopowano"
        self.trump = False


    
    def stop(self):
        ak.start(self.on_press_false())
        
    def save_file(self, dataArray1):
        f = open("zapis.csv", "a")
        f.write(",".join(dataArray1))
        f.close()
        self.com.text += ",".join(dataArray1)

    def save_file_(self):
        Thread(target = self.file_load).start()
        
    def file_load(self):
        filedialog.askopenfilename()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.com.text)

        self.dismiss_popup()


class MyApp(App):
    def build(self):
        #return ScreenManagement()
        return MyGrid()


        

if __name__ == '__main__':

    MyApp().run()
    