import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.gridlayout import GridLayout

class AUserListManagment(RecycleView):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []


class BattonManagmentLabel(RecycleDataViewBehavior,GridLayout):
    
    def __init__(self) -> None:
        super().__init__()
        print(self.values)

class AManagmentSensorsWidget(Screen):
    recyViewManagment = ObjectProperty(None)
    def on_load(self):
        self.recyViewManagment.data = [{'text': str(self.parent.get_id), 'values': str(x+1)} for x in range(int(self.parent.get_many()))]
    