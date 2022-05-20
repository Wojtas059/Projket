# self implementation generated from reading ui file '.\choose_lots_muscles_widget.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QWidget,QMessageBox, QHBoxLayout)
from src.database_handlers.database_handler import DatabaseHandler

class ChooseMuscles(QHBoxLayout):
    def __init__(self,  **kwargs):
        super(ChooseMuscles, self).__init__()

        self.number:int = kwargs.get('id', 0)
        list_muscles:list = kwargs.get('list_muscles', [])
        list_users:list = kwargs.get('list_users', [])
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.addItem(spacerItem)
        self.choose_users = QtWidgets.QComboBox()
        self.choose_users.setObjectName("choose_users")
        self.addWidget(self.choose_users)
        self.choose_muscles = QtWidgets.QComboBox()
        self.choose_muscles.setObjectName("choose_muscles")
        self.addWidget(self.choose_muscles)
        for i in list_muscles:
            self.choose_muscles.addItem(i[-1])
        for i in list_users:
            self.choose_users.addItem(i)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ManagmentSensor", '{:02d}'.format(self.number+1)))

    def getNumberBlocks(self)->int:
        return self.number

    def getNameUser(self)->str:
        return self.choose_users.currentText()
    
    def getNameMuscles(self)->str:
        return self.choose_muscles.currentText()

class ChooseLotsMusclesAdvanced(QWidget):
    def __init__(self, parent):
        super(ChooseLotsMusclesAdvanced, self).__init__(parent)

        self.setObjectName("Choose Lots Muscles Advanced")
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

        for i in range(20):
            
            self.many_muscles.addItem(str(i+1))

        self.horizontalLayout.addWidget(self.many_muscles)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        
        self.scrollArea_2 = QtWidgets.QScrollArea()
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout.addWidget(self.scrollArea_2)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.list_class_choose_muscles:list = []
        self.retranslateUi()
        self.addActionButtons()
        self.id_list:list = []
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

        
    def addItemMuscules(self):

        if  self.parent().getQuantityMangeSensor()> 0:
            self.list_class_choose_muscles =[]
            list_muscles:list =  self.getAllMuscles()
            list_users:list = self.getAllUsers()
            self.next.setEnabled(True)
            for j in range(self.parent().getQuantityMangeSensor()):
                self.list_class_choose_muscles.append(ChooseMuscles(id=j,id_list = self.id_list, list_users=list_users, list_muscles=list_muscles))
                self.verticalLayout_1.addLayout(self.list_class_choose_muscles[-1])
            

    def getAllMuscles(self)->list:
        dataList = []
        instance = DatabaseHandler()
        instance.createConnection()
        dataList = instance.getAllMuscles()
        instance.closeConnection()
        return dataList

    def getAllUsers(self)->list:
        datalist:list = []
        next_list:list = []
        
        users:list = []
        instance = DatabaseHandler()
        instance.createConnection()
        content = instance.findUsersForAdvanced(self.parent().user_login.get_id())
        if not content:
            content = []
        else:
            for con in content:
                next_list.append(con[0])
            datalist = instance.findUserByIdList(next_list)
        instance.closeConnection()



        for  x in datalist:
            self.id_list.append(x[0])
            users.append(str(x[1])+" "+str(x[2])+" "+str(x[4]))
        
        return users


    def selectItemChooseMuscules(self, s):
        objectName: str = str(self.sender().objectName())
        self.parent().addKeyValueMangeSensor(objectName, s)
        

    def selectItemActivity(self, index):
        self.many_muscles.setEnabled(True)
        item = self.many_muscles.model().itemFromIndex(index)
        self.lot_of_muscles =  int(item.text())
        self.parent().setQuantityMangeSensor(self.lot_of_muscles)
        if self.verticalLayout_1 is not None:
            self.parent().chooseLotsMusclesAdvancedShow()
        self.addItemMuscules()   
    
    def backScreen(self):
        self.parent().openLastWidget()

    def showScreen(self):
        # if self.many_muscles.currentText().__eq__("1"):
        #    self.parent().deleteKeyValueManageSensor("sensor_2")

        for i in self.list_class_choose_muscles:
            self.parent().addKeyValueMangeSensorUsers(name="sensor_"+str(i.getNumberBlocks()+1), name_surname=i.getNameUser(), muscules=i.getNameMuscles() )

        self.parent().addScreen(self.getWidget())
        self.parent().managmentSensorShow()
    
    def getWidget(self):
        return str(self.objectName())
