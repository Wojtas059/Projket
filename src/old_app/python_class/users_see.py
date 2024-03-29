import queue

# isort: split
import kivy
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen

# isort: split
from src.database_handlers.database_handler import DatabaseHandler

kivy.require("1.0.6")  # replace with your current kivy version !

csvQueue = queue.Queue()


class UserListButton(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []

    def get_data(self):
        self.data = ["Maj"]


class BattonLabel(RecycleDataViewBehavior, GridLayout):
    nazwa = ObjectProperty(None)

    def see_user_pop(self, name, emial):
        pop = Popup(
            title="Dane użytkownika",
            content=Label(text="Imie i nazwisko: " + name + "\n" + "Email: " + emial),
            size_hint=(None, None),
            size=(400, 400),
        )
        pop.open()


class UsersSeeWidget(Screen):
    log_in = True
    du = ObjectProperty(None)

    def on_load(self):
        self.log_in = self.parent.get_bool_LogIn()
        print("Jestem zalogowany: " + str(self.log_in))
        if not self.log_in:
            self.id_ = self.parent.get_id()
            print("O id: " + str(self.id_))
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
            if not content:
                content = []
            else:

                datalist = instance.findUserByIdList(next_list)
                self.data = [
                    {"text": str(x[1]) + " " + str(x[2]), "hint_text": str(x[4])}
                    for x in datalist
                ]
            instance.closeConnection()

        return self.data

    def on_press(self):

        if self.email_add_user.text == "":
            self.error_pop("", "Uzupełnij pole email")

        else:
            instance = DatabaseHandler()
            instance.createConnection()
            if not instance.findAnyEmail(self.email_add_user.text):
                if instance.findUserPrivilegesById(
                    int(instance.findUserIDByEmail(self.email_add_user.text))
                ):
                    if instance.insertUserAndAdvanced(
                        self.parent.get_id(), self.email_add_user.text
                    ):
                        self.error_pop("", "Pomyślnie dodałeś użytkownika")
                        instance.closeConnection()
                        self.on_load()
                        return True
                    else:
                        self.error_pop("", "Nie powiodło się dodanie użytkownika")
                else:
                    self.error_pop(
                        "",
                        "Dany użytkownik jest osobą wykwalifikowana nie możesz jej dodać",
                    )
            else:
                self.error_pop("", "Użytkonik o podanym emailu nie istnije")
            instance.closeConnection()
            return False

    def error_pop(self, name, text):
        pop = Popup(
            title="Invalid Form",
            content=Label(text=name + "\n" + text),
            size_hint=(None, None),
            size=(400, 400),
        )
        pop.open()
