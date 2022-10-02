import kivy
kivy.require('2.1.0') #required kivy version

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text="Blank")

