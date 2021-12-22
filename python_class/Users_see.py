import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.properties import BooleanProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import  Screen
from kivy.metrics import dp
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class EditStatePopup(Popup):
    col_data = ListProperty(["?", "?"])
    index = NumericProperty(0)

    def __init__(self, obj, **kwargs):
        super(EditStatePopup, self).__init__(**kwargs)
        self.index = obj.index
        self.col_data[0] = obj.rv_data[self.index]["Id"]
        self.col_data[1] = obj.rv_data[self.index]["Name"]



class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    rv_data = ObjectProperty(None)
    start_point = NumericProperty(0)

    def __init__(self, **kwargs):
        super(SelectableButton, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, .0005)



    def update(self, *args):
        self.text = self.rv_data[self.index][self.key]

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        self.rv_data = rv.data



    def on_press(self):
        popup = EditStatePopup(self)
        popup.open()

class MyRV(RecycleView):
    def __init__(self, **kwargs):
        super(MyRV, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.selectedItem = -1

    def _keyboard_closed(self):
        pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'down':
            self.clearAll()
            self.nextItem()
            print('down')
        elif keycode[1] == 'up':
            self.clearAll()
            self.prevItem()
            print("up")
        elif keycode[1] == 'e' and len(modifiers) > 0 and modifiers[0] == 'ctrl':
            self.view_adapter.views[self.selectedItem].on_press()

    def clearAll(self):
        if (self.selectedItem > -1):
            for i in range(len(self.view_adapter.views) - 1):
                self.view_adapter.views[self.selectedItem].selected = 0


    def nextItem(self):
        if self.selectedItem < len(self.view_adapter.views) - 1:
            self.selectedItem += 1
        else:
            self.selectedItem = 0
        self.view_adapter.views[self.selectedItem].selected = 1
        print(self.selectedItem)


    def prevItem(self):
        if self.selectedItem > 0:
            self.selectedItem -= 1
        else:
            self.selectedItem = len(self.view_adapter.views) - 1
        self.view_adapter.views[self.selectedItem].selected = 1
        print(self.selectedItem)
class RV(RecycleView):
    data_items = ListProperty([])
    col1 = ListProperty()
    col2 = ListProperty()

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.get_states()

    def update(self):
        self.col1 = [{'Id': str(x[0]), 'Name': x[1], 'key': 'Id', 'text': str(x[2])} for x in self.data_items]
        self.col2 = [{'Id': str(x[0]), 'Name': x[1], 'key': 'Name', 'text': str(x[2])} for x in self.data_items]


    def get_states(self):
        rows = [(1, 'Test1'), (2, 'Test2'), (3, 'Test3')]

        i = 0
        for row in rows:
            self.data_items.append([row[0], row[1], i])
            i += 1
        print(self.data_items)
        self.update()

class MainMenu(BoxLayout):
    states_cities_or_areas = ObjectProperty()

    def display_states(self):
        self.remove_widgets()
        self.rv = RV()
        self.states_cities_or_areas.add_widget(self.rv)

    def remove_widgets(self):
        self.states_cities_or_areas.clear_widgets()




class UsersSeeWidget(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(MainMenu())

