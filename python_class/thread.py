from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.properties import *
from kivy.core.window import Window
from kivy.clock import Clock, mainthread
import threading
import time


########################################################################
class ScreenManagement(ScreenManager):
    pass

class MenuScreen(Screen):
    def routine(self):
        self.parent.current = 'program' 
        threading.Thread(target=self.manager.get_screen('program').build).start()

class ProgramScreen(Screen):

    @mainthread
    def update_label(self, int_counter, new_text):
        if int_counter == 0 :
            self.filler1.text = new_text
        elif int_counter == 1 :
            self.filler2.text = new_text
        elif int_counter == 2 :
            self.filler3.text = new_text
        elif int_counter == 3 :
            self.filler4.text = new_text
        else:
            self.filler1.text = "fault"

#dummy function to be replaced with a function that will call GPIO for input and feedback.
    def func (self,value):
        for i in xrange(10*(value+1)): 
            if ((i%3) == 0):
                self.update_label(int(value),str(i))
                time.sleep(1)
        

    def build(self):
        NumberofFiller = 2
        NumberofCells = 5
        CellCounter = 0
        while CellCounter < NumberofCells:
            try:
                threads = []
                print ('Counter:',CellCounter,'Fillers:',NumberofFiller,'Cells:',NumberofCells)     
                for i in range (NumberofFiller):
                    t = threading.Thread(target=self.func, args=((CellCounter%NumberofFiller),))
                    t.start()
                    threads.append(t)
                    CellCounter = CellCounter +1

                for x in threads:
                    #Problem I believe is here.
                    x.join()
                    #Need a way to pause the While loop for the first set of threads to finish before starting the next threads.
#                print (threads)
            except (KeyboardInterrupt, SystemExit):
                functions.cleanAndExit() 


########################################################################
Builder.load_file("Menu_red.kv") #Not needed
class Menu_red2App(App):
    def build(self):
        return ScreenManagement()

#----------------------------------------------------------------------
if __name__ == "__main__":
    Menu_red2App().run()