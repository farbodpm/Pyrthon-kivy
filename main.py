import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.graphics import Color, Bezier, Line
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

class amlakApp(App):
    def build(self):
        box = FloatLayout()
        textinput = TextInput(width=200,height=50,size_hint=(None, None),pos=(100,200),text='pasword', multiline=False)
        def on_focus(instance, value):
            instance.text = ""
        box.add_widget(textinput)
        textinput.bind(focus=on_focus)
        textinput = TextInput(width=200,height=50,size_hint=(None, None),pos=(100,300),text='user name', multiline=False)
        box.add_widget(textinput)
        textinput.bind(focus=on_focus)
        button = Button(size_hint=(None, None),pos=(100,25), text='amlakApp')
        box.add_widget(button)
        return box





if __name__ == '__main__':
   amlakApp().run()
