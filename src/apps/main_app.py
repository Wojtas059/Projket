from optparse import Values
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QWidget)
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow 
import sys
import queue
from src.grpc.python_client_server_dir.client_base_station_com.client import Client as ClientPi
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
from threading import Thread

# Import class of type QWidget from file
from src.pyqt_design.home_widget import HomeWidget
from src.pyqt_design.sing_in_widget import SingIn
from src.pyqt_design.sing_up_widget import SingUp
from src.pyqt_design.choose_method_widget import ChooseMethod
from src.pyqt_design.managment_sensor_widget import ManagmentSensor
from src.pyqt_design.choose_lots_muscles_widget import ChooseLotsMuscles
from src.pyqt_design.start_reference_widget import StartReference
from src.pyqt_design.video_player import VideoPlayer
from src.pyqt_design.observation_reference import ObservationReference
from src.pyqt_design.start_exp_widget import StartExperience
from src.pyqt_design.user_profil_widget import UserProfilSee
from src.pyqt_design.list_users_widget import ListUsers
from src.pyqt_design.choose_lots_muscles_advanced_widget import ChooseLotsMusclesAdvanced
from src.pyqt_design.experience_observation_widget import ExperienceObservationWidget
from src.pyqt_design.graph_observation_widget import GraphObservationWidget

# Import class 
from src.user.user_logIn import UserLogIn
from src.experience_class.manage_sensor import ManageSensor
from src.experience_class.activity_exp import ActivityExperience

from src.database_handlers.database_handler import DatabaseHandler
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        title = "Application"
        self.setWindowTitle(title)
        self.see_grpah:bool = False
        self.see_number: int = None
        self.dataQueue_1 = queue.Queue()
        

    ### Create central widget ### 
        self.homeShow()
        #self.videoPlayerShow()
        self.resize(800, 600)
        self.setMinimumSize(500,200)
        self.setStyleSheet("QScrollArea { border: 0px;}")
        self._createMenuBar()


    ### Create menu bar
    def _createMenuBar(self):
        menubar = self.menuBar()
        ## Add help for users
        self.fileMenu = menubar.addMenu('Pomoc')
        self.exit = menubar.addMenu('Zamknij')


        self.user_manual= QAction('Instrukcja obsługi', self)
        self.meas_procedure = QAction('Procedura pomiarowa', self)
        self.chatbot = QAction('Chatbot', self)

        self.fileMenu.addAction(self.user_manual)
        self.fileMenu.addAction(self.meas_procedure)
        self.fileMenu.addAction(self.chatbot)

    ### Create global virable ###
        # Add lifo queqe, responsible for stack/lifo last used widgets
        self.lifo_use_widget = queue.LifoQueue()

        # Create object UserLogIn
        self.user_login = UserLogIn()

        # Create object ManageSensor
        self.manage_sensor = ManageSensor()

        # Create object ActivityExperience
        self.activity_experience = ActivityExperience()

     # Function add last used widget
    def addScreen(self, widget_name: str):
        self.lifo_use_widget.put(widget_name)

    # Function return last used name widget
    def lastScreen(self):
        return self.lifo_use_widget.get()

    # Function set data user after succes log in 
    def setUserCredentials(self, user_row: tuple, login:str, bool_advanced):
        self.user_login = UserLogIn(login=login,advanced=bool_advanced, id = user_row[0], name = user_row[1] ,surname= user_row[2] , email = user_row[3])

    # Function set quantity uses sensor
    def setQuantityMangeSensor(self, quantity: int):
        self.manage_sensor.setQuantityDataSensor(quantity)

    # Function get quantity uses sensor
    def getQuantityMangeSensor(self)->int:
        return self.manage_sensor.getQuantityDataSensor()

    # Function add value to manage sensor object
    def addKeyValueMangeSensor(self, name: str, muscules: str):
        
        if self.user_login.get_name().__eq__(""):
            name_surname = "gosc gosc"
        else:
            name_surname = self.user_login.get_name() +" "+ self.user_login.get_surname()

        value = [name_surname, muscules]
        self.manage_sensor.addKeyValueDataSensor(name, value)


    def addKeyValueMangeSensorUsers(self, name: str,name_surname:str, muscules: str):
        value = [name_surname, muscules]
        self.manage_sensor.addKeyValueDataSensor(name, value)

    # Function adding ip_addres to list manage sensor object
    def addIpAddressManageSensor(self, ip_addres: str):
        self.manage_sensor.addIpAddressSensor(ip_addres)

    # Function  delete key and value from data_sensor type of dict , managerSensor object
    def deleteKeyValueManageSensor(self, key_name: str):
        self.manage_sensor.deleteKeyValueDataSensor(key_name)


    def setActivityExperience(self, type_activity: str, type_exercise: str, type_physique: str,humidity: str):
        self.activity_experience = ActivityExperience(type_activity=type_activity, type_exercise=type_exercise, type_physique=type_physique, humidity=humidity )

    

    def connectBaseStation(self)->bool:
        self.client_connect = ClientPi()
        if self.client_connect.connect() and self.client_connect.startSTM() :
            Thread(target=self.getDataSTM).start()
            return True
        else:
            return False

    def stopSTMdata(self):
        if self.client_connect.stopSTM():
            print("Udało się ")
        else:
            print("Nie udało się")

    def startSTM(self):
        if self.client_connect.startSTM():
            Thread(target=self.getDataSTM).start()
        else:
            print("Nie udało się")


    def setSeeNumberGraph(self, number:int):
        self.see_number = number
        self.see_grpah = True
        self.dataQueue_1 = None
        self.dataQueue_1 = queue.Queue()
    def getDataSTM(self):
        if(self.client_connect.transfer_status):
            results = self.client_connect.stub.sendSTMData(ServicerMethods.Void())
            for result in results:
                print(result.data)
                dataarray = result.data.split(',')
                if self.see_grpah:
                    self.dataQueue_1.put(float(dataarray[self.see_number]))
