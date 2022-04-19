import queue

# isort: split
import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

# isort: split
# spytać sie przemka jak obejść coś takiego czy to zostawić
import src.old_app.python_class.advance_class.a_Choose_lots_muscles_widget as AChooseLots
import src.old_app.python_class.advance_class.a_choose_method_widget as AChooseMeth
import src.old_app.python_class.advance_class.a_choose_user_widget as AChooseUser
import src.old_app.python_class.advance_class.a_finish_ref_widget as AFinishRef
import src.old_app.python_class.advance_class.a_managment_s_widget as AManagmentS
import src.old_app.python_class.advance_class.a_observation_exp_widget as AObserExp
import src.old_app.python_class.advance_class.a_observation_ref_widget as AObserRef
import src.old_app.python_class.advance_class.a_pauze_exp_widget as APauzeExp
import src.old_app.python_class.advance_class.a_reference_inst_widget as ARefInstr
import src.old_app.python_class.advance_class.a_start_guest_widget as AStartGuest
import src.old_app.python_class.advance_class.a_start_reference_widget as AStartRef

# isort: split
import src.old_app.python_class.auto_class.choose_lots_muscles_widget as ChooseLots
import src.old_app.python_class.auto_class.choose_method_widget as ChooseMeth
import src.old_app.python_class.auto_class.choose_user_widget as ChooseUser
import src.old_app.python_class.auto_class.finish_ref_widget as FinishRef
import src.old_app.python_class.auto_class.managment_s_widget as ManagmentS
import src.old_app.python_class.auto_class.observation_exp_widget as ObserExp
import src.old_app.python_class.auto_class.observation_ref_widget as ObserRef
import src.old_app.python_class.auto_class.pauze_exp_widget as PauzeExp
import src.old_app.python_class.auto_class.reference_inst_widget as RefInstr
import src.old_app.python_class.auto_class.start_guest_widget as StartGuest
import src.old_app.python_class.auto_class.start_reference_widget as StartRef
import src.old_app.python_class.help_widget as Help
import src.old_app.python_class.home_widget as Home
import src.old_app.python_class.kivy_builders.kivy_main_app_build as kivy_build
import src.old_app.python_class.sing_in_widget as SingIn
import src.old_app.python_class.sing_up_widget as SingUp
import src.old_app.python_class.user_pro_w as UserPro
import src.old_app.python_class.user_widget as User
import src.old_app.python_class.users_see as USee
import src.old_app.python_class.user_account_w as UserAccount
from src.grpc.python_client_server_dir.client_base_station_com.client import Client as ClientPi
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer

# isort: split
from src.user.measurement import Measurement
from src.user.user_logIn import UserLogIn

# replace with your current kivy version!
kivy.require("1.0.6")


class ScreenManagement(ScreenManager):
    

    def __init__(self, **kwargs):
        # self.q1.put('homewidget')
        super(ScreenManagement, self).__init__(**kwargs)
        self.q1 = queue.LifoQueue()
        self.home_widget = "homewidget"
        self.userLogIn = None
        self.noneLogIn = True
        self.count_ = 0
        self.see_account = None
        self.client_connect = ClientPi()
        self.connect_stats = False
        self.add_widget(Home.HomeWidget(name="homewidget"))
        self.add_widget(SingIn.SingInWidget(name="singinwidget"))
        self.add_widget(Help.HelpWidget(name="helpwidget"))
        self.add_widget(User.UserWidget(name="userwidget"))
        self.add_widget(UserAccount.UserAccountWidget(name="useraccountwidget"))
        self.add_widget(UserPro.UserProWidget(name="userprowidget"))
        # , index =(True, 0)))
        self.add_widget(USee.UsersSeeWidget(name="usersseewidget"))
        self.add_widget(SingUp.SingUpWidget(name="singupwidget"))
        self.add_widget(ChooseUser.ChooseUserWidget(name="chooseuserwidget"))
        self.add_widget(ChooseMeth.ChooseMethodWidget(name="choosemethodwidget"))
        self.add_widget(StartGuest.StartGuestWidget(name="startguestwidget"))
        self.add_widget(
            ChooseLots.ChooseLotsMusclesWidget(name="chooselotsmuscleswidget")
        )
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
        self.add_widget(
            AChooseLots.AChooseLotsMusclesWidget(name="a_chooselotsmuscleswidget")
        )
        self.add_widget(
            AManagmentS.AManagmentSensorsWidget(name="a_managmentsensorsidget")
        )
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
        self.count_ = 0

    def get_many(self):
        return self.userMean.get_many_sensor()

    def auto_refresh(self):
        self.clear_widgets(screens=[self.get_screen("usersseewidget")])
        # , index =(self.get_bool_LogIn(),self.get_id())))
        self.add_widget(USee.UsersSeeWidget(name="usersseewidget"))

    def log_in(self, id, login, name, surname, email):
        self.noneLogIn = False
        self.userLogIn = UserLogIn(id,login, name, surname, email)

    def how_meny(self, a: str):
        self.count_ += 1
        print("jestem " + str(self.count_))
        if self.count_ < self.get_many():
            return a + "referenceinstwidget"

        else:
            return a + "finishrefwidget"

    def restart_widget(self):
        self.clear_widgets(screens=[self.get_screen("observationrefwidget")])
        self.add_widget(ObserRef.ObservationRefWidget(name="observationrefwidget"))

    def A_restart_widget(self):
        self.clear_widgets(screens=[self.get_screen("a_observationrefwidget")])
        self.add_widget(AObserRef.AObservationRefWidget(name="a_observationrefwidget"))

    def get_count(self):
        return self.count_

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
    
    def get_login(self):
        return self.userLogIn.get_login()


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

    def connect_rasp(self):
        if self.client_connect.connect():
            self.connect_stats = True

    def status_connection(self):
        return self.connect_stats

    def get_see_account(self):
        return self.see_account

    def set_see_account(self, email):
        self.see_account = email

class MyApp(MDApp):
    def on_start(self):
        Window.size = (1000, 800)

    def build(self):

        kivy_build.Upload()

        return ScreenManagement()


if __name__ == "__main__":
    MyApp().run()
