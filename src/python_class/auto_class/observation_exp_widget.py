from itertools import count
from math import sin

# isort: split
import kivy
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from threading import Thread
from collections import deque
import numpy
from itertools import count
from src.grpc.python_client_server_dir.client_base_station_com.client import Client as ClientPi
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import matplotlib.pyplot as plt
kivy.require("1.0.6")  # replace with your current kivy version !

# from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
# import matplotlib.pyplot as plt
#
#
# = [1,2,3,4,5]
# = [5, 12, 6, 9, 15]
#
# lt.plot(x,y)
# lt.ylabel("This is MY Y Axis")
# lt.xlabel("X Axis")


class ObservationExpWidget(Screen):
    
    #   def __getattr__(self, item):
    #       None
    graph_test = ObjectProperty(None)
    box = ObjectProperty(None)
    def on_load(self):
        self=[]
        self.y=[]
        self.update_graph()
        if self.parent.status_connection():
            self.parent.client_connect.startSTM()
            Thread(target=self.getDataSTM).start()

    def update_graph(self):
        index = count()
        
        self.x.append(next(index))
        self.y.append(1.0)
        plt.plot(self.x,self.y)
        plt.ylabel("Dupa")
        plt.xlabel("Twoja stara")
        self.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def getDataSTM(self):
        index = count()
        points = []
        if(self.parent.client_connect.transfer_status):
            results = self.parent.client_connect.stub.sendSTMData(ServicerMethods.Void())
            print(results)
            for result in results:
                try:
                    dupa = []
                    dupa = result.data.split(',')
                    self.x.append(next(index))
                    self.y.append(float(dupa[0]))
                    plt.plot(self.x,self.y)





                   #points.pop(0)
                
                   #points_dequeued=deque(points)
                   #points_dequeued.rotate(-1)
                   #points_dequeued=list(points_dequeued)
                   #dupa = []
                   #dupa = result.data.split(',')
                   ##print(dupa[0])
                   #points_dequeued.append((  998,float(dupa[0])   ))
                   #print(points_dequeued[-1])
                   #self.plot.points = points_dequeued
                   #self.graph_test.add_plot(self.plot.points)
                except IndexError:
                    pass