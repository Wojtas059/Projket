from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QWidget)
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow 
import sys
import queue

# Import class of type QWidget from file
from src.pyqt_designe.home_widget import HomeWidget
from src.pyqt_designe.sing_in_widget import SingIn
from src.pyqt_designe.sing_up_widget import SingUp



class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        
        title = "Application"
        self.setWindowTitle(title)

    ### Create central widget ### 
        self.homeShow()
        self.resize(800, 600)
        self.setMinimumSize(500,200)
        self.setStyleSheet("QScrollArea { border: 0px;}")
        self._createMenuBar()


    ### Create menu bar
    def _createMenuBar(self):
        menubar = self.menuBar()
        ## Add help for users
        fileMenu = menubar.addMenu('Pomoc')
        exit = menubar.addMenu('Zakmknij')

        self.user_manual= QAction('Instrukcja obsługi', self)
        self.meas_procedure = QAction('Procedura pomiarowa', self)
        self.chatbot = QAction('Chatbot', self)

        fileMenu.addAction(self.user_manual)
        fileMenu.addAction(self.meas_procedure)
        fileMenu.addAction(self.chatbot)

        

    ### Create global virable ###
        # Add lifo queqe, responsible for stack/lifo last used widgets
        self.lifo_use_widget = queue.LifoQueue()




     # Function add last used widget
    def addScreen(self, widget_name: str):
        self.lifo_use_widget.put(widget_name)

    # Function return last used name widget
    def lastScreen(self):
        return self.lifo_use_widget.get()



### Function set central widget ! ###
    
    # Function set center widget - home widget
    def homeShow(self):
        self.ui = HomeWidget(self)
        self.setCentralWidget(self.ui )
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


    # Function set center widget
    def openWidget(self, widget: QWidget):
        self.setCentralWidget(widget)
        self.show()

    def openLastWidget(self):
        widget_name = self.lastScreen()
        if widget_name.__eq__("Home Widget"):
            self.homeShow()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyApp()
    sys.exit(app.exec())



    
