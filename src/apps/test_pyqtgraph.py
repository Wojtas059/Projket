import os
import queue
import sys  # We need sys so that we can pass argv to QApplication
from datetime import datetime
from random import randint
from threading import Thread

import pyqtgraph as pg
from numpy import average
from PyQt5 import QtCore, QtWidgets
from pyqtgraph import PlotWidget, plot

import grpc
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
from src.grpc.python_client_server_dir.client_base_station_com.client import (
    Client as ClientPi,
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.dataQueue_1 = queue.Queue()
        self.dataQueue_20_value = queue.Queue()
        self.dataQueue_aa = queue.Queue()
        self.x = list(range(700))  # 100 time points
        self.y = [0 for _ in range(700)]  # 100 data points
        # Thread(target=self.saveFileValue).start()

        Thread(target=self.function).start()

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def function(self):
        while True:
            f = open("static/po/test.csv", "r")

            for i in f:
                self.dataQueue_1.put(float(i))

    def update_plot_data(self):

        if self.dataQueue_1.qsize() > 0:
            self.x = self.x[1:]  # Remove the first y element.
            # Add a new value 1 higher than the last.

            self.y = self.y[1:]  # Remove the first
            self.x.append(self.x[-1] + 1)
            self.y.append(self.dataQueue_1.get())  # Add a new random value.

        self.data_line.setData(self.x, self.y)

    def getDataSTM(self):
        self.licznik = 0
        dataarray: list = []
        # try:
        if self.client_connect.transfer_status:
            results = self.client_connect.stub.sendSTMData(ServicerMethods.Void())
            print(results)
            self.licznik += 1
            for result in results:

                try:

                    print(result.data)
                    dataarray = result.data.split(",")
                    self.dataQueue_1.put(float(dataarray[0]))
                    # self.dataQueue_20_value.put(float(result.data))
                except IndexError:
                    pass
                except ValueError:
                    pass

        # if self.licznik >= 20:
        #    sum=0
        #    while self.dataQueue_20_value.qsize() > 0 :
        #        sum += self.dataQueue_20_value.get()
        #    self.licznik=0
        #    self.dataQueue_aa.put(float(sum/20))
        # except _MultiThreadedRendezvous as e:
        #    if e.code() == grpc.StatusCode.CANCELLED:
        #        pass
        #        # process cancelled status

    #
    #    elif e.code() == grpc.StatusCode.UNAVAILABLE and 'Connection reset by peer' in e.details():
    #        pass
    #        # process unavailable status
    #
    #    else:
    #        raise
    def average(self):
        if self.licznik >= 20:
            sum = 0
            while self.dataQueue_20_value.qsize() > 0:
                sum += self.dataQueue_20_value.get()
            self.licznik = 0

    def saveFileValue(self):
        now = datetime.now()
        f = open(
            "static/csv_saves/pomiary/zapis_"
            + now.strftime("%d_%m_%Y")
            + "_"
            + now.strftime("%H_%M_%S")
            + ".csv",
            "a",
        )
        while True:
            if self.dataQueue_1.qsize() > 0:
                self.dataQueue_1.get()  # Add a new random value.
                f.write(self.dataQueue_1.get())


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
