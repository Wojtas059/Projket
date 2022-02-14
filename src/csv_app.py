import kivy
from kivy.app import App
import src.python_class.kivy_csv_build as kivy_b
import src.proto_file.mygrid as mygrid
# replace with your current kivy version!
kivy.require('1.0.6')


class MyApp(App):
    def build(self):
        kivy_b.Upload()
        return mygrid.MyGrid()


if __name__ == '__main__':

    MyApp().run()
