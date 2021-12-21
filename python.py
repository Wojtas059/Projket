# kivy_venv\Scripts\activate
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.properties import ObjectProperty

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import python_class.kivy_build as kivy_build
import python_class.Home_widget as Home
import python_class.SingIn_widget as SingIn
import python_class.Help_widget as Help
import python_class.User_widget as User
import python_class.User_pro_w as UserPro
import python_class.Users_see as USee




class MyApp(App):
    def build(self):
        kivy_build.Upload()
        sm = ScreenManager()
        sm.add_widget(Home.HomeWidget(name="homewidget"))
        sm.add_widget(SingIn.SingInWidget(name="singinwidget"))
        sm.add_widget(Help.HelpWidget(name="helpwidget"))
        sm.add_widget(User.UserWidget(name="userwidget"))
        sm.add_widget(UserPro.UserProWidget(name="userprowidget"))
        sm.add_widget(USee.UsersSeeWidget(name="usersseewidget"))
        return sm


if __name__ == '__main__':
    MyApp().run()