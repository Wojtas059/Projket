# kivy_venv\Scripts\activate
from operator import index
import queue
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import python_class.auto_class.Pauze_exp_widget as PauzeExp
import python_class.auto_class.Observation_exp_widget as ObserExp
import python_class.auto_class.Finish_ref_widget as FinishRef
import python_class.auto_class.Observation_ref_widget as ObserRef
import python_class.auto_class.Reference_inst_widget as RefInstr
import python_class.auto_class.Start_reference_widget as StartRef
import python_class.auto_class.Managment_s_widget as ManagmentS
import python_class.auto_class.Choose_lots_muscles_widget as ChooseLots
import python_class.auto_class.Start_guest_widget as StartGuest
import python_class.auto_class.Choose_method_widget as ChooseMeth
import python_class.auto_class.Choose_user_widget as ChooseUser

import python_class.advance_class.A_Pauze_exp_widget as APauzeExp
import python_class.advance_class.A_Observation_exp_widget as AObserExp
import python_class.advance_class.A_Finish_ref_widget as AFinishRef
import python_class.advance_class.A_Observation_ref_widget as AObserRef
import python_class.advance_class.A_Reference_inst_widget as ARefInstr
import python_class.advance_class.A_Start_reference_widget as AStartRef
import python_class.advance_class.A_Managment_s_widget as AManagmentS
import python_class.advance_class.A_Choose_lots_muscles_widget as AChooseLots
import python_class.advance_class.A_Start_guest_widget as AStartGuest
import python_class.advance_class.A_Choose_method_widget as AChooseMeth
import python_class.advance_class.A_Choose_user_widget as AChooseUser

import python_class.SingUp_widget as SingUp
import python_class.Users_see as USee
import python_class.User_pro_w as UserPro
import python_class.User_widget as User
import python_class.Help_widget as Help
import python_class.SingIn_widget as SingIn
import python_class.Home_widget as Home
import python_class.kivy_build as kivy_build
from User.UserLogIn import UserLogIn
from User.measurement import Measurement
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.core.window import Window
import kivy

from database_handlers.database_handler import DatabaseHandler
kivy.require('1.0.6')  # replace with your current kivy version !




class ScreenManagement(ScreenManager):
    q1 = queue.LifoQueue()
    home_widget = 'homewidget'
    userLogIn = None
    noneLogIn = True

    def __init__(self, **kwargs):
        # self.q1.put('homewidget')
        super(ScreenManagement, self).__init__(**kwargs)
        self.add_widget(Home.HomeWidget(name="homewidget"))
        self.add_widget(SingIn.SingInWidget(name="singinwidget"))
        self.add_widget(Help.HelpWidget(name="helpwidget"))
        self.add_widget(User.UserWidget(name="userwidget"))
        self.add_widget(UserPro.UserProWidget(name="userprowidget"))
        self.add_widget(USee.UsersSeeWidget(name="usersseewidget"))#, index =(True, 0)))
        self.add_widget(SingUp.SingUpWidget(name="singupwidget"))
        self.add_widget(ChooseUser.ChooseUserWidget(name="chooseuserwidget"))
        self.add_widget(ChooseMeth.ChooseMethodWidget(name="choosemethodwidget"))
        self.add_widget(StartGuest.StartGuestWidget(name="startguestwidget"))
        self.add_widget(ChooseLots.ChooseLotsMusclesWidget(name="chooselotsmuscleswidget"))
        self.add_widget(ManagmentS.ManagmentSensorsWidget(name="managmentsensorsidget"))
        self.add_widget(StartRef.StartReferenceWidget(name="startreferencewidget"))
        self.add_widget(RefInstr.ReferenceInstWidget(name="referenceinstwidget"))
        self.add_widget(ObserRef.ObservationRefWidget(name="observationrefwidget"))
        self.add_widget(FinishRef.FinishRefWidget(name="finishrefwidget"))
        self.add_widget(ObserExp.ObservationExpWidget(name="observationexpwidget"))
        self.add_widget(PauzeExp.PauzeExpWidget(name="pauzeexpwidget"))
        self.add_widget(AChooseUser.AChooseUserWidget(name="a_chooseuserwidget"))
        self.add_widget(AChooseMeth.AChooseMethodWidget(name="a_choosemethodwidget"))
        self.add_widget(AStartGuest.AStartGuestWidget(name="a_startguestwidget"))
        self.add_widget(AChooseLots.AChooseLotsMusclesWidget(name="a_chooselotsmuscleswidget"))
        self.add_widget(AManagmentS.AManagmentSensorsWidget(name="a_managmentsensorsidget"))
        self.add_widget(AStartRef.AStartReferenceWidget(name="a_startreferencewidget"))
        self.add_widget(ARefInstr.AReferenceInstWidget(name="a_referenceinstwidget"))
        self.add_widget(AObserRef.AObservationRefWidget(name="a_observationrefwidget"))
        self.add_widget(AFinishRef.AFinishRefWidget(name="a_finishrefwidget"))
        self.add_widget(AObserExp.AObservationExpWidget(name="a_observationexpwidget"))
        self.add_widget(APauzeExp.APauzeExpWidget(name="a_pauzeexpwidget"))
        self.userMean = Measurement()
        self.userMean.set_type("Auto_guest")

    def set_type(self, name):
        self.userMean.set_type(name)

    def set_many(self, many):
        self.userMean.set_many_sensor(many)
    
    def get_many(self):
        return self.userMean.get_many_sensor()

    def auto_refresh(self):
        self.clear_widgets(screens=[self.get_screen("usersseewidget")])
        self.add_widget(USee.UsersSeeWidget(name="usersseewidget"))#, index =(self.get_bool_LogIn(),self.get_id())))

    def log_in(self, id, name, surname, email):
        self.noneLogIn = False
        self.userLogIn = UserLogIn(id, name, surname, email)
        
        

    def get_bool_LogIn(self):
        return self.noneLogIn

    def log_out(self):
        self.noneLogIn = True
        self.userLogIn = None

    def get_id(self):
        return self.userLogIn.get_id()

    def get_email(self):
        return self.userLogIn.get_email()

    def get_name(self):
        return self.userLogIn.get_name()
    
    def get_surname(self):
        return self.userLogIn.get_surname()
    
    def get_userLogIn(self):
        return self.userLogIn

    def set_home_widget(self, name_widget):
        self.home_widget = name_widget
    
    def get_home_widget(self):
        return self.home_widget

    def add_screen(self, name):
        self.q1.put(name)

    def last_screen(self):
        return self.q1.get()

    def clear_screen(self):
        while not self.q1.empty():
            self.q1.get()


class MyApp(App):
    def on_start(self):
        Window.size = (1000, 800)
    def build(self):
        
        kivy_build.Upload()
        
        return ScreenManagement()



if __name__ == '__main__':
    MyApp().run()