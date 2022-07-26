import threading
from enum import _auto_null, auto

import kivy

kivy.require("1.0.6")  # replace with your current kivy version !
import _thread
import asyncio
import ctypes
import logging
import os
import queue
import struct
import sys
import time
from datetime import datetime
from threading import Thread
from tkinter import filedialog

import serial
import serial.tools.list_ports as list_ports
from kivy.clock import Clock, mainthread
from kivy.loader import Loader
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from serial.tools.list_ports_common import ListPortInfo

import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
import src.proto_file.proto_comm as proto_comm
from src.grpc.python_client_server_dir.client_base_station_com.client import (
    Client as ClientPi,
)


class MyGrid(Widget):
    com = ObjectProperty(None)
    comm = None
    port = ""
    name_csv = ObjectProperty(None)
    csvQueue = queue.Queue()

    # Zmienna odpowiedzilana za połączenie z raspberrypi
    client_connect = None

    def __init__(self, **var_args):
        super(MyGrid, self).__init__(**var_args)
        try:
            os.mkdir("pomiary")
        except FileExistsError:
            pass

    trump = False

    def auto_connect(self):
        # portData = serial.tools.list_ports.comports()
        # commPport = "None"
        # dataport = []
        # for j in portData:
        #    dataport = str(j).split()
        #    for i in dataport:
        #        if i == "STMicroelectronics":
        #            self.port = dataport[0]
        #            commPport = "Start"
        #            Thread(
        #                target=self.error_win("Urządzenie zostało podłączone")
        #            ).start()
        #            break

        # if commPport == "Start":
        #    self.start_thread()

        self.client_connect = ClientPi()
        if self.client_connect.connect() and self.client_connect.startSTM():
            Thread(target=self.getDataSTM).start()
        else:
            self.error_win("Błąd połączenia się z portem ")

    def getDataSTM(self):
        # file = open("data_stm_sampling.csv","w")
        # file.write("Value A, Value B, Value C, Constant value\n")
        # print("Dupa")
        # file.close
        # queue_data = queue.Queue()
        self.com.text += "\nRozpoczęto pomiar\n\n"
        self.csvQueue.put_nowait("Value A, Value B, Value C, Constant value")
        if self.client_connect.transfer_status:
            results = self.client_connect.stub.sendSTMData(ServicerMethods.Void())

            print(results)
            for result in results:
                print(result.data)
                self.com.text += str(result.data) + "\n"
                self.csvQueue.put_nowait(result.data)

            #    #file.write(result.data)

        print(results)
        # for result in results:
        #    print(result.data)
        #    self.com.text += result.data
        #    self.csvQueue.put_nowait(result.data)
        # ile = open("data_stm_sampling.csv","a")
        # hile queue_data.qsize() > 0:
        #   file.write(queue_data.get())
        # ile.close

    def on_press(self):
        self.trump = True
        try:

            self.comm = proto_comm.ProtobufComm(self.port, 115200)
            self.comm.stm.flush()
            self.comm.stm.read_all()
            self.comm.stm.flushInput()
            self.comm.stm.flushOutput()
            self.comm.start_data_output()
            self.com.text += "\nRozpozęto pomiar\n\n"
            self.com.text = self.comm.start_pom()
            self.csvQueue.put_nowait(self.comm.start_pom())
            while self.trump:
                line_from_stm_output = self.comm.handle_data()
                self.com.text += line_from_stm_output
                self.csvQueue.put_nowait(line_from_stm_output)
            self.comm.stm.flush()
            self.comm.stm.flushInput()
            self.comm.stm.read_all()
            self.comm.stm.flushOutput()
            self.comm.stop_data_output()
            self.comm = None
        except serial.serialutil.SerialException:
            logging.error(serial.serialutil.SerialException)
            Thread(target=self.error_win("Błąd połączenia się z portem ")).start()
        except struct.error:
            logging.error(struct.error)
            Thread(target=self.error_win("Urządzenie zostało odłączone")).start()
        except TypeError:
            logging.error(TypeError)
            Thread(target=self.error_win("Błąd połączenia się z portem ")).start()
        self.trump = False

    def spinner_clicked(self, value):
        self.port = value

    def save_file(self):
        self.trump = True
        now = datetime.now()
        f = open(
            "static/csv_saves/pomiary/zapis_"
            + now.strftime("%d_%m_%Y")
            + "_"
            + now.strftime("%H_%M_%S")
            + ".csv",
            "w",
        )
        dataArray1 = []
        if self.name_csv.text == "":
            f.write("Tu znajduje sie opis mojich pomiarow\n")
        else:
            f.write(self.name_csv.text + "\n")
        while self.csvQueue.qsize() > 0:
            dataArray1 = self.csvQueue.get_nowait()
            f.write(str(dataArray1))
        f.close()
        self.trump = False

    def start_thread(self):
        if not (self.trump):
            self.com.text = "Rozpozęto pomiar"
            Thread(target=self.on_press).start()
        else:
            Thread(target=self.error_win("Już uruchomiłeś pomiar")).start()

    def error_win(self, error_txt):
        ctypes.windll.user32.MessageBoxW(None, error_txt, "Error", 0)

    def on_press_false(self):
        self.client_connect.stopSTM()
        # if self.trump:
        #    self.trump = False
        #    time.sleep(0.2)
        #    self.com.text += "Pomiar Zastopowano"

    def stop(self):
        Thread(target=self.on_press_false).start()

    def save_file_(self):
        Thread(target=self.save_file).start()

    def file_load(self):
        filedialog.askopenfilename()

    def save(self, path, filename):
        with open(os.path.join(path, filename), "w") as stream:
            stream.write(self.com.text)
