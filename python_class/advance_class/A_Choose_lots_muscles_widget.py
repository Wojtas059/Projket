import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database_handlers.database_handler import DatabaseHandler
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.gridlayout import GridLayout

class AUserListButton(RecycleView):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
    def get_data(self):
        self.data = ["Maj"]

    #def refresh_from_data(self):
    #    return super(UserListButton, self).refresh_from_data( self.data)
        

class BattonLabelSpinner(RecycleDataViewBehavior,GridLayout):
    nazwa=ObjectProperty(None)
    label_text = ObjectProperty(None)


class AChooseLotsMusclesWidget(Screen):
    many_ = ObjectProperty(None)
    recyView = ObjectProperty(None)

    def choose_clicked( self, many):
        self.recyView.disabled = False
        self.recyView.data = [{'text': str(x)} for x in range(int(many))]    

    def on_load(self):
        self.recyView.disabled = True
        listData = []
        self.many_.values = [str(x) for x in range(20)]

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