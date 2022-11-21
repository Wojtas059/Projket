# Form implementation generated from reading ui file 'start_reference_widget.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget


class ObservationReference(QWidget):
    def __init__(self, parent):
        super(ObservationReference, self).__init__(parent)
        self.setObjectName("Observation Reference")

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

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem4)
        self.start = QtWidgets.QPushButton(self)
        self.start.setObjectName("START")
        self.start.setMinimumSize(QtCore.QSize(200, 48))
        self.start.setMaximumSize(QtCore.QSize(200, 48))
        self.horizontalLayout_4.addWidget(self.start)
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem6)
        self.save_file = QtWidgets.QPushButton(self)
        self.save_file.setObjectName("Zapisz wyniki")
        self.save_file.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.save_file)
        spacerItem7 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

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
        self.next.setEnabled(False)
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
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(
            _translate(
                "Form",
                "Naciśnij przycisk START aby wykonać ćwiczenie pokazane wcześniej",
            )
        )
        self.back.setText(_translate("Form", "Wróć"))
        self.next.setText(_translate("Form", "Dalej"))
        self.start.setText(_translate("Form", "START"))
        self.save_file.setText(_translate("From", "Zapisz wyniki"))

    def addActionButtons(self):
        self.next.clicked.connect(lambda: self.showScreen())
        self.start.clicked.connect(lambda: self.startClicked())
        self.back.clicked.connect(lambda: self.backScreen())

    def startClicked(self):
        self.next.setEnabled(True)
        self.save_file.setEnabled(True)

    def backScreen(self):
        self.parent().openLastWidget()

    def showScreen(self):
        self.parent().addScreen(self.getWidget())
        self.parent().startExperienceShow()

    def getWidget(self):
        return str(self.objectName())
