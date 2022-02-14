import kivy
from kivy.animation import Animation
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
kivy.require("1.0.6")  # replace with your current kivy version !


class IncrediblyCrudeClock(Label):
    a = NumericProperty(3)  # seconds

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)

        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "STOP"
            self.parent.finish()

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)


class BoxLayout_(BoxLayout):
    def finish(self):
        self.parent.next.disabled = False


class ObservationRefWidget(Screen):
    timeer_ = ObjectProperty(None)
    next = ObjectProperty(None)
    start = ObjectProperty(None)

    def on_load(self):
        self.timeer_.start()
