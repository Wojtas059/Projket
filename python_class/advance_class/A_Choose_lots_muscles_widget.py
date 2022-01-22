from logging import root
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.popup import Popup
from threading import Thread 
from kivy.uix.label import Label
from database_handlers.database_handler import DatabaseHandler
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class AUserListButton(RecycleView):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
    def get_data(self):
        self.data = ["Maj"]

    def get_par(self):
        return 3
    #def refresh_from_data(self):
    #    return super(UserListButton, self).refresh_from_data( self.data)
        

class BattonLabelSpinner(RecycleDataViewBehavior,GridLayout):
    id_user=ObjectProperty(None)
    label_text = ObjectProperty(None)
    spinner_musc = ObjectProperty(None)

    def __init__(self) -> None:
        super().__init__()
        print("pizda")
        self.get_values()

    def get_values(self):
        datalist = []
        self.data = []
        next_list = []
        instance = DatabaseHandler()
        instance.createConnection()
        f = open("name.txt", "r")
        for i in f:
            self.id_ = i
        print("to jest: "+self.id_user.text)
        content = instance.findUsersForAdvanced(self.id_)
        for con in content:
            next_list.append(con[0])
        if not content:
                content = []
        else:
            datalist = instance.findUserByIdList(next_list)
            self.data = [str(x[0])+" "+str(x[1])+" "+str(x[2]) for x in datalist]
            print(datalist)
            instance.closeConnection()
        return  self.data


    def on_load(self):
        listData = []
        instance = DatabaseHandler()
        instance.createConnection()
        
        for i in instance.getAllMuscles():
            listData.append(i[-1])
        instance.closeConnection()
        self.get_values()
        return listData

    def update(self):
        self.spinner_user.values = self.get_values()

    def on_press(self):
        content = Button(text='Close me!')
        pop = Popup(title='Invalid Form',
                  content=content,
                  size_hint=(None, None), size=(400, 400))
        pop.open()
   
    def error_pop(self, name, text):
        pop = Popup(title='Invalid Form',
                  content=Label(text=name+'\n'+text),
                  size_hint=(None, None), size=(400, 400))
        pop.open()

    #TODO Tutaj ma byc obsluga uzyskanych danych, return ma byc nie zmieniany
    #W razie omówię PŁ
    def callbackPop(self,instance):
        return True

    def create_popup(self):
        self.pup = CustomPopup(self.id_user.values)
        self.pup.bind(on_dismiss=self.callbackPop)
        self.pup.open()
        #Thread(target=self.new).start()
        #self.label_text.text = str(self.pup.get_name())

        

    def new(self):
        while isinstance(self.pup, Popup):
            None
        self.label_text.text = str(self.pup.get_name())


class CustomPopup(Popup):
    email_add_user = ObjectProperty(None)
    popup =ObjectProperty(None)
    spinner_user = ObjectProperty(None)
    name = None
    id_ = 3
    id_choose_usr = None
    

    def __init__(self, id):
        super().__init__()
#
        self.id_ = id
        self.get_values()
#
    def get_id(self):
        return self.id_choose_usr

    def get_name(self):
        return self.name

    def get_values(self):
        datalist = []
        self.data = []
        next_list = []
        f = open("name.txt", "r")
        for i in f:
            self.id_ = i
        instance = DatabaseHandler()
        instance.createConnection()
        content = instance.findUsersForAdvanced(self.id_)
        for con in content:
            next_list.append(con[0])
        if not content:
                content = []
        else:
            datalist = instance.findUserByIdList(next_list)
            self.data = [str(x[0])+" "+str(x[1])+" "+str(x[2]) for x in datalist]
            print(datalist)
            instance.closeConnection()
        return self.data

    def choose_clicked(self, text:str):
        datalist = []
        datalist = text.split(' ')
        self.id_choose_usr = datalist[0]

    def error_pop(self,name, text):
        pop = Popup(title='Invalid Form',
                  content=Label(text=name+'\n'+text),
                  size_hint=(None, None), size=(400, 400))
        pop.open()
        #self.popup.dismiss()

    def on_press(self):
        if self.spinner_user.text == 'Wybierz Użytkownika':
            self.error_pop("Erroe","Proszę wybrać użytkownika")
        else:
            f = open("name.txt", "w")
            f.write(self.spinner_user.text)
            f.close
            self.name = self.spinner_user.text

            


    def add_new_user(self):
        
        if  self.email_add_user.text == '':
            self.error_pop('', 'Uzupełnij pole email')

        else:
            instance = DatabaseHandler()
            instance.createConnection()
            if not instance.findAnyEmail(self.email_add_user.text):
                if instance.findUserPrivilegesById(int(instance.findUserIDByEmail(self.email_add_user.text))):
                    if instance.insertUserAndAdvanced( self.id_, self.email_add_user.text):
                        self.error_pop('Sukces', 'Pomyślnie dodałeś użytkownika')
                        instance.closeConnection()
                        self.dismiss()
                        #return True
                    else:
                        self.error_pop('', 'Nie powiodło się dodanie użytkownika')  
                else:
                    self.error_pop('', 'Dany użytkownik jest osobą wykwalifikowana nie możesz jej dodać')
            else:
                self.error_pop('', 'Użytkonik o podanym emailu nie istnije')
            instance.closeConnection()
            #return False








class AChooseLotsMusclesWidget(Screen):
    many_ = ObjectProperty(None)
    recyView = ObjectProperty(None)

    def choose_clicked( self, many):
        self.recyView.disabled = False
        f = open("name.txt", "w")
        f.write(str(self.id_))
        f.close
        self.recyView.data = [{'text': str(self.id_), 'values': str(self.id_)} for x in range(int(many))]    
        

    def pizda(self):
        print("Pizda")
    def on_load(self):
        self.recyView.disabled = True
        listData = []
        self.id_ = self.parent.get_id()
        self.many_.values = [str(x) for x in range(1,21)]

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