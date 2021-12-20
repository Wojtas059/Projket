# kivy_venv\Scripts\activate
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.clock import Clock, mainthread
from kivy.loader import Loader
import kivy_b
import mygrid

    #def build(self):
    #    #return ScreenManagement()
    #    threading.Thread(target=self.manager.get_screen('mygrid').build).start()



class MyApp(App):
    def build(self):
        kivy_b.Upload()
        return mygrid.MyGrid()


        

if __name__ == '__main__':

    MyApp().run()
    