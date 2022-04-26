from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QWidget)
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow 
import sys
import queue

# Import class of type QWidget from file
from src.pyqt_design.home_widget import HomeWidget
from src.pyqt_design.sing_in_widget import SingIn
from src.pyqt_design.sing_up_widget import SingUp
from src.pyqt_design.choose_method_widget import ChooseMethod
from src.pyqt_design.managment_sensor_widget import ManagmentSensor
from src.pyqt_design.video_referenec_widget import VideoPlayer
from src.pyqt_design.choose_lots_muscles_widget import ChooseLotsMuscles
from src.pyqt_design.start_reference_widget import StartReference


# Import class 
from src.user.user_logIn import UserLogIn


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        
        title = "Application"
        self.setWindowTitle(title)

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


     # Function add last used widget
    def addScreen(self, widget_name: str):
        self.lifo_use_widget.put(widget_name)

    # Function return last used name widget
    def lastScreen(self):
        return self.lifo_use_widget.get()

    # Function set data user after succes log in 
    def setUserCredentials(self, user_row: tuple, login:str, bool_advanced):
        self.user_login = UserLogIn(login=login,advanced=bool_advanced, id = user_row[0], name = user_row[1] ,surname= user_row[2] , email = user_row[3])

### Function set central widget ! ###
    
    # Function set center widget - home widget
    def homeShow(self):
        self.home_widget = HomeWidget(self)
        self.setCentralWidget(self.home_widget)
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

    def chooseMethodShow(self):
        self.choose_method = ChooseMethod(self)
        self.setCentralWidget(self.choose_method)
        self.show()

    # Function set center widget - sing in widget 
    def singInShow(self):
        self.sing_in = SingIn(self)
        self.setCentralWidget(self.sing_in)
        self.show()

    # Function set center widget - sing up widget 
    def singUpShow(self):
        self.sing_up = SingUp(self)
        self.setCentralWidget(self.sing_up)
        self.show()

    def videoPlayerShow(self):
        self.viode_player = VideoPlayer(self)
        self.setCentralWidget(self.viode_player)
        self.show()

    def managmentSensorShow(self):
        self.managment_sensor = ManagmentSensor(self)
        self.setCentralWidget(self.managment_sensor)
        self.show()

    def chooseLotsMusclesShow(self):
        self.choose_lots_muscles = ChooseLotsMuscles(self)
        self.setCentralWidget(self.choose_lots_muscles)
        self.show()

    def startReferenceShow(self):
        self.start_reference = StartReference(self)
        self.setCentralWidget(self.start_reference)
        self.show()
    
    # Function set center widget
    def openWidget(self, widget: QWidget):
        self.setCentralWidget(widget)
        self.show()

    def openLastWidget(self):
        widget_name = self.lastScreen()
        if widget_name.__eq__("Home Widget"):
            self.homeShow()
        if widget_name.__eq__("Choose Method"):
            self.chooseMethodShow()
        if widget_name.__eq__("Choose Lots Muscles"):
            self.chooseLotsMusclesShow()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyApp()
    sys.exit(app.exec())



    
