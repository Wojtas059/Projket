# Form implementation generated from reading ui file 'sing_up_widget.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QMessageBox
from src.user.user_validator import UserValidator
from src.user.user import User
from src.database_handlers.database_handler import DatabaseHandler


class SingUp(QWidget):
    def __init__(self, parent):
        super(SingUp, self).__init__(parent)
        self.setObjectName("SingUp")
        self.resize(634, 536)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.imie = QtWidgets.QLabel(self)
        self.imie.setObjectName("imie")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.imie)
        self.name_5 = QtWidgets.QLabel(self)
        self.name_5.setObjectName("name_5")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name_5)
        self.name_6 = QtWidgets.QLabel(self)
        self.name_6.setObjectName("name_6")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name_6)
        self.name_7 = QtWidgets.QLabel(self)
        self.name_7.setObjectName("name_7")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name_7)
        self.name_8 = QtWidgets.QLabel(self)
        self.name_8.setObjectName("name_8")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name_8)
        self.name_9 = QtWidgets.QLabel(self)
        self.name_9.setObjectName("name_9")
        self.formLayout_2.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name_9)
        self.name = QtWidgets.QLineEdit(self)
        self.name.setObjectName("name")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.name)
        self.surname = QtWidgets.QLineEdit(self)
        self.surname.setObjectName("surname")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.surname)
        self.login = QtWidgets.QLineEdit(self)
        self.login.setObjectName("login")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.login)
        self.email = QtWidgets.QLineEdit(self)
        self.email.setObjectName("email")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.email)
        self.password = QtWidgets.QLineEdit(self)
        self.password.setObjectName("password")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password)
        self.confirm_password = QtWidgets.QLineEdit(self)
        self.confirm_password.setObjectName("confirm_password")
        self.formLayout_2.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.confirm_password)
        self.horizontalLayout.addLayout(self.formLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.user_advance = QtWidgets.QCheckBox(self)
        self.user_advance.setObjectName("user_advance")
        self.horizontalLayout_5.addWidget(self.user_advance)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.sing_up = QtWidgets.QPushButton(self)
        self.sing_up.setObjectName("sing_up")
        self.horizontalLayout_6.addWidget(self.sing_up)
        self.back = QtWidgets.QPushButton(self)
        self.back.setObjectName("back")
        self.horizontalLayout_6.addWidget(self.back)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 614, 138))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(self)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 614, 138))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)

        self.retranslateUi()
        self.addActionBattons()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SingUp", "Form"))
        self.imie.setText(_translate("SingUp", "Imię"))
        self.name_5.setText(_translate("SingUp", "Nazwisko"))
        self.name_6.setText(_translate("SingUp", "Login"))
        self.name_7.setText(_translate("SingUp", "Email"))
        self.name_8.setText(_translate("SingUp", "Hasło"))
        self.name_9.setText(_translate("SingUp", "Powtórz hasło"))
        self.user_advance.setText(_translate(
            "SingUp", "Użytkownik zaawansowany"))
        self.sing_up.setText(_translate("SingUp", "Zarejestruj się"))
        self.back.setText(_translate("SingUp", "Wróć"))

    def addActionBattons(self):
        self.sing_up.clicked.connect(lambda: self.register())
        self.back.clicked.connect(lambda: self.backScreen())

    def register(self):
        name = self.name.text()
        surname = self.surname.text()
        email = self.email.text()
        login = self.login.text()
        password = self.password.text()
        confirm_password = self.confirm_password.text()
        advanced_mode = int(self.user_advance.isChecked())
        str_error = ""
        if (
            name == "" or
            surname == "" or
            email == "" or
            login == "" or
            password == "" or
            confirm_password == ""
        ):
            str_error = "Uzupełnij wszystie pola"
            self.createMessageBox(str_error)
        else:
            if password.__eq__(confirm_password):
                print("test1")
                new_user = User(name=name, surname=surname, email=email,
                                login=login, password=password, advanced=advanced_mode)
                user_validator = UserValidator(new_user)
                data_error = user_validator.validateRegistration()
                licznik = 0

                if not data_error.get("NAME") == UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error += "Imie\njest za krotkie, minimum 4 zaki\n"
                if not data_error.get("SURNAME") == UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error += "Nazwisko\njest za krotkie, minimum 4 zaki\n"

                if not data_error.get("PASSWORD") == UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error += "Hasło\njest za krotkie, minimum 8 zaki\n"
                if not data_error.get("LOGIN") == UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error += "Login\njest za krotki, minimum 4 zaki\n"
                if (
                    not data_error.get("LOGINEXISTENCE")
                    == UserValidator.Flags.CORRECTFIELD
                ):
                    licznik += 1
                    str_error += "Login\nTaki login juz istnieje\n"
                if not data_error.get("EMAIL") == UserValidator.Flags.CORRECTFIELD:
                    licznik += 1
                    str_error += "Email\njest nie poprawny\n"
                if (
                    not data_error.get("EMAILEXISTENCE")
                    == UserValidator.Flags.CORRECTFIELD
                ):
                    licznik += 1
                    str_error += "Email\nTaki email juz istnieje\n"

                if licznik == 0:
                    databaseHandler = DatabaseHandler()
                    databaseHandler.createUser(new_user)
                    self.createMessageBox(
                        "Rejestracja powowiodła się pomyślnie"
                    )
                    return True
                else:
                    self.createMessageBox(str_error)
                    return False
            else:
                print("test2")
                message = "Hasła się niepokrywają"
                self.createMessageBox(message)

    def createMessageBox(self, message: str):
        msg = QMessageBox()
        msg.setWindowTitle("Błąd")
        msg.setText(message)
        msg.exec()

    def backScreen(self):
        self.parent().openLastWidget()
