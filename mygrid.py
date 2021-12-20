import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from threading import Thread 
import time
import ctypes
import asynckivy as ak
from tkinter import filedialog
import os
import class_other
import serial.tools.list_ports as list_ports
from serial.tools.list_ports_common import ListPortInfo
import struct
import proto_comm
import sys
import serial
from kivy.uix.spinner import Spinner



class MyGrid(Widget):
    com = ObjectProperty(None)
    mainbutton = ObjectProperty(None)
    comm = None
    trump =False
    port = ''

    def __init__(self, **var_args):
        super(MyGrid, self).__init__(**var_args)
        self.dropdown = class_other.CustomDropDown()
        self.mainbutton.bind(on_release=self.dropdown.open)
    ## Added button to FloatLayout so inherits this class 
        self.dropdown.bind(on_select = lambda\
                           instance, x: setattr(self.mainbutton, 'text', x))

    


    def on_press(self):
        try:   
            self.comm = proto_comm.ProtobufComm( class_other.CustomDropDown().port, 115200)
            self.comm.stm.flush()
            self.comm.stm.read_all()
            self.comm.stm.flushInput()
            self.comm.stm.flushOutput()
            self.comm.start_data_output()
            self.com.text += "\nRozpozęto pomiar\n\n"
            self.com.text = self.comm.start_pom()
            while self.trump:
                self.com.text += self.comm.handle_data()
            self.comm.stm.flush()
            self.comm.stm.flushInput()
            self.comm.stm.read_all()
            self.comm.stm.flushOutput()
            self.comm.stop_data_output()
            self.comm = None

        except serial.serialutil.SerialException:
             Thread(target = self.error_win("Błąd połączenia się z portem ")).start()
        except struct.error:
            Thread(target = self.error_win('Urządzenie zostało odłączone')).start()
        except TypeError:
            Thread(target = self.error_win("Błąd połączenia się z portem ")).start()

        self.trump =False

        




    def ___on_press(self):
        self.trump = True
        file = open("scope_126.csv")
        dataArray1 = []
        for lin in file:
            dataArray1 = lin.split(',')
            self.save_file(dataArray1)
            if not (self.trump):
                break


    def start_thread(self):
        if not(self.trump):
            self.trump =True
            Thread(target = self.on_press()).start()
            
                
        else:
            Thread(target = self.error_win("Już uruchomiłeś pomiar")).start()
        

    def error_win(self, error_txt):
        ctypes.windll.user32.MessageBoxW(None, error_txt, "Error", 0)

    def on_press_false(self):
        if (self.trump):
            self.trump = False
            time.sleep(0.2)
            self.com.text += "Pomiar Zastopowano"
        
        



    
    def stop(self):
        Thread(target=self.on_press_false()).start()
        
    def save_file(self, dataArray1):
        f = open("zapis.csv", "a")
        f.write(",".join(dataArray1))
        f.close()
        self.com.text += ",".join(dataArray1)

    def save_file_(self):
        Thread(target = self.file_load).start()
        
    def file_load(self):
        filedialog.askopenfilename()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.com.text)

        self.dismiss_popup()