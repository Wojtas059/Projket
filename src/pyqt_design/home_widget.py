# Form implementation generated from reading ui file 'home_widget_qt.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QWidget)

### Class type QWidget, responsible for set widget
class HomeWidget(QWidget):
    def __init__(self, parent ):
        super(HomeWidget, self).__init__(parent)

      
        self.setObjectName("Home Widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_4 = QtWidgets.QScrollArea(self)
        self.scrollArea_4.setLineWidth(0)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 675, 125))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.sing_up = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.sing_up.setObjectName("sing_up")
        self.horizontalLayout_3.addWidget(self.sing_up)
        self.sing_in = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.sing_in.setObjectName("sing_in")
        self.horizontalLayout_3.addWidget(self.sing_in)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_3.addWidget(self.scrollArea_4)
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.scrollArea_5 = QtWidgets.QScrollArea(self)
        self.scrollArea_5.setLineWidth(0)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 675, 125))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(245, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.auto_start = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.auto_start.setMinimumSize(QtCore.QSize(200, 48))
        self.auto_start.setMaximumSize(QtCore.QSize(200, 48))
        self.auto_start.setObjectName("auto_start")
        self.horizontalLayout_4.addWidget(self.auto_start)
        spacerItem1 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_3.addWidget(self.scrollArea_5)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.scrollArea_6 = QtWidgets.QScrollArea(self)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 677, 268))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_6)

        self.retranslateUi()
        self.addActionButtons()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    
    # Function set text label and button 
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Home Widget", "Home Widget"))
        self.label_2.setText(_translate("Home Widget", "Używasz aplikacji w trybie gość, zaloguj się albo zarejestruj!"))
        self.sing_up.setText(_translate("Home Widget", "Zarejestruj się"))
        self.sing_in.setText(_translate("Home Widget", "Zaloguj się "))
        self.auto_start.setText(_translate("Home Widget", "Rozpocznij badanie"))
    

    def retranslateSuccesLogIn(self):
        _translate = QtCore.QCoreApplication.translate
        self.setObjectName("Home Widget Succes Login")
        self.setWindowTitle(_translate("Home Widget", "Home Widget Succes Login"))
        self.label_2.setText(_translate("Home Widget", "Witaj "))
        self.sing_up.setText(_translate("Home Widget", "Profil"))
        self.sing_up.clicked.connect(lambda:self.userProfilShow())
        self.sing_in.setText(_translate("Home Widget", "Historia pomiarowa"))
        self.sing_in.clicked.connect(lambda:self.histroySeeShow())
        self.log_out = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.log_out.setObjectName("see_history")
        self.horizontalLayout_3.addWidget(self.log_out)
        self.log_out.setText(_translate("Home Widget", "Wyloguj się"))
        self.log_out.clicked.connect(lambda:self.addActionButtonLogOut())

    def retranslateHomeWidgetName(self, name):
        _translate = QtCore.QCoreApplication.translate 
        self.label_2.setText(_translate("Home Widget", "Witaj "+name))


    def addActionButtonLogOut(self):
        self.parent().homeShow()
    # Function declare action(other function) after pushing the button
    def addActionButtons(self):
        self.sing_up.clicked.connect(lambda:self.showScreen())
        self.sing_in.clicked.connect(lambda:self.showScreen())
        self.auto_start.clicked.connect(lambda:self.showScreen())

    def userProfilShow(self):
        self.parent().userProfilSeeShow()
    def histroySeeShow(self):
        self.parent().histroySeeShow()
    def addButtonHistoryUserSee(self):
        self.see_users = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.see_users.setObjectName("see_users")
        self.horizontalLayout_3.addWidget(self.see_users)
        _translate = QtCore.QCoreApplication.translate
        self.see_users.setText(_translate("Home Widget", "Twoi użytkownicy"))
        self.see_users.clicked.connect(lambda:self.seeUsers())

    # Function add name widget to lifo in the parent class and go to chosen widget
    def showScreen(self):
        objectName: str = str(self.sender().objectName())
        self.parent().addScreen(self.getWidget())
        if objectName.__eq__("sing_in"):
            self.parent().singInShow() 
        elif objectName.__eq__("sing_up"):
            self.parent().singUpShow() 
        elif objectName.__eq__("auto_start"):
            self.parent().chooseMethodShow() 

    def seeUsers(self):
        self.parent().addScreen(self.getWidget())
        self.parent().listUsersShow()

    # Function return name object used widget
    def getWidget(self):
        return str(self.objectName())
