
import logging
import struct
from queue import Queue
from threading import Thread

import serial
import serial.tools.list_ports
import serial.tools.list_ports as list_ports
from serial.tools.list_ports_common import ListPortInfo

import file.proto_comm as proto_comm


class Connect:
    queue = Queue()


    trump = False
    def start(self):
        Thread(target=self.on_press).start()
    def stop(self):
        Thread(target=self.on_stop).start()
    def on_press(self):
            self.trump = True
            try:
                comm = proto_comm.ProtobufComm('/dev/ttyACM0', 115200)
                comm.stm.flush()
                comm.stm.read_all()
                comm.stm.flushInput()
                comm.stm.flushOutput()
                comm.start_data_output()
                while self.trump:
                    self.queue.put(comm.handle_data() )
                comm.stm.flush()
                comm.stm.flushInput()
                comm.stm.read_all()
                comm.stm.flushOutput()
                comm.stop_data_output()
                comm = None
            except serial.serialutil.SerialException:
                logging.error(serial.serialutil.SerialException)
            except struct.error:
                logging.error(struct.error)

    
    def on_stop(self):
        self.trump = False
        
