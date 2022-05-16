# self implementation generated from reading ui file '.\choose_lots_muscles_widget.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QWidget,QMessageBox)
from src.database_handlers.database_handler import DatabaseHandler


class ChooseLotsMuscles(QWidget):
    def __init__(self, parent):
        super(ChooseLotsMuscles, self).__init__(parent)
        self.setObjectName("Choose Lots Muscles")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.many_muscles = QtWidgets.QComboBox(self)
        self.many_muscles.setObjectName("many_muscles")
        self.number:int = 1
        self.many_muscles.addItem("1")
        self.many_muscles.addItem("2")
        self.horizontalLayout.addWidget(self.many_muscles)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.choose_1 = QtWidgets.QComboBox(self)
        self.choose_1.setObjectName("sensor_1")
        self.choose_1.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.choose_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.choose_2 = QtWidgets.QComboBox(self)
        self.choose_2.setObjectName("sensor_2")
        self.choose_2.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.choose_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.back = QtWidgets.QPushButton(self)
        self.back.setObjectName("back")
        self.horizontalLayout_5.addWidget(self.back)
        self.next = QtWidgets.QPushButton(self)
        self.next.setObjectName("next")
        self.next.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.next)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 158))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi()
        self.addActionButtons()
        self.addItemMuscules()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Wybierz liczbę taśm"))
        self.back.setText(_translate("Form", "Wróć"))
        self.next.setText(_translate("Form", "Dalej"))

    def addActionButtons(self):
        self.next.clicked.connect(lambda: self.showScreen())
        self.many_muscles.view().pressed.connect(self.selectItemActivity)
        self.back.clicked.connect(lambda: self.backScreen())

        self.choose_1.currentTextChanged.connect(self.selectItemChooseMuscules)
        self.choose_2.currentTextChanged.connect(self.selectItemChooseMuscules)

    def addItemMuscules(self):
        instance = DatabaseHandler()
        instance.createConnection()
        for i in instance.getAllMuscles():
            self.choose_1.addItem(i[-1])
            self.choose_2.addItem(i[-1])
        instance.closeConnection()

    def selectItemChooseMuscules(self, s):
        objectName: str = str(self.sender().objectName())
        self.parent().addKeyValueMangeSensor(objectName, s)
        

    def selectItemActivity(self, index):
        self.many_muscles.setEnabled(True)
        self.next.setEnabled(True)
        item = self.many_muscles.model().itemFromIndex(index)
        if str(item.text()).__eq__("1"):
            self.choose_1.setEnabled(True)
            self.choose_2.setEnabled(False)
            self.number: int = 1
            self.parent().setQuantityMangeSensor(1)
            
        elif str(item.text()).__eq__("2"):
            self.choose_1.setEnabled(True)
            self.choose_2.setEnabled(True)
            self.number: int = 2
            self.parent().setQuantityMangeSensor(2)
            
        self.next.setEnabled(True)
        


    def backScreen(self):
        self.parent().openLastWidget()

    def showScreen(self):
        if self.many_muscles.currentText().__eq__("1"):
            self.parent().deleteKeyValueManageSensor("sensor_2")

        self.parent().addScreen(self.getWidget())
        self.parent().managmentSensorShow(self.number)
    
    def getWidget(self):
        return str(self.objectName())
