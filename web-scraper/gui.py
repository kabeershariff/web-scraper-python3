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
        
        #main grid column number
        self.cols = 1
        
        #top grid
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        self.add_widget(self.top_grid)

        #widgets

        #search box
        self.search_box = TextInput(multiline = False)
        self.top_grid.add_widget(self.search_box)

        #search button
        self.search_button = Button(text="Search")
        self.top_grid.add_widget(self.search_button)
        
        self.search_button.bind(on_press=self.search)

        #results here
        self.result = TextInput(multiline =True)
        self.add_widget(self.result)

    def search(self, instance):
        pass
        #query = self.search_box.text


class MyApp(App):

    def build(self):
        return Layout()