### Function set central widget ! ###
    
    # Function set center widget - home widget
    def homeShow(self):
        self.user_login = UserLogIn()
        self.home_widget = HomeWidget(self)
        self.setCentralWidget(self.home_widget)
        self.show()

    def singInShow(self):
        self.sing_in = SingIn(self)
        self.setCentralWidget(self.sing_in)
        self.show()

    # Function set center widget - sing up widget 
    def singUpShow(self):
        self.sing_up = SingUp(self)
        self.setCentralWidget(self.sing_up)
        self.show()
    # Function set center widget - home widget for succes log in user
    def homeShowSuccesLogIn(self, user_advanced: bool):
        self.home_widget = HomeWidget(self)
        if not user_advanced:
            self.home_widget.addButtonHistoryUserSee()
        self.home_widget.retranslateSuccesLogIn()
        self.home_widget.retranslateHomeWidgetName(self.user_login.get_name())
        self.setCentralWidget(self.home_widget)
        self.show()

    def userProfilSeeShow(self):
        self.userprofilsee = UserProfilSee(self)
        self.setCentralWidget(self.userprofilsee)
        self.show()

    def chooseMethodShow(self):
        self.choose_method = ChooseMethod(self)
        self.setCentralWidget(self.choose_method)
        self.show()

    def listUsersShow(self):
        self.list_users = ListUsers(self)
        self.setCentralWidget(self.list_users)
        self.show()
    # Function set center widget - sing in widget 
    

    

    
    def chooseLotsMusclesShow(self):
        self.choose_lots_muscles = ChooseLotsMuscles(self)
        self.setCentralWidget(self.choose_lots_muscles)
        self.show()
    
    def chooseLotsMusclesAdvancedShow(self):
        self.choose_lots_muscles_advanced = ChooseLotsMusclesAdvanced(self)
        self.setCentralWidget(self.choose_lots_muscles_advanced)
        self.show()

    def managmentSensorShow(self):
        self.managment_sensor = ManagmentSensor(self)
        self.setCentralWidget(self.managment_sensor)
        self.show()

    def startReferenceShow(self):
        self.start_reference = StartReference(self)
        self.setCentralWidget(self.start_reference)
        self.show()
    
    def videoPlayerShow(self):
        self.viode_player = VideoPlayer(self)
        self.setCentralWidget(self.viode_player)
        self.show()
    
    def observationReferenceShow(self):
        self.start_reference = ObservationReference(self)
        self.setCentralWidget(self.start_reference)
        self.show()
    
    def startExperienceShow(self):
        self.start_exp = StartExperience(self)
        self.setCentralWidget(self.start_exp)
        self.show()
    
    def experienceObservationShow(self):
        self.exp_observation = ExperienceObservationWidget(self)
        self.setCentralWidget(self.exp_observation)
        self.show()

    def graphObservationShow(self, id:int=0, name_users:str = "",choose_muscles:str="" ):
        self.graph_observation = GraphObservationWidget(self, id = id, name_users=name_users, choose_muscles=choose_muscles)
        self.setCentralWidget(self.graph_observation)
        self.show()

    # Function set center widget
    def openWidget(self, widget: QWidget):
        self.setCentralWidget(widget)
        self.show()

    def openLastWidget(self):
        widget_name = self.lastScreen()
        if widget_name.__eq__("Home Widget"):
            self.homeShow()
        if widget_name.__eq__("Home Widget Succes Login"):
            self.homeShowSuccesLogIn(self.user_login.get_advanced())
        if widget_name.__eq__("Choose Method"):
            self.chooseMethodShow()
        if widget_name.__eq__("Choose Lots Muscles"):
            self.chooseLotsMusclesShow()
        if widget_name.__eq__("Managment Sensor"):
            self.managmentSensorShow()
        if widget_name.__eq__("Start Reference"):
            self.startReferenceShow()
        if widget_name.__eq__("Video Player"):
            self.videoPlayerShow()
        if widget_name.__eq__("Observation Reference"):
            self.observationReferenceShow()
        if widget_name.__eq__("Start Experience"):
            self.startExperienceShow()
        if widget_name.__eq__("Experience"):
            self.experienceObservationShow()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyApp()
    sys.exit(app.exec())



    
