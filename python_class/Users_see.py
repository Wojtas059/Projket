import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import BooleanProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.metrics import dp
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recyclelayout import RecycleLayout
import queue

csvQueue=queue.Queue()

class UserListButton(RecycleView):
    def __init__(self, **kwargs):
        super(UserListButton, self).__init__(**kwargs)
        content = ["Wojciech Maj 1", "Piotr Łach 2 ","Wojciech Maj 3","Wojciech Maj 4","Wojciech Maj 5 ","Wojciech Maj 6", "Piotr Łach 7", "Dupa 8"]
        self.data = [{'text':x} for x in content]

class BattonLabel(GridLayout):
    nazwa=ObjectProperty(None)
    label_text = ObjectProperty(None)


        


class UsersSeeWidget(Screen):
    pass




