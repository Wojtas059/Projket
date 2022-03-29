import random
from itertools import count
from textwrap import indent
import pandas as pd
from threading import Thread
import matplotlib.pyplot as plt
import queue
from matplotlib.animation import FuncAnimation
from src.grpc.python_client_server_dir.client_base_station_com.client import Client as ClientPi
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []
y_vals_1 = []
marian = ClientPi()
marian.connect()
marian.startSTM()
index = count()
dataQueue = queue.Queue()


def animate(i):
    plt.subplot(211)
    x_vals.append(next(index))
    if dataQueue.qsize() > 0 :
        y_vals.append(dataQueue.get())
        y_vals.append(dataQueue.get())
    else:
        y_vals.append(5.0)
        y_vals_1.append(5.0)
    plt.cla()
    plt.plot(x_vals, y_vals)

    plt.subplot(212)
    plt.cla()
    plt.plot(x_vals, y_vals_1)

def data_stream():
    if(marian.transfer_status):
        results = marian.stub.sendSTMData(ServicerMethods.Void())
        for result in results:
            try:
                dupa = []
                dupa = result.data.split(',')
                print(dupa)
                dataQueue.put(float(dupa[0]))
                plt.cla()
                plt.plot(x_vals, y_vals)
            except IndexError:
                pass

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
#Thread(target=data_stream).start()

plt.tight_layout()
plt.show()
