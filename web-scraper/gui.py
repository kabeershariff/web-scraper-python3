import kivy
kivy.require('2.1.0') #required kivy version

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Layout(GridLayout):
    #initialize
    def __init__(self, **kwargs):
        #calling constructor
        super(Layout, self).__init__(**kwargs)
        
        #column number
        self.cols = 2

        #widgets

        #search box
        self.search_box = TextInput(multiline = False)
        self.add_widget(self.search_box)

        #search button
        self.search_button = Button(text="Search")
        self.add_widget(self.search_button)
        
        self.search_button.bind(on_press=self.search)

    def search(self, instance):
        query = self.search_box.text
        print(query)


class MyApp(App):

    def build(self):
        return Layout()

