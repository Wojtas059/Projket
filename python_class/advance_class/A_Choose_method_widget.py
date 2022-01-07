import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen



class AChooseMethodWidget(Screen):
    reh = ObjectProperty(None)
    activ = ObjectProperty(None)

    def choose_clicked(self,text):
        if( text == "Aktywność"):
            self.activ.disabled = False
            self.reh.disabled = True
        else:
            self.reh.disabled = False
            self.activ.disabled = True