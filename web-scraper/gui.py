from scrape import *
import kivy
kivy.require('2.1.0') #required kivy version

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel

class MyLayout(Widget):
    
    search_box = ObjectProperty(None)
    result1 = ObjectProperty(None)
    result2 = ObjectProperty(None)
    
    def search(self):
        global url
        url = self.search_box.text
        Start().get_page(url)


class MyApp(App):

    def build(self):
        return MyLayout()


