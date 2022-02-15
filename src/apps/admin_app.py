import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

import src.python_class.home_admin_widget as Home
import src.python_class.kivy_builders.kivy_admin_builder as kivy_build

kivy.require("1.0.6")  # replace with your current kivy version !


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        self.add_widget(Home.HomeAdminWidget(name="home_admin_widget"))


class MyApp(App):
    def build(self):
        kivy_build.Upload()

        return ScreenManagement()


if __name__ == "__main__":
    MyApp().run()
