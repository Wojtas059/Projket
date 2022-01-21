from pkgutil import get_data
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import BooleanProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.metrics import dp
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from database_handlers.database_handler import DatabaseHandler
import queue
import getpass

csvQueue=queue.Queue()


class UserListButton(RecycleView):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
    def get_data(self):
        self.data = ["Maj"]

    #def refresh_from_data(self):
    #    return super(UserListButton, self).refresh_from_data( self.data)
        

class BattonLabel(RecycleDataViewBehavior,GridLayout):
    nazwa=ObjectProperty(None)
    label_text = ObjectProperty(None)

   

  


class UsersSeeWidget(Screen):
    log_in =True
    du = ObjectProperty(None)
    
    def on_load(self):
        self.log_in = self.parent.get_bool_LogIn()
        print("Jestem zalogowany: "+str(self.log_in))
        if not self.log_in:
            self.id_ = self.parent.get_id()
            print("O id: "+str(self.id_))
        self.du.data = self.get_data()
        
    
    email_add_user = ObjectProperty(None)
    
    def get_data(self):
        datalist = []
        self.data = []
        print("Jestem tu")
        if not (self.log_in):
            
            next_list = []
            instance = DatabaseHandler()
            instance.createConnection()
            content = instance.findUsersForAdvanced(self.id_)
            print(content)
            for con in content:
                next_list.append(con[0])
            #"Wojciech Maj 1", "Piotr Łach 2 ","Wojciech Maj 3","Wojciech Maj 4","Wojciech Maj 5 ","Wojciech Maj 6", "Piotr Łach 7", "Dupa 8"]
            if not content:
                content = []
            else:
                
                datalist = instance.findUserByIdList(next_list)
                for i in datalist:
                    print(i)
                self.data = [{'text':str(x[1])+" "+str(x[2])} for x in datalist]
            instance.closeConnection()

        
        return self.data
    


    def on_press(self):
        
        if  self.email_add_user.text == '':
            self.error_pop('', 'Uzupełnij pole email')

        else:
            instance = DatabaseHandler()
            instance.createConnection()
            if not instance.findAnyEmail(self.email_add_user.text):
                if instance.findUserPrivilegesById(int(instance.findUserIDByEmail(self.email_add_user.text))):
                    if instance.insertUserAndAdvanced( self.parent.get_id(), self.email_add_user.text):
                        self.error_pop('', 'Pomyślnie dodałeś użytkownika')
                        instance.closeConnection()
                        self.on_load()
                        return True
                    else:
                        self.error_pop('', 'Nie powiodło się dodanie użytkownika')  
                else:
                    self.error_pop('', 'Dany użytkownik jest osobą wykwalifikowana nie możesz jej dodać')
            else:
                self.error_pop('', 'Użytkonik o podanym emailu nie istnije')
            instance.closeConnection()
            return False

    def error_pop(self, name, text):
        pop = Popup(title='Invalid Form',
                  content=Label(text=name+'\n'+text),
                  size_hint=(None, None), size=(400, 400))
        pop.open()


