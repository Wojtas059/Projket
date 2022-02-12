import kivy

from src.database_handlers.database_handler import DatabaseHandler

kivy.require("1.0.6")  # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


class HomeAdminWidget(Screen):
    def resetDatabase(self):
        databaseHandler = DatabaseHandler()
        databaseHandler.createConnection()
        databaseHandler.dropAndCreateTables()
        databaseHandler.closeConnection()
