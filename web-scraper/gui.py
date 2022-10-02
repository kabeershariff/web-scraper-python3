import kivy
kivy.require('2.1.0') #required kivy version

from kivy.app import App
from kivy.uix.widget import Widget


class MyGridLayout(Widget):
        
    def search(self, instance):
        pass


class MyApp(App):

    def build(self):
        return MyGridLayout()

