import kivy
kivy.require('2.1.0') #required kivy version

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    
    search_box = ObjectProperty(None)
    result = ObjectProperty(None)
    
    def search(self):
        pass


class MyApp(App):

    def build(self):
        return MyGridLayout()

