import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.lang import Builder
import os.path
from kivy.resources import resource_add_path

def Upload():
    #KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './kivy_bulider/___my.kv'))
    #resource_add_path(KV_PATH)
    Builder.load_file('kivy_bulider/csv.kv')



