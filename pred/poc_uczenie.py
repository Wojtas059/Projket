from collections import deque
from csv import reader
import multiprocessing
import queue
import threading
from pred_class import Prediction 
import pandas



class Test():
    emg_queue = queue.Queue()
    mmg_queue = queue.Queue()
    is_pred_activated = False
    is_pred_working =False
    data_frame= pandas.DataFrame()
    is_reading_end=False
    do_it_once=True
    def launch_pred(self):
        while(True):
            if self.is_pred_activated and not self.is_pred_working:
                self.is_pred_working=True
                print("Działam")
                shared_result=multiprocessing.Queue()
                prediction=Prediction(df=self.data_frame,queue_result=shared_result)
                prediction.start()
                prediction.join()
                print("Powinnien być tu wynik")
                print(shared_result.get())
                self.is_pred_working=False
                self.is_pred_activated= False



    def read_file(self):
        with open('TRAINING_03.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                my_row=row[0].split(";")
                self.emg_queue.put(my_row[0])
                self.mmg_queue.put(my_row[1])
        print("Skończyłem czytać")
      
        self.is_reading_end=True

    def check_queue(self):
        while(True):
            if  self.emg_queue.qsize() >= 400 and self.mmg_queue.qsize() >= 400 and not self.is_pred_activated:
                print("Wielkość emg_queue")
                print(self.emg_queue.qsize())
                mmg_list = list()
                emg_list = list()
                for _ in range(400):
                    mmg_list.append(self.mmg_queue.get())
                    emg_list.append(self.emg_queue.get())
                self.data_frame["MMG"]=mmg_list
                self.data_frame["EMG"]=emg_list
                self.data_frame['MMG'] = self.data_frame['MMG'].astype(float)
                self.data_frame['EMG'] = self.data_frame['EMG'].astype(float)
                self.is_pred_activated = True
                if self.do_it_once:
                    self.do_it_once=False
                    print("Tak byłem tutaj i włączyłem śmiecia")
            

test = Test()
try:
    print("Zaczynam t1")
    t1=threading.Thread(target=test.read_file)
    t1.start()
    print("Zaczynam t2")
    t2=threading.Thread(target=test.check_queue)
    t2.start()
    print("Zaczynam t3")
    t3=threading.Thread(target=test.launch_pred)
    t3.start()
except Exception:
    t1.join()
    t2.join()
    t3.join()