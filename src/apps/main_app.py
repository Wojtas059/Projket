from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtWidgets import QMainWindow 
import sys
from src.pyqt_designe.home_widget import HomeWidget
from src.pyqt_designe.sing_up_widget import SingIn
from src.pyqt_designe.home_widget_qt import Ui_Form



class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        title = "Application"

        ### Create central widget ### 
        self.setWindowTitle(title)
        self.home_show()
        self.resize(800, 600)
        self.setMinimumSize(600,400)
        self.setStyleSheet("QScrollArea { border: 0px;}")

    def home_show(self):
        self.ui = Ui_Form(self)
        self.setCentralWidget(self.ui )
        self.show()
        
    def sing_in_show(self):
        self.sing_in = SingIn(self)
        self.setCentralWidget(self.sing_in)
        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyApp()
    sys.exit(app.exec())



    
