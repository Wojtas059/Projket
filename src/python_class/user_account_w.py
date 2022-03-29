import kivy

kivy.require("1.0.6")  # replace with your current kivy version !
from kivy.uix.screenmanager import Screen
from src.database_handlers.database_handler import DatabaseHandler
from kivy.properties import ObjectProperty

class UserAccountWidget(Screen):
    name_text = ObjectProperty(None)
    surname_text = ObjectProperty(None)
    email_text = ObjectProperty(None)

    def on_load(self):
        instance = DatabaseHandler()
        instance.createConnection()
        row = instance.getUserCredentials(self.parent.get_login())
        self.name_text.text = row[1]
        self.surname_text.text = row[2]
        self.email_text.text = row[3]

    


