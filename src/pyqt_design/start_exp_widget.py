# Form implementation generated from reading ui file 'start_reference_widget.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QWidget


class StartExperience(QWidget):
    def __init__(self, parent):
        super(StartExperience, self).__init__(parent)
        self.setObjectName("Start Experience")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
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
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem2)
        self.back = QtWidgets.QPushButton(self)
        self.back.setObjectName("back")
        self.horizontalLayout_5.addWidget(self.back)
        self.next = QtWidgets.QPushButton(self)
        self.next.setObjectName("next")
        self.horizontalLayout_5.addWidget(self.next)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 220))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi()
        self.addActionButtons()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Start Experience", "Start Experience"))
        self.label.setText(_translate("Start Experience", "Rozpoczęcie Badania"))
        self.back.setText(_translate("Start Experience", "Wróć"))
        self.next.setText(_translate("Start Experience", "START"))

    def addActionButtons(self):
        self.next.clicked.connect(lambda: self.showScreen())
        self.back.clicked.connect(lambda: self.backScreen())

    def backScreen(self):
        self.parent().openLastWidget()

    def showScreen(self):
        if self.parent().connectBaseStation():
            self.parent().addScreen(self.getWidget())
            self.parent().experienceObservationShow()
        else:
            self.createMessageBox("Nie udało się połączyć ze stacją bazową")

    def createMessageBox(self, message: str):
        msg = QMessageBox()
        msg.setWindowTitle("Błąd")
        msg.setText(message)
        msg.exec()

    def getWidget(self):
        return str(self.objectName())
