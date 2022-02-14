import enum
import queue
import serial


class server:
    class WorkFlags(enum):
        WORK = 1
        STOP = 0

    class PendingActionFlags(enum):
        WAITING = 1
        CONNECNTION = 2
        HANDSHAKE = 3
        DATA = 4

    class NotificationFlags(enum):
        NONOTYFICATION = 1

    def __init__(self):
        # Flags init
        self.work = self.WorkFlags.WORK
        self.pendingAction = self.PendingActionFlags.WAITING
        self.notification = self.NotificationFlags.NONOTYFICATION
        # Serial init
        self.serialport = serial.Serial()
        self.serialport.port = "COMX"
        self.serialport.baudrate = 115200
        self.serialport.open()
        # Queue init
        self.dataFrame = queue.Queue()

    # TODO Dyskusja co do metody przesyłu i odbioru danych, ważne i to cholernie
    def wifiConnection(self):
        pass

    def API_DECODE(self, pendingAction: PendingActionFlags):
        if self.dataFrame.qsize() > 0:
            command = self.dataFrame.get()
            if pendingAction == self.PendingActionFlags.WAITING:
                pass
        return self.NotificationFlags.NONOTYFICATION

    def API_WORKER(self, notification: NotificationFlags):
        if notification == self.NotificationFlags.NONOTYFICATION:
            pass

    def mainLoop(self):
        # Tutaj można by było dać urocheminie parsera
        while self.work == self.WorkFlags.WORK:
            while self.pendingAction != self.PendingActionFlags.WAITING:
                self.API_WORKER(self.API_DECODE(self.pendingAction))

    def commandParser(self):
        if self.serialport.is_open:
            while self.work == self.WorkFlags.WORK:
                while self.serialport.in_waiting > 0:
                    dataFrame = self.serialport.read()
                    # Operacje rozpoznywania danych może jakieś proto czy co tam będzie
                    self.dataFrame.put(dataFrame)
