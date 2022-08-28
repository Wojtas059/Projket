# Form implementation generated from reading ui file 'sing_in_widget.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QWidget

from src.database_handlers.database_handler import DatabaseHandler
from src.user.user import User
from src.user.user_validator import UserValidator


class SingIn(QWidget):
    def __init__(self, parent):
        super(SingIn, self).__init__(parent)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 534, 124))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.login = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.horizontalLayout_2.addWidget(self.password)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem4)
        self.log_in = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.log_in.setObjectName("log_in")
        self.horizontalLayout_3.addWidget(self.log_in)

        self.back = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.back.setObjectName("back")
        self.horizontalLayout_3.addWidget(self.back)
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(self)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 534, 124))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 534, 124))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollArea_3)
        self.addActionButtons()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Hasło"))
        self.log_in.setText(_translate("Form", "Zaloguj się"))
        self.back.setText(_translate("Form", "Wróć"))

    def addActionButtons(self):
        self.log_in.clicked.connect(lambda: self.logIn())
        self.back.clicked.connect(lambda: self.backScreen())

    def backScreen(self):
        self.parent().openLastWidget()

    # Function add name widget to lifo in the parent class and go to chosen widget
    def showScreen(self):
        objectName: str = str(self.sender().objectName())
        self.parent().addScreen(self.getWidget())
        if objectName.__eq__("sing_in"):
            self.parent().singInShow()

    # Function return name object used widget
    def getWidget(self):
        return str(self.objectName())

    def logIn(self):
        if self.checkCredentials():
            bool_advanced = self.getUserPrivileges()
            self.getUserCredentials(bool_advanced)
            self.parent().homeShowSuccesLogIn()
            
    def checkCredentials(self):
        if self.login.text() == "" or self.password.text() == "":
            self.createMessageBox("Uzupełnij wszytskie pola")

        else:
            self.user = User(self.login.text(), self.password.text())
            self.uvaild = UserValidator(self.user)
            data_error = {}
            data_error = self.uvaild.validateLoginOperation()
            if (
                data_error.get("LOGINEXISTENCE") == UserValidator.Flags.CORRECTFIELD
                and data_error.get("PASSWORDCORRECTNESS")
                == UserValidator.Flags.CORRECTFIELD
            ):
                self.login_ = self.login.text()
                return True

            else:
                self.createMessageBox("Nie poprawy email lub haslo")
                return False

    def getUserCredentials(self, bool_advanced):
        instance = DatabaseHandler()
        instance.createConnection()
        row = instance.getUserCredentials(self.login_)
        self.parent().setUserCredentials(row, self.login_, bool_advanced)
        instance.closeConnection()

    def getUserPrivileges(self):
        instance = DatabaseHandler()
        instance.createConnection()
        bool_Advance_User = instance.findUserPrivilegesByLogin(self.login_)
        instance.closeConnection()
        return bool_Advance_User

    def createMessageBox(self, message: str):
        msg = QMessageBox()
        msg.setWindowTitle("Błąd")
        msg.setText(message)
        msg.exec()
