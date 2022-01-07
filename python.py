# kivy_venv\Scripts\activate
import queue
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import python_class.Pauze_exp_widget as PauzeExp
import python_class.Observation_exp_widget as ObserExp
import python_class.Finish_ref_widget as FinishRef
import python_class.Observation_ref_widget as ObserRef
import python_class.Reference_inst_widget as RefInstr
import python_class.Start_reference_widget as StartRef
import python_class.Managment_s_widget as ManagmentS
import python_class.Choose_lots_muscles_widget as ChooseLots
import python_class.Start_guest_widget as StartGuest
import python_class.Choose_method_widget as ChooseMeth
import python_class.Choose_user_widget as ChooseUser
import python_class.SingUp_widget as SingUp
import python_class.Users_see as USee
import python_class.User_pro_w as UserPro
import python_class.User_widget as User
import python_class.Help_widget as Help
import python_class.SingIn_widget as SingIn
import python_class.Home_widget as Home
import python_class.kivy_build as kivy_build
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.app import App
import kivy

from database_handlers.database_handler import DatabaseHandler
kivy.require('1.0.6')  # replace with your current kivy version !




class ScreenManagement(ScreenManager):
    q1 = queue.LifoQueue()

    def __init__(self, **kwargs):
        # self.q1.put('homewidget')
        super(ScreenManagement, self).__init__(**kwargs)
        self.add_widget(Home.HomeWidget(name="homewidget"))
        self.add_widget(SingIn.SingInWidget(name="singinwidget"))
        self.add_widget(Help.HelpWidget(name="helpwidget"))
        self.add_widget(User.UserWidget(name="userwidget"))
        self.add_widget(UserPro.UserProWidget(name="userprowidget"))
        self.add_widget(USee.UsersSeeWidget(name="usersseewidget"))
        self.add_widget(SingUp.SingUpWidget(name="singupwidget"))
        self.add_widget(ChooseUser.ChooseUserWidget(name="chooseuserwidget"))
        self.add_widget(ChooseMeth.ChooseMethodWidget(
            name="choosemethodwidget"))
        self.add_widget(StartGuest.StartGuestWidget(name="startguestwidget"))
        self.add_widget(ChooseLots.ChooseLotsMusclesWidget(
            name="chooselotsmuscleswidget"))
        self.add_widget(ManagmentS.ManagmentSensorsWidget(
            name="managmentsensorsidget"))
        self.add_widget(StartRef.StartReferenceWidget(
            name="startreferencewidget"))
        self.add_widget(RefInstr.ReferenceInstWidget(
            name="referenceinstwidget"))
        self.add_widget(ObserRef.ObservationRefWidget(
            name="observationrefwidget"))
        self.add_widget(FinishRef.FinishRefWidget(name="finishrefwidget"))
        self.add_widget(ObserExp.ObservationExpWidget(
            name="observationexpwidget"))
        self.add_widget(PauzeExp.PauzeExpWidget(name="pauzeexpwidget"))

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