import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
import time
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

class IncrediblyCrudeClockA(Label):
    a = NumericProperty(4)  # seconds
        
    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "STOP"
            self.parent.finish()
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

class BoxLayout_A(BoxLayout):
    def finish(self):
        self.parent.next.disabled = False

class AObservationRefWidget(Screen):
    timeer_A = ObjectProperty(None)
    next = ObjectProperty(None)
    start = ObjectProperty(None)


    def on_load(self): 
        self.timeer_A.start()