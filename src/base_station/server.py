import queue
import serial
# isort: split

from src.base_station.flags import notifications_flags, pending_actions_flags, work_flags


class server:

    _work_flags = work_flags.WorkFlags
    _pending_actions_flags = pending_actions_flags.PendingActionFlags
    _notifications_flags = notifications_flags.NotificationFlags

    def __init__(self):
        # Flags init
        self.work = self._work_flags.WORK
        self.pendingAction = self._pending_actions_flags.WAITING
        self.notification = self._notifications_flags.NONOTYFICATION
        # Serial init
        self.serialport = serial.Serial()
        self.serialport.port = "COMX"
        self.serialport.baudrate = 115200
        self.serialport.open()
        # Queue init
        self.dataFrame = queue.Queue()

    def API_DECODE(self, pendingAction: pending_actions_flags.PendingActionFlags):
        if self.dataFrame.qsize() > 0:
            command = self.dataFrame.get()
            if pendingAction == self._pending_actions_flags.WAITING:
                pass
        return self._notifications_flags.NONOTYFICATION

    def API_WORKER(self, notification: notifications_flags.NotificationFlags):
        if notification == self._notifications_flags.NONOTYFICATION:
            pass

    def mainLoop(self):
        # Tutaj można by było dać urocheminie parsera
        while self.work == self._work_flags.WORK:
            while self.pendingAction != self._pending_actions_flags.WAITING:
                self.API_WORKER(self.API_DECODE(self.pendingAction))

    def commandParser(self):
        if self.serialport.is_open:
            while self.work == self._work_flags.WORK:
                while self.serialport.in_waiting > 0:
                    dataFrame = self.serialport.read()
                    # Operacje rozpoznywania danych może jakieś proto czy co tam będzie
                    self.dataFrame.put(dataFrame)
