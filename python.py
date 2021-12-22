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
import python_class.SingUp_widget as SingUp
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import queue



class ScreenManagement(ScreenManager):
    q1 = queue.LifoQueue()
    def __init__(self,**kwargs):
        #self.q1.put('homewidget')
        super(ScreenManagement, self).__init__(**kwargs)
        self.add_widget(Home.HomeWidget(name="homewidget"))
        self.add_widget(SingIn.SingInWidget(name="singinwidget"))
        self.add_widget(Help.HelpWidget(name="helpwidget"))
        self.add_widget(User.UserWidget(name="userwidget"))
        self.add_widget(UserPro.UserProWidget(name="userprowidget"))
        self.add_widget(USee.UsersSeeWidget(name="usersseewidget"))
        self.add_widget(SingUp.SingUpWidget(name="singupwidget"))

    def add_screen(self, name):

        self.q1.put(name)

    def last_screen(self):
        return self.q1.get()
        
    def clear_screen(self):
        while not self.q1.empty():
            self.q1.get()

class MyApp(App):
    def build(self):
        kivy_build.Upload()
        
        return ScreenManagement()

    

    

if __name__ == '__main__':
    MyApp().run()