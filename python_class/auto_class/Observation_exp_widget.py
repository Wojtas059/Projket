import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.graph import Graph, MeshLinePlot
from math import sin
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
#import matplotlib.pyplot as plt
#
#
# = [1,2,3,4,5]
# = [5, 12, 6, 9, 15]
#
#lt.plot(x,y)
#lt.ylabel("This is MY Y Axis")
#lt.xlabel("X Axis")


class ObservationExpWidget(Screen):

#   def __getattr__(self, item):
#       None
    graph_test = ObjectProperty(None)
    def on_load(self):
        self.update_graph()
        
    def update_graph(self):
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        self.graph_test.add_plot(plot)
        #
        