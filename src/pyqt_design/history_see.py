import pyqtgraph as pg
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget
from pyqtgraph import PlotWidget, plot

from src.database_handlers.database_handler import DatabaseHandler


class HistorySeeWidget(QWidget):
    def __init__(self, parent):
        super(HistorySeeWidget, self).__init__(parent)

        self.setObjectName("History See")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem)
        self.labe_name = QtWidgets.QLabel()
        self.labe_name.setObjectName("choose_users")
        self.horizontalLayout_6.addWidget(self.labe_name)
        self.choose_muscles = QtWidgets.QComboBox(self)
        self.choose_muscles.setObjectName("choose_muscles")

        exp_measurment = self.getMeasurment()
        for i in exp_measurment:
            self.choose_muscles.addItem(
                str(i[2]) + " " + str(i[3]) + " dla " + str(i[2])
            )
        self.horizontalLayout_6.addWidget(self.choose_muscles)
        self.show = QtWidgets.QPushButton(self)
        self.show.setObjectName("show")
        self.show.setEnabled(False)
        self.horizontalLayout_6.addWidget(self.show)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem1)
        if not exp_measurment == []:
            self.show.setEnabled(True)

        self.scrollArea_2 = QtWidgets.QScrollArea()
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.x = []  # list(range(800))  # 100 time points
        self.y = []  # [0 for _ in range(800)]  # 100 data points
        self.graphWidget = pg.PlotWidget()
        self.verticalLayout_1.addWidget(self.graphWidget)
        self.data_line = self.graphWidget.plot(self.x, self.y)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(5)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem6)
        self.back = QtWidgets.QPushButton(self)
        self.back.setObjectName("back")
        self.horizontalLayout_5.addWidget(self.back)

        spacerItem7 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem7)
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

    def getMeasurment(self):
        instance = DatabaseHandler()
        instance.createConnection()
        if not self.parent().user_login.get_advanced():
            row = instance.findMeasurementAdvance(self.parent().user_login.get_id())
        else:
            row = instance.findMeasurement(self.parent().user_login.get_id())
        instance.closeConnection()
        return row

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.back.setText(_translate("Form", "Wróć"))
        self.show.setText(_translate("Form", "Pokaż"))
        self.labe_name.setText(_translate("Form", "Wybierz pomiar: "))

    def addActionButtons(self):
        self.back.clicked.connect(lambda: self.backScreen())

    def backScreen(self):
        self.parent().openLastWidget()

    def getWidget(self):
        return str(self.objectName())

    def update_plot_data(self):
        if self.parent().dataQueue_1.qsize() > 0:
            # self.x = self.x[1:]  # Remove the first y element.
            # Add a new value 1 higher than the last.

            # self.y = self.y[1:]  # Remove the first
            self.x.append(self.x[-1] + 1)
            self.y.append(self.parent().dataQueue_1.get())  # Add a new random value.

        self.data_line.setData(self.x, self.y)
