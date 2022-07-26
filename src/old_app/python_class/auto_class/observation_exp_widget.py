from itertools import count
from math import sin

# isort: split
import queue
from itertools import count
from threading import Thread

import kivy
import matplotlib.pyplot as plt
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from matplotlib.animation import FuncAnimation

import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
from src.grpc.python_client_server_dir.client_base_station_com.client import (
    Client as ClientPi,
)

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
    sensor_1 = ObjectProperty(None)
    sensor_2 = ObjectProperty(None)
    index = count()
    x_vals = []
    y_vals = []
    x_vals_1 = []
    y_vals_1 = []
    dataQueue_1 = queue.Queue()
    dataQueue_2 = queue.Queue()

    def on_load(self):
        self.sensor_1.disabled = False
        if self.parent.get_many() > 1:
            self.sensor_2.disabled = False
        else:
            self.sensor_2.disabled = True
        # Thread(target=self.update_graph).start()
        if self.parent.status_connection():
            self.parent.client_connect.startSTM()
            Thread(target=self.getDataSTM).start()

    def animate(self, i):
        self.x_vals.append(next(self.index))
        if self.dataQueue_1.qsize() > 0:
            self.y_vals.append(self.dataQueue_1.get())

        else:
            self.y_vals.append(5.0)

        if self.dataQueue_2.qsize() > 0:
            self.y_vals_1.append(self.dataQueue_2.get())

        else:
            self.y_vals_1.append(5.0)

        plt.cla()
        plt.subplot(211)
        plt.plot(self.x_vals, self.y_vals)
        plt.xlim(i - 49, i)
        plt.subplot(212)
        plt.cla()
        plt.plot(self.x_vals, self.y_vals_1)
        plt.xlim(i - 49, i)

    def update_graph(self):
        plt.figure(1)
        plt.style.use("fivethirtyeight")
        plt.plot()

        # self.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.ani = FuncAnimation(plt.gcf(), self.animate, interval=100)
        plt.tight_layout()
        plt.show()

    def getDataSTM(self):
        if self.parent.client_connect.transfer_status:
            results = self.parent.client_connect.stub.sendSTMData(
                ServicerMethods.Void()
            )
            print(results)
            for result in results:
                try:
                    dupa = []
                    dupa = result.data.split(",")
                    self.dataQueue_1.put(float(dupa[0]))
                    # self.dataQueue_2.put(float(dupa[1]))

                # points.pop(0)

                # points_dequeued=deque(points)
                # points_dequeued.rotate(-1)
                # points_dequeued=list(points_dequeued)
                # dupa = []
                # dupa = result.data.split(',')
                ##print(dupa[0])
                # points_dequeued.append((  998,float(dupa[0])   ))
                # print(points_dequeued[-1])
                # self.plot.points = points_dequeued
                # self.graph_test.add_plot(self.plot.points)
                except IndexError:
                    pass
                except ValueError:
                    pass

    def stop_stream_data(self):
        self.parent.client_connect.stopSTM()
        # self.ani.event_source.stop()
        # del self.ani
        plt.close()

    def see_plot(self):
        Thread(target=self.update_graph).start()
