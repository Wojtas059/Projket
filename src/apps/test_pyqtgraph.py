from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import queue
from random import randint
from src.grpc.python_client_server_dir.client_base_station_com.client import Client as ClientPi
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
from threading import Thread

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.dataQueue_1 = queue.Queue()
        self.x = list(range(300))  # 100 time points
        self.y = [randint(0,100) for _ in range(300)]  # 100 data points


        self.client_connect = ClientPi()
        if self.client_connect.connect() and self.client_connect.startSTM() :
            Thread(target=self.getDataSTM).start()

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
          # Add a new value 1 higher than the last.
        
        self.y = self.y[1:]  # Remove the first
        if self.dataQueue_1.qsize() > 0 :
            self.x.append(self.x[-1] + 1)
            self.y.append(self.dataQueue_1.get()) # Add a new random value.

        self.data_line.setData(self.x, self.y)
    
    def getDataSTM(self):

        if(self.client_connect.transfer_status):
            results = self.client_connect.stub.sendSTMData(ServicerMethods.Void())
            print(results)
            for result in results:
                try:
                    dupa = []
                    print(result.data)
                    dupa = result.data.split(',')
                    self.dataQueue_1.put(float(result.data))
                except IndexError:
                    pass
                except ValueError:
                    pass

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())