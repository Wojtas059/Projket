

from PyQt6 import QtCore , QtWidgets
from PyQt6.QtWidgets import (QWidget, QHBoxLayout)


class ChooseMuscles(QHBoxLayout):
    def __init__(self, **kwargs):
        super(ChooseMuscles, self).__init__()



        self.number = kwargs.get('number', 1)
        self.id = kwargs.get('id', '')
        self.muscles:str = kwargs.get('choose_muscles', 'Wybrane partie mięśni')
        self.name:str= kwargs.get('name_users', 'Gość Gość')

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.addItem(spacerItem)
        self.button = QtWidgets.QRadioButton()
        self.addWidget(self.button)

        self.name_users = QtWidgets.QLabel()
        self.name_users.setObjectName("choose_users")
        self.addWidget(self.name_users)
        self.choose_muscles = QtWidgets.QLabel()
        self.choose_muscles.setObjectName("choose_muscles")
        self.addWidget(self.choose_muscles)

        self.addItem(spacerItem)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.name_users.setText(_translate("Form", self.name))
        self.choose_muscles.setText(_translate("Form", self.muscles))


    
    def dupa(self):
        print(self.button.isChecked())



class ExperienceObservationWidget(QWidget):
    def __init__(self, parent):
        super(ExperienceObservationWidget, self).__init__(parent)
        self.list_class_choose_muscles:list =[]
        self.setObjectName("Choose Lots Muscles Advanced")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        
        self.scrollArea_2 = QtWidgets.QScrollArea()
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget(self)
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout.addWidget(self.scrollArea_2)
        
        
        self.data_sensor:dict = self.parent().manage_sensor.getDataSensor()
        for i in range(self.parent().getQuantityMangeSensor()):
            self.list_class_choose_muscles.append(ChooseMuscles( name_users=self.data_sensor['sensor_'+str(i+1)][0],choose_muscles=self.data_sensor['sensor_'+str(i+1)][1] ))
            self.verticalLayout_1.addLayout(self.list_class_choose_muscles[-1])

            
     
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.see_graph = QtWidgets.QPushButton()
        self.see_graph.setObjectName("see_graph")
        self.horizontalLayout_5.addWidget(self.see_graph)
        self.back = QtWidgets.QPushButton(self)
        self.back.setObjectName("back")
        #self.back.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.back)
        self.next = QtWidgets.QPushButton(self)
        self.next.setObjectName("next")
        self.horizontalLayout_5.addWidget(self.next)

        self.analitik = QtWidgets.QPushButton(self)
        self.analitik.setObjectName("analitic")
        self.analitik.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.analitik)

        self.start = QtWidgets.QPushButton(self)
        self.start.setObjectName("analitic")
        self.start.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.start)

        self.stop = QtWidgets.QPushButton(self)
        self.stop.setObjectName("stop")
        
        self.horizontalLayout_5.addWidget(self.stop)

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
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.back.setText(_translate("Form", "Wróć do menu"))
        self.stop.setText(_translate("Form", "Zatrzymaj"))
        self.next.setText(_translate("Form", "Zakończ"))
        self.analitik.setText(_translate("Form", "Analiza pomiarowa"))
        self.start.setText(_translate("Form", "Wznów"))
        self.see_graph.setText(_translate("Form", "Zobacz wykres"))

        
    def addActionButtons(self):
        self.next.clicked.connect(lambda: self.showScreen())
        self.back.clicked.connect(lambda: self.backScreen())
        self.see_graph.clicked.connect(lambda: self.graphShow())


    def backScreen(self):
        self.parent().openLastWidget()

    def showScreen(self):
        self.parent().videoPlayerShow()
    
    def getWidget(self):
        return str(self.objectName())

    def graphShow(self):
        self.parent().addScreen(self.getWidget())
        self.parent().graphObservationShow()

  